from fastapi import APIRouter

tags = ["Document"]
router_document = APIRouter(prefix='/document')

@router_document.post("/document", tags=tags)
def Upload():
    pass
