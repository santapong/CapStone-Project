import io
import json
from typing import List
from pypdf import PdfReader

from fastapi.responses import JSONResponse
from fastapi import (
    File,
    Form,
    Depends,
    APIRouter,
    UploadFile,
    HTTPException
    )

from capstone.backend.llms import RAGModel
from capstone.backend.api.models import FileLength
from capstone.backend.database import (
    get_db, 
    DBConnection,
    DocumentTable,
    )

# Setting RAG model
RAG = RAGModel()

tags = ["Document"]
router_document = APIRouter(prefix='/document')

# Uploadfile PDF from API.
@router_document.post("/uploadfile", tags=tags)
async def uploadFile(
    data: str = Form(...), 
    file: UploadFile = File(...),
    db: DBConnection = Depends(get_db)
    ):

    try:
        # Parse the JSON string into the Pydantic model
        interval = FileLength.model_validate_json(data)

        # Read PDF Files.
        content = await file.read()
        pdf_file = io.BytesIO(content)
        reader = PdfReader(pdf_file)

        # Make sure the interval is good.
        if (interval.start_page < 1 or 
            interval.final_page > len(reader.pages) or 
            interval.start_page > interval.final_page):

            # Raise an Exception 422
            raise HTTPException(422, f"The interval that given {interval} is not good.")
        
        # Specific target page to extract
        target_interval = [ target for target in range(
                                                interval.start_page-1, # First page is zero. 
                                                interval.final_page
                                                )] 
        print(target_interval)
        # Prepare Temp Varr
        contents = ""
        metadatas = []

        # Extract contents from each page
        for page in reader.pages:
            if page.page_number in target_interval:
                contents += page.extract_text()
                metadatas.append({"source": file.filename,
                                "Page":page.page_number,
                                })
        
        # Insert to Document Table.
        db.insert(DocumentTable, document_name= file.filename, pages=len(target_interval))
        # # Upload PDF to Vector Database
        # documents = await RAG.aload_from_API(
        #     contents=contents,
        #     metadatas=metadatas
        #     )

        return JSONResponse(content={
            "filename": file.filename,
            "Metadata":metadatas}
            )

    except json.JSONDecodeError:
        raise HTTPException(400, "Invalid JSON format")
    except Exception as e:
        raise HTTPException(400, f"Data validation error: {str(e)}")

# TODO: Make Can upload multiple document beware error.
@router_document.post("/upload_multiple", tags=tags)
async def uploadFileMultiple(files: List[UploadFile] = File(...)):
    file_contents = {}

    for file in files:
        file_data = await file.read()  # Read file asynchronously
        pdf_reader = PdfReader(io.BytesIO(file_data))  # Convert bytes to PDF reader
        
        # Extract text from all pages
        extracted_text = "\n".join(page.extract_text() or "" for page in pdf_reader.pages)
        
        file_contents[file.filename] = extracted_text  # Map filename to extracted text

    return JSONResponse(content={"files": file_contents})  # Return JSON response