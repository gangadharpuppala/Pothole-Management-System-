from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, crud, database, models
from ..deps import get_current_user

router = APIRouter(prefix="/potholes", tags=["Potholes"])

@router.post("/", response_model=schemas.PotholeReportOut)
def create_report(
    report: schemas.PotholeReportCreate,
    db: Session = Depends(database.SessionLocal),
    current_user: models.User = Depends(get_current_user)
):
    return crud.create_pothole_report(db, report, current_user.id)

@router.get("/", response_model=List[schemas.PotholeReportOut])
def list_reports(
    db: Session = Depends(database.SessionLocal),
    current_user: models.User = Depends(get_current_user)
):
    if current_user.role not in ["staff", "admin"]:
        raise HTTPException(status_code=403, detail="Not authorized to view all reports")
    return crud.get_all_reports(db)

@router.get("/me", response_model=List[schemas.PotholeReportOut])
def list_my_reports(
    db: Session = Depends(database.SessionLocal),
    current_user: models.User = Depends(get_current_user)
):
    return crud.get_user_reports(db, user_id=current_user.id)

