from pydantic_settings import BaseSettings, SettingsConfigDict
import logging

logger = logging.getLogger(__name__)

class Settings(BaseSettings):
    model: str 
    model_host: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")