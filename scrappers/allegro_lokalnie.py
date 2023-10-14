from typing import Optional, List

from .base import BaseScrapper


class AllegroLokalnie(BaseScrapper):
    _BASE_URL = 'https://allegrolokalnie.pl'
    _URL = 'https://allegrolokalnie.pl/oferty/q/{query}'
    NAME = 'Allegro'

    @classmethod
    async def search(cls, query: str) -> Optional[List[str]]:
        r = await cls.perform_request(query=query, is_json=False)
        if r is None:
            return

        offers = r.findAll('a', attrs={'class': 'mlc-card mlc-itembox'})
        if not offers:
            return []

        return [cls.concat_url(item['href']) for item in offers]
