from pydantic import BaseModel, Field

class StudentResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str

    class Config:
        orm_mode = True


class StudentInput(BaseModel):
    first_name: str = Field(...)
    last_name: str = Field(...)
    email: str = Field(...)

class StudentUpdate(BaseModel):
    first_name: str
    last_name: str
    email: str