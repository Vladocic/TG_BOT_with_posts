from app.bot import bot,dp
from app.handlers import     register_handlers(db)



async def main():
    register_handlers(db)