# webhook_server.py
import logging
import asyncio
from aiohttp import web
from app.database.init_db import init_db
from app.handlers import register_handlers
from app.config import WEBHOOK_URL
from app.commands.commands import set_commands
from app.bot import bot,dp
from app.database.init_db import init_models


# Регистрируем роутеры
register_handlers(dp)

async def on_startup(app):
    print("🟢 Стартуем сервер...")
    await init_db()
    await set_commands(bot)
    await bot.set_webhook(WEBHOOK_URL)
    info = await bot.get_webhook_info()
    print(f"🔗 Текущий webhook в Telegram: {info.url}")
    logging.info("🚀 Webhook установлен")

async def on_shutdown(app):
    await bot.delete_webhook()
    logging.info("🛑 Webhook удалён")

async def handle_webhook(request):
    update = await request.json()
    await dp.feed_webhook_update(bot=bot, update=update)
    return web.Response()

app = web.Application()
app.on_startup.append(on_startup)
app.on_shutdown.append(on_shutdown)

app.router.add_post("/webhook", handle_webhook)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    web.run_app(app, port=8000)