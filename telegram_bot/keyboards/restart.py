from aiogram import types

def generate_restart_kb(common_ans: list[str]):
    restart = []
    for ans in common_ans:
        restart.append([
            types.InlineKeyboardButton(text=ans, 
                                       callback_data="generate_" + ans)
            ])
    restart.append([
        types.InlineKeyboardButton(text="Вернуться в меню ⤴️",
                                   callback_data="return")
    ])
    
    restart_kb = types.InlineKeyboardMarkup(
        inline_keyboard=restart)
    
    return restart_kb


