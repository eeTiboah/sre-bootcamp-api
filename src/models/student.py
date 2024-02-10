from pydantic import BaseModel, Field

class StudentResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str


class StudentInput(BaseModel):
    first_name: str = Field(...)
    last_name: str = Field(...)
    email: str = Field(...)