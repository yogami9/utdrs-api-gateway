from fastapi import APIRouter, Depends
from core.models.user import User
from utils.security import get_current_active_user

router = APIRouter()

@router.get("/")
async def get_simulation_status(current_user: User = Depends(get_current_active_user)):
    '''Get simulation status (placeholder).'''
    return {"message": "Simulation endpoint placeholder"}

@router.post("/start")
async def start_simulation(current_user: User = Depends(get_current_active_user)):
    '''Start simulation (placeholder).'''
    return {"message": "Simulation started (placeholder)"}

@router.post("/stop")
async def stop_simulation(current_user: User = Depends(get_current_active_user)):
    '''Stop simulation (placeholder).'''
    return {"message": "Simulation stopped (placeholder)"}
