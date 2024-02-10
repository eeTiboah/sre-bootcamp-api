
from fastapi import APIRouter, status, Depends
from src.models.student import StudentResponse
from src.db.database import get_db
from src.db.models import Student
from sqlalchemy.orm import Session

route = APIRouter(prefix="/student")

route.get("/", status_code=status.HTTP_200_OK, response_model=StudentResponse)
def get_students(db: Session= Depends(get_db)):
    students = db.query(Student)