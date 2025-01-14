import logging
from fastapi import APIRouter

logging.getLogger(__name__)

router_dynamic = APIRouter(prefix='/dynamic')

# Create API on the fly.
@router_dynamic.put('/')
async def test(prefix, tags):
    router = APIRouter(prefix=prefix)

    @router.get('/', tags=[tags])
    def test():
        return {"msg":"hello"}
    
    return {"msg":f"{prefix} has created."}
