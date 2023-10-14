from abc import ABC, abstractmethod
from typing import Optional, List
from bs4 import BeautifulSoup
import httpx


class BaseScrapper(ABC):
    _BASE_URL: Optional[str] = None
    _URL: str
    NAME: str
    _verify_ssl: bool = True

    @classmethod
    async def perform_request(cls, query: str, is_json: bool, headers=None):
        async with httpx.AsyncClient(verify=True) as client:
            r = await client.get(cls._URL.format(query=query), headers=headers)
            if r.status_code != 200:
                return
        return r.json() if is_json else BeautifulSoup(r.text, features='html.parser')

    @classmethod
    def concat_url(cls, relative_path: str):
        if not relative_path.startswith('/'):
            relative_path = f'/{relative_path}'
        return f'{cls._BASE_URL}{relative_path}'

    @abstractmethod
    async def search(self, query: str) -> Optional[List[str]]:
        ...
