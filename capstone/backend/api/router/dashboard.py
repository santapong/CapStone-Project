from fastapi import APIRouter

router_dashboard = APIRouter(prefix='/dashboard')

tags = ['Dashboard']

@router_dashboard.get('/data', tags=tags)
def history():
    return {"msg":"test"}