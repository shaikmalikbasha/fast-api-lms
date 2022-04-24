from fastapi import FastAPI

from api import courses, sections, users

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

app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router)
