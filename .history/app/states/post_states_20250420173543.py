from aiogram.fsm.state import State, StatesGroup

class GetPostState(StatesGroup):
    waiting_for_post_id = State()

class AddPostState(StatesGroup):
    waiwaiting_for_post_idting = State()
    waiting_for_post_id = State ()