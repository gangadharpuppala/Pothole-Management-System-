from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry
from datetime import datetime
from .database import Base
import enum

class RoleEnum(str, enum.Enum):
    public = "public"
    staff = "staff"
    admin = "admin"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(Enum(RoleEnum), default="public")

class PotholeReport(Base):
    __tablename__ = "pothole_reports"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    location = Column(Geometry(geometry_type='POINT', srid=4326))
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User")

