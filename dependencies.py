from .database import SessionLocal


# Зависимость для базы данных (если используется)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
