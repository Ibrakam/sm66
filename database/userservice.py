from database import get_db
from database.models import User
from api.user_api.schemas import UserSchema

"""
Функция для создания пользовтеля
Удаления польователя
"""


def create_user_db(user: UserSchema):
    db = next(get_db())
    user_data = user.model_dump()
    new_user = User(**user_data)
    db.add(new_user)
    db.commit()
    return new_user.id


def get_all_or_exact_user_db(uid=0):
    db = next(get_db())
    if uid:
        exact_user = db.query(User).filter_by(id=uid).first()
        if exact_user:
            return exact_user
        return False
    return db.query(User).all()


def update_user_db(uid, change_info, new_info):
    db = next(get_db())
    user_to_update = db.query(User).filter_by(id=uid).first()
    if user_to_update:
        if change_info == "name":
            user_to_update.name = new_info
        elif change_info == "surname":
            user_to_update.surname = new_info
        else:
            return False
        db.commit()
        return True
    return False
