from fastapi import APIRouter
from database.userservice import (create_user_db, update_user_db,
                                  get_all_or_exact_user_db)
from api.user_api.schemas import UserSchema, UserRead

user_router = APIRouter(prefix="/user", tags=["User API"])


@user_router.post("/create_user", response_model=UserRead)
async def create_user_api(user: UserSchema):
    result = create_user_db(user)
    return {"status": 1, "message": result}


@user_router.get("/get_all_or_exact_user", response_model=UserRead)
async def get_users_api(uid: int = 0):
    result = get_all_or_exact_user_db(uid)
    if result:
        return {"status": 1, "message": result}
    return {"status": 0, "message": "Error"}


@user_router.put("/update_user", response_model=UserRead)
async def update_user_api(uid: int, change_info: str, new_info: str):
    result = update_user_db(uid, change_info, new_info)
    if result:
        return {"status": 1, "message": result}
    return {"status": 0, "message": "Error"}

