from NekoGram import Menu, Neko, NekoRouter
from aiogram import types
import const


ROUTER: NekoRouter = NekoRouter()


@ROUTER.formatter()
async def start(data: Menu, user: types.User, _: Neko):
    if user.id not in const.ADMIN_IDS:
        data.text = data.extras['no_permission']
    await data.build()
