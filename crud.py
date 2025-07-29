from sqlalchemy.orm import Session
from . import models, schemas
from .core.security import get_password_hash

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_all_reports(db: Session):
    return db.query(models.PotholeReport).all()

def get_user_reports(db: Session, user_id: int):
    return db.query(models.PotholeReport).filter(models.PotholeReport.user_id == user_id).all()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_pw = get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_pothole_report(db: Session, report: schemas.PotholeReportCreate, user_id: int):
    location = f'POINT({report.longitude} {report.latitude})'
    db_report = models.PotholeReport(description=report.description, location=location, user_id=user_id)
    db.add(db_report)
    db.commit()
    db.refresh(db_report)
    return db_report

