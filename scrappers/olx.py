from typing import Optional, List

from .base import BaseScrapper


class Olx(BaseScrapper):
    _BASE_URL = 'https://www.olx.pl'
    _URL = 'https://www.olx.pl/oferty/q-{query}/'
    NAME = 'OLX'

    @classmethod
    async def search(cls, query: str) -> Optional[List[str]]:
        r = await cls.perform_request(query=query.replace(' ', '-'), is_json=False, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/94.0.4606.61 Safari/537.36'
        })
        if r is None:
            return

        offers = r.findAll('a', attrs={'class': 'css-rc5s2u'})
        if not offers:
            return []

        results = [cls.concat_url(item['href']) for item in offers]
        if results and results[0].endswith('?reason=extended_search_no_results_last_resort'):
            return []
        return results
