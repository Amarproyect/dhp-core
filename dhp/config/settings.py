from pathlib import Path
import os

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[2]

load_dotenv(BASE_DIR / ".env")


class Settings:
    PRESTASHOP_URL = os.getenv("PRESTASHOP_URL")
    PRESTASHOP_API_KEY = os.getenv("PRESTASHOP_API_KEY")


settings = Settings()
