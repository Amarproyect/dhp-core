from abc import ABC


class Provider(ABC):

    def __init__(self, url, api_key):
        self.url = url.rstrip("/")
        self.api_key = api_key