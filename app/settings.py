from pydantic import Field, field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = Field(default="NLPServer", description="The name of project")

    SEED: int = Field(default=42, description="The seed to use for the GPT model")

    MONGO_URI: str = Field(default=..., description="The URI of the MongoDB database")
    MONGO_DB_NAME: str = Field(default=..., description="The name of the MongoDB database")

    LOGGING_LEVEL: str = Field(default="INFO", description="The logging level")

    ENVIRONMENT: str = Field(default="local", description="The environment to run server")

    @staticmethod
    @field_validator('MONGO_URI', 'MONGO_DB_NAME')
    def check_not_empty(value, field):
        if not value.strip():
            raise ValueError(f"{field.name} must not be empty")
        return value

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
