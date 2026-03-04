from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application configuration.

    Values can come from:
    1. Environment variables
    2. Defaults defined here
    """

    # Application Environment
    ENV: str = Field(default="dev")

    # Database connection string
    # Default = SQLite for local development
    DATABASE_URL: str = Field(default="sqlite:///./expense_tracker.db")

    class Config:
        # Optional .env file support
        env_file = ".env"
        case_sensitive = True


# Create a single global settings instance
settings = Settings()
