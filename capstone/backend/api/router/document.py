import os
import io
import json
import time
import logging

from pypdf import PdfReader
from dotenv import load_dotenv
from fastapi.responses import JSONResponse
from fastapi import (
    File,
    Form,
    Depends,
    APIRouter,
    UploadFile,
    HTTPException
    )

from capstone.backend.llms import RAGModel, get_RAG
from capstone.backend.api.models import FileLength
from capstone.backend.database import (
    get_db, 
    DBConnection,
    DocumentTable,
    )

load_dotenv()
logging.getLogger(__name__)
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", default="bge-m3")

tags = ["Document"]
router_document = APIRouter(prefix='/document')

# Uploadfile PDF from API.
@router_document.post("/uploadfile", tags=tags)
async def uploadFile(
    data: str = Form(default={"first_page":0,"final_page":0}), 
    file: UploadFile = File(...),
    db: DBConnection = Depends(get_db),
    RAG: RAGModel = Depends(get_RAG)
    ):

    try:
        start_time = time.time()
        # Parse the JSON string into the Pydantic model
        interval = FileLength.model_validate_json(data)

        # Read PDF Files.
        content = await file.read()
        pdf_file = io.BytesIO(content)
        reader = PdfReader(pdf_file)

        # IF start page = final page and zero must extract all.
        # Example reqeust body 
        # { "start_page":0, "final_page":0 }
        if ((interval.start_page == interval.final_page) and 
            (interval.start_page == 0 and interval.final_page == 0)):
            
            # Make to extract all data.
            interval.start_page = 1 # first_page = 1 in PDF
            interval.final_page = len(reader.pages)

            # logging info.
            logging.info(f"Receive start_page = 0 and final_page = 0 >> Set inteval to extract all")
        
        # IF start_page != 0 and final_page > max_page or == 0
        # Example request body 
        # { "start_page":1, "final_page":0 ( < start_page ) }
        elif ((interval.start_page != 0) and
              ((interval.final_page > len(reader.pages)) or 
               (interval.final_page == 0))):
            
            # Set final page to Extract all page.
            interval.final_page = len(reader.pages)

            # logging info.
            logging.info(f"Set final_page = {len(reader.pages)} >> Set to extract all from start_page")

        # IF start_page == 0 and final_page != 0
        # Example request body
        # { "start_page":0, "final_page":10 }
        # Must extract from first_page to final_page
        elif (interval.start_page == 0 and interval.final_page != 0):
            
            # Set start_page = 1
            interval.start_page = 1

            # logging info.
            logging.info("Set start_page = 1")


        # start_page must less than final_page and final_page must max to pages.
        # Example request body 
        # { "start_page":2, "final_page":1 }
        elif (interval.start_page > interval.final_page):

            # Raise an Exception HTTP ERROR 422.
            raise HTTPException(422, f"The interval that given {interval} is not good.")
        
        # Specific target page to extract
        target_interval = [ target for target in range(
                    interval.start_page-1, # First page is zero. 
                    interval.final_page
                    )] 
        logging.info(f'Extract {target_interval}')

        # Prepare Temp Varr.
        contents = ""
        metadatas = []

        # Extract contents from each page
        for page in reader.pages:
            if page.page_number in target_interval:
                contents += page.extract_text()
                metadatas.append({
                    "page":page.page_number,
                    "source": file.filename,
                                })
        
        # Upload PDF to Vector Database
        documents = await RAG.aload_from_API(
            contents=contents,
            metadatas=metadatas
            )
        time_usage = time.time() - start_time

        # Insert to Document Table.
        db.insert(
            DocumentTable, 
            embedding_model = EMBEDDING_MODEL,
            document_name = file.filename,
            time_usage=time_usage,
            pages=len(target_interval)
            )

        return JSONResponse(content={
            "Filename": file.filename,
            "Metadata": metadatas,
            "time_usage": time_usage,
            })

    except json.JSONDecodeError:
        raise HTTPException(400, "Invalid JSON format")
    except Exception as e:
        raise HTTPException(400, f"Data validation error: {str(e)}")
    
# Use to remove Document inside vector database.
@router_document.delete("/documents")
async def removeDocs():
    pass

# Get Document from database.
@router_document.get('/documents')
async def getDocs():
    pass