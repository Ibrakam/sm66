from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Указываем тип бд(sqlite3, postgres)
SQL_DATABASE = "sqlite:///sm.db"

# Создаем бд
engine = create_engine(SQL_DATABASE)

# Создаем сессию что бы хранить данные
SessionLocal = sessionmaker(bind=engine)

# Создаем полноценную базу(django=models.Models)
Base = declarative_base()


# Подключение к бд
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
