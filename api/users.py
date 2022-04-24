from fastapi import APIRouter

router = APIRouter()


@router.get("/users")
async def get_users():
    return {"users": []}


@router.post("/users")
async def create_user():
    return {"created_user": {}}


@router.get("/users/{user_id}")
async def get_user_by_id(user_id: int):
    return {}


@router.patch("/users/{user_id}")
async def update_user_by_id(user_id: int):
    return {}


@router.patch("/users/{user_id}")
async def delete_user_by_id(user_id: int):
    return {}
