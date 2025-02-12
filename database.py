from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine


# Настройка базы данных (если используется для других целей)
DATABASE_URL = "sqlite:///./telegram_summary.db"
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}, echo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Создание всех таблиц (теперь только необходимые)
Base.metadata.create_all(bind=engine)
