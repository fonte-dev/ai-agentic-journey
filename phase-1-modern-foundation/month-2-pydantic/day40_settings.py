# Day 40 - Settings Management
# Task: Use pydantic-settings to read .env files.
# Learning goal: Security: Handling API keys safely.
# Date: Feb 2026
# Status: DONE ✅

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, SecretStr
from typing import Optional, Literal


class Settings(BaseSettings):
    """Configuration for the entire MERITUM project."""

    # Required API keys (will be loaded from .env)
    openai_api_key: SecretStr = Field(
        ..., description="OpenAI API key - never commit this!"
    )
    anthropic_api_key: Optional[SecretStr] = None

    # Other settings
    ollama_model: str = "qwen2.5:7b"
    environment: Literal["development", "production"] = "development"
    database_url: Optional[str] = None  # Optional for now

    # Tell pydantic-settings to read the .env file
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # ignore extra variables in .env
    )


if __name__ == "__main__":
    settings = Settings()  # type: ignore # This automatically loads .env

    print(" Settings loaded successfully!")
    print(f"Environment     : {settings.environment}")
    print(f"Ollama model    : {settings.ollama_model}")
    print(
        f"OpenAI key      : {settings.openai_api_key.get_secret_value()[:10]}... (hidden)"
    )
