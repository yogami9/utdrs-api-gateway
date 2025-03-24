from fastapi import APIRouter, Depends
from core.models.user import User
from utils.security import get_current_active_user

router = APIRouter()

@router.get("/")
async def get_detection_status(current_user: User = Depends(get_current_active_user)):
    '''Get detection status (placeholder).'''
    return {"message": "Detection endpoint placeholder"}
