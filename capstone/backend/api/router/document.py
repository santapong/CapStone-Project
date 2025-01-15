import io

from typing import Annotated
from pypdf import PdfReader

from fastapi import APIRouter, UploadFile, File

tags = ["Document"]
router_document = APIRouter(prefix='/document')


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

    return {"filename": file.filename, "content": text}
