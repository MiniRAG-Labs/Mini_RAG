from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str

    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHUNK_SIZE: int

    class Config:
        env_file = ".env"

def get_settings():
    return Settings()
# from typing import Optional, List
# # لو بتستخدم pydantic v2
# from pydantic_settings import BaseSettings, SettingsConfigDict
# # لو عندك v1 فقط، شوف الملاحظة تحت

# class Settings(BaseSettings):
#     APP_NAME: str
#     APP_VERSION: str
#     OPENAI_API_KEY: Optional[str] = None

#     FILE_ALLOWED_TYPES: List[str]
#     FILE_MAX_SIZE: int
#     FILE_DEFAULT_CHUNK_SIZE: int

#     FILES_DIR: str = "src/assets/files"

#     # لو pydantic-settings (v2)
#     model_config = SettingsConfigDict(env_file=".env", extra="ignore")

#     # لو بتستخدم pydantic v1 بدلاً من v2، استبدل السطر اللي فوق بــ:
#     # class Config:
#     #     env_file = ".env"
#     #     extra = "ignore"

# def get_settings():
#     return Settings()
