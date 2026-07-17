from dataclasses import dataclass

from dhp.config.settings import settings as legacy_settings


@dataclass
class DHPConfig:
    prestashop_url: str = legacy_settings.PRESTASHOP_URL
    prestashop_api_key: str = legacy_settings.PRESTASHOP_API_KEY


settings = DHPConfig()


