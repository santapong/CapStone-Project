from fastapi import APIRouter

router_dashboard = APIRouter(prefix='/dashboard')

tags = ['Dashboard']

@router_dashboard.get('/history', tags=tags)
def history():
    pass