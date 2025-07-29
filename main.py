from fastapi import FastAPI
from .database import Base, engine
from .routers import users, potholes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Pothole Reporting System")

app.include_router(users.router, prefix="/api")


