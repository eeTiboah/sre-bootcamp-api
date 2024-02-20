
from fastapi import APIRouter, status, Depends
from src.models.student import StudentResponse, StudentInput
from src.db.database import get_db
from src.db.models import Student
from sqlalchemy.orm import Session
from src.core.exceptions import NotFoundError

router = APIRouter(tags=["Student"], prefix="/students")

@router.get("/", status_code=status.HTTP_200_OK, response_model=StudentResponse)
def get_students(db: Session= Depends(get_db)):
    students = db.query(Student).all()
    return students

@router.get("/{student_id}", status_code=status.HTTP_200_OK, response_model=StudentResponse)
def get_students(student_id: int, db: Session= Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise NotFoundError(status_code=status.HTTP_404_NOT_FOUND, error_msg=f"Student with id {student_id} not found")
    
    return student

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=StudentResponse)
def create_student(student: StudentInput, db: Session= Depends(get_db)):
    new_student = Student(**student.model_dump())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student

@router.patch("/{student_id}", status_code=status.HTTP_200_OK, response_model=StudentResponse)
def update_student(student_id: str, student_input: StudentInput, db: Session=Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id)
    student_in_db = student.first()
    if not student_in_db:
        raise NotFoundError(status_code=status.HTTP_404_NOT_FOUND, error_msg=f"Student with id {student_id} not found")
    updated_dict = student_input.dict()
    new_update = {k: v for k, v in updated_dict.items() if v is not None}

    student.update(new_update)
    db.commit()

    student_data = student.first()

    return student_data


    
@router.delete("/{student_id}")
def delete_student(student_id: str, db: Session=Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id)
    student_in_db = student.first()
    if not student_in_db:
        raise NotFoundError(status_code=status.HTTP_404_NOT_FOUND, error_msg=f"Student with id {student_id} not found")
    student.delete()
    db.commit()

    return None

