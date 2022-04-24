from fastapi import APIRouter

router = APIRouter()


@router.get("/courses")
async def get_courses():
    return {"courses": []}


@router.post("/courses")
async def create_course():
    return {"created_course": {}}


@router.get("/courses/{course_id}")
async def get_course_by_id(course_id: int):
    return {"course_id": course_id}


@router.patch("/courses/{course_id}")
async def update_course_by_id(course_id: int):
    return {"course_id": course_id}


@router.delete("/courses/{course_id}")
async def delete_course_by_id(course_id: int):
    return {"course_id": course_id}
