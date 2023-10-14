from aiogram import exceptions as aiogram_exc
from NekoGram import Menu
import asyncio

from const import SEARCH_LIST, ADMIN_IDS, RUN_INTERVAL, NEKO, STORAGE
from loggers import main_logger
import scrappers


async def send_data(data: Menu, user: int):
    while True:
        try:
            await NEKO.bot.send_message(
                chat_id=user,
                text=data.text,
                reply_markup=data.markup,
                parse_mode=data.parse_mode
            )
            break
        except aiogram_exc.RetryAfter as e:
            await asyncio.sleep(e.timeout)
        except aiogram_exc.TelegramAPIError:
            break
        await asyncio.sleep(.2)


async def notify_error(scrapper: str):
    main_logger.error(f'Error in {scrapper}')
    for user in ADMIN_IDS:
        data = await NEKO.build_menu(name='notification_failed', obj=None, user_id=user, auto_build=False)
        await data.build(text_format={'scrapper': scrapper})
        await send_data(data=data, user=user)


async def notify_found(item_name: str, store_name: str, url: str):
    for user in ADMIN_IDS:
        data = await NEKO.build_menu(name='notification_found', obj=None, user_id=user, auto_build=False)
        await data.build(text_format={'item': item_name, 'store': store_name}, markup_format={'url': url})
        await send_data(data=data, user=user)


async def scrape_urls():
    while True:
        for item in SEARCH_LIST:
            main_logger.info(f'Looking up {item}')
            for scrapper in [s for s in dir(scrappers) if s[0].isupper()]:
                scrapper_class = getattr(scrappers, scrapper)
                r = await getattr(scrapper_class, 'search')(item)
                main_logger.info(f'Results: {r}')
                if r is None:
                    await notify_error(scrapper=scrapper)
                for result in r:
                    if not await STORAGE.check('SELECT url FROM search_cache WHERE url = ?', result):
                        await STORAGE.apply('INSERT INTO search_cache (url) VALUES (?)', result)
                        await notify_found(item_name=item, store_name=getattr(scrapper_class, 'NAME'), url=result)
            await asyncio.sleep(RUN_INTERVAL)


async def startup(_):
    await NEKO.storage.acquire_pool()

    # Import database structure
    with open('db.sql', 'r') as f:
        for statement in f.read().split('--'):
            await NEKO.storage.apply(statement)

    asyncio.get_event_loop().create_task(scrape_urls())


async def shutdown(_):
    await NEKO.storage.close_pool()


if __name__ == '__main__':
    NEKO.start_polling(on_startup=startup, on_shutdown=shutdown)
