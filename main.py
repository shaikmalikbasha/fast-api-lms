from typing import Optional

from black import List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI(
    title="FastAPI LMS",
    description="Learning Management System for Stdents & Courses",
    version="0.0.1",
    contact={
        "name": "Shaik Malik Basha",
        "email": "shaikmalikbasha@example.com",
        "instagram": "INST",
        "linked": "LiniedIn",
    },
    license_info={"name": "MIT"},
)

users = []


class UserSchema(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


@app.get("/users", response_model=List[UserSchema])
async def get_users():
    return users


@app.post("/users")
async def create_users(user: UserSchema):
    users.append(user)
    return user


@app.get("/users/{user_id}")
async def get_user_by_id(
    user_id: int = Path(..., description="Id for the USER", lt=3, gt=0),
    q: str = Query(None, max_length=5),
):
    return {"user": users[user_id], "query": q}
