from app.bot import bot,dp
from app.handlers import register_handlers



async def main():
    register_handlers(db)