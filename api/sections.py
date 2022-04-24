from fastapi import APIRouter

router = APIRouter()


@router.get("/sections")
async def get_sections():
    return {"sections": []}


@router.post("/sections")
async def create_section():
    return {"created_section": "Section"}


@router.get("/sections/{section_id}")
async def get_section_by_id(section_id: int):
    return {"section_id": section_id}


@router.patch("/sections/{section_id}")
async def update_section_by_id(section_id: int):
    return {"section_id": section_id}


@router.delete("/sections/{section_id}")
async def delete_section_by_id(section_id: int):
    return {"section_id": section_id}
