from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Language Translator API"
    DEBUG: bool = False
    
    class Config:
        env_file = ".env"

settings = Settings()