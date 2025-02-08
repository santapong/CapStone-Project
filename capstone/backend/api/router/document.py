import io
from typing import List
from pypdf import PdfReader

from fastapi.responses import JSONResponse
from fastapi import (
    File,
    Depends,
    APIRouter,
    UploadFile,
    BackgroundTasks
    )

from capstone.backend.llms import RAGModel
from capstone.backend.database.connection import (
    get_db, 
    DBConnection
    )

# Setting RAG model
RAG = RAGModel()

tags = ["Document"]
router_document = APIRouter(prefix='/document')

# Uploadfile PDF from API.
@router_document.post("/uploadfile", tags=tags)
async def uploadFile(file: UploadFile = File(...), db: DBConnection = Depends(get_db)):

    # Read PDF Files.
    content = await file.read()
    pdf_file = io.BytesIO(content)
    reader = PdfReader(pdf_file)
    
    contents = ""
    metadatas = []

    # Extract contents from each page
    for page in reader.pages:
        contents += page.extract_text()
        metadatas.append({"source":file.filename,
                          "Page":page.page_number,
                        })

    # Upload PDF to Vector Database
    documents = await RAG.aload_from_API(
        contents=contents,
        metadatas=metadatas
        )

    return JSONResponse(content={"filename": file.filename, 
                                 "example content": documents[0].page_content ,
                                 "Metadata":metadatas})


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