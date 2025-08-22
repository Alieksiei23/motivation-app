from pydantic import BaseModel, EmailStr

class AddUser(BaseModel):
    username: str
    password: str
    email: EmailStr


class GetUser(AddUser):
    id: int


class AddLetter(BaseModel):
    letter: str


class Admin(BaseModel):
    username: str
    password: str