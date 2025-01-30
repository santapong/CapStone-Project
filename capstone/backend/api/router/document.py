import io

from typing import List
from pypdf import PdfReader


from fastapi.responses import JSONResponse
from fastapi import (
    APIRouter, 
    UploadFile, 
    File
    )

from capstone.backend.llms import RAGmodel

# Setting RAG model
llms = RAGmodel().setEmbeddings().setModel()

tags = ["Document"]
router_document = APIRouter(prefix='/document')


# Uploadfile PDF from API.
@router_document.post("/uploadfile", tags=tags)
async def uploadFile(file: UploadFile = File(...)):

    # Read PDF Files.
    contents = await file.read()
    pdf_file = io.BytesIO(contents)
    reader = PdfReader(pdf_file)
    text = ""

    # Extract text from each page
    for page in reader.pages:
        text += page.extract_text()

    return JSONResponse(content={"filename": file.filename, "content": text})


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