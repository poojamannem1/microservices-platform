import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    # 🔹 App
    APP_NAME: str = os.getenv("APP_NAME", "Microservice")

    # 🔹 Database
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://admin:admin123@postgres:5432/microservices_db"
    )

    # 🔹 JWT
    SECRET_KEY: str = os.getenv("SECRET_KEY", "mysecretkey")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")

    # 🔹 Redis
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://redis:6379")


settings = Settings()