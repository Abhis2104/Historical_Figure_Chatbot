"""config.py – Environment configuration for Groq API."""

import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
GROQ_MODEL = os.getenv("GROQ_MODEL", "qwen/qwen3.8-27b")


def validate_api_key() -> tuple[bool, str]:
    """Return (is_valid, error_message)."""
    if not GROQ_API_KEY:
        return False, "GROQ_API_KEY is missing. Add it to your .env file."
    if len(GROQ_API_KEY) < 10:
        return False, "GROQ_API_KEY looks invalid. Please check your .env file."
    return True, ""
