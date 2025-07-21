from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # App settings
    PROJECT_NAME: str = "SnapGrub"
    API_V1_STR: str = "/api/v1"
    BACKEND_CORS_ORIGINS: list[str] = ["*"]
    BACKEND_PORT: int = 8000
    DEBUG: bool = False
    
    # Database settings
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: int = 5432
    
    # Redis settings
    REDIS_HOST: str
    REDIS_PORT: int
    
    # Security settings
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Timezone
    TIMEZONE: str = "UTC"
    
    class Config:
        case_sensitive = True
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()