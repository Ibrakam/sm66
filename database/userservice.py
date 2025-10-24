from database import get_db
from database.models import User



"""
Функция для создания пользовтеля
Удаления польователя
"""


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

