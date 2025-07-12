from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openrouter_deepseek_key: str
    openroter_mistral_7b_key: str

    class Config:
        env_file = ".env" 

settings = Settings()