# модуль содержит объект используемый для работы с inline клавиатурами

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inlinekeyboard.callback_data import navigation_btm_callback

from Classes import Player

from brain import game_computer, check_game


def start_game_inline_keyboard(current_game: Player):
    inline_keyboard = InlineKeyboardMarkup()
    btm_restart = InlineKeyboardButton(text='Начать заново', callback_data=navigation_btm_callback.new(id_btm='restart', id_msg=current_game.id_message, sign='1'))

    btm_zero = InlineKeyboardButton(text=' ', callback_data=navigation_btm_callback.new(id_btm='0', id_msg=current_game.id_message, sign='0'))
    btm_one = InlineKeyboardButton(text=' ', callback_data=navigation_btm_callback.new(id_btm='1', id_msg=current_game.id_message, sign='0'))
    btm_two = InlineKeyboardButton(text=' ', callback_data=navigation_btm_callback.new(id_btm='2', id_msg=current_game.id_message, sign='0'))
    btm_three = InlineKeyboardButton(text=' ', callback_data=navigation_btm_callback.new(id_btm='3', id_msg=current_game.id_message, sign='0'))
    if current_game.sign == 'O':
        btm_four = InlineKeyboardButton(text='X', callback_data=navigation_btm_callback.new(id_btm='4', id_msg=current_game.id_message, sign='1'))
        current_game.current_game_computer.append(4)
    else:
        btm_four = InlineKeyboardButton(text=' ', callback_data=navigation_btm_callback.new(id_btm='4', id_msg=current_game.id_message, sign='0'))
    btm_five = InlineKeyboardButton(text=' ', callback_data=navigation_btm_callback.new(id_btm='5', id_msg=current_game.id_message, sign='0'))
    btm_six = InlineKeyboardButton(text=' ', callback_data=navigation_btm_callback.new(id_btm='6', id_msg=current_game.id_message, sign='0'))
    btm_seven = InlineKeyboardButton(text=' ', callback_data=navigation_btm_callback.new(id_btm='7', id_msg=current_game.id_message, sign='0'))
    btm_eight = InlineKeyboardButton(text=' ', callback_data=navigation_btm_callback.new(id_btm='8', id_msg=current_game.id_message, sign='0'))
    current_game.list_btm = [btm_zero, btm_one, btm_two, btm_three, btm_four, btm_five, btm_six, btm_seven, btm_eight]

    inline_keyboard.row(current_game.list_btm[0], current_game.list_btm[1], current_game.list_btm[2])
    inline_keyboard.row(current_game.list_btm[3], current_game.list_btm[4], current_game.list_btm[5])
    inline_keyboard.row(current_game.list_btm[6], current_game.list_btm[7], current_game.list_btm[8])
    inline_keyboard.row(btm_restart)
    return inline_keyboard

def game_inline_keyboard(current_game: Player, id_btm: int = 0):
    inline_keyboard = InlineKeyboardMarkup()
    btm_restart = InlineKeyboardButton(text='Начать заново', callback_data=navigation_btm_callback.new(id_btm='restart', id_msg=current_game.id_message, sign='1'))
    for i in range(len(current_game.list_btm)):
        if i == id_btm:
            current_game.list_btm[i] = InlineKeyboardButton(text=current_game.sign, callback_data=navigation_btm_callback.new(id_btm=str(id_btm), id_msg=current_game.id_message, sign='1'))
            current_game.current_game_player.append(i)

    if check_game(current_game.current_game_player):
        current_game.finish_game = 1
    elif len(current_game.current_game_player) + len(current_game.current_game_computer) == 9:
        current_game.finish_game = 3
    else:
        move = game_computer(current_game.current_game_player, current_game.current_game_computer, current_game.level)
        current_game.current_game_computer.append(move)
        if check_game(current_game.current_game_computer):
            current_game.finish_game = 2
        elif len(current_game.current_game_player) + len(current_game.current_game_computer) == 9:
            current_game.finish_game = 3
        for i in range(len(current_game.list_btm)):
            if i == move:
                current_game.list_btm[i] = InlineKeyboardButton(text=current_game.sign_computer,
                                                                callback_data=navigation_btm_callback.new(
                                                                    id_btm=str(id_btm), id_msg=current_game.id_message,
                                                                    sign='1'))

    inline_keyboard.row(current_game.list_btm[0], current_game.list_btm[1], current_game.list_btm[2])
    inline_keyboard.row(current_game.list_btm[3], current_game.list_btm[4], current_game.list_btm[5])
    inline_keyboard.row(current_game.list_btm[6], current_game.list_btm[7], current_game.list_btm[8])
    inline_keyboard.row(btm_restart)
    return inline_keyboard


def finish_game(current_game: Player):
    inline_keyboard = InlineKeyboardMarkup()
    btm_restart = InlineKeyboardButton(text='Начать заново', callback_data=navigation_btm_callback.new(id_btm='restart', id_msg=current_game.id_message, sign='1'))
    for i in range(len(current_game.list_btm)):
        id_btm = str(current_game.list_btm[i].callback_data.split(':')[1])
        sign = current_game.list_btm[i].callback_data.split(':')[3]
        if sign == '0':
            print(sign)
            current_game.list_btm[i] = InlineKeyboardButton(text=' ', callback_data=navigation_btm_callback.new(id_btm=id_btm, id_msg=current_game.id_message, sign='1'))

    inline_keyboard.row(current_game.list_btm[0], current_game.list_btm[1], current_game.list_btm[2])
    inline_keyboard.row(current_game.list_btm[3], current_game.list_btm[4], current_game.list_btm[5])
    inline_keyboard.row(current_game.list_btm[6], current_game.list_btm[7], current_game.list_btm[8])
    inline_keyboard.row(btm_restart)
    return inline_keyboard

def choosing_option(current_game: Player):
    inline_keyboard = InlineKeyboardMarkup()
    btm_first = InlineKeyboardButton(text='X', callback_data=navigation_btm_callback.new(id_btm='X', id_msg=current_game.id_message, sign='0'))
    btm_second = InlineKeyboardButton(text='O', callback_data=navigation_btm_callback.new(id_btm='O', id_msg=current_game.id_message, sign='0'))
    inline_keyboard.row(btm_first, btm_second)
    return inline_keyboard


def difficulty_level(current_game: Player):
    inline_keyboard = InlineKeyboardMarkup()
    btm_first = InlineKeyboardButton(text='Легко', callback_data=navigation_btm_callback.new(id_btm='easy', id_msg=current_game.id_message, sign='0'))
    btm_second = InlineKeyboardButton(text='Нормально', callback_data=navigation_btm_callback.new(id_btm='normal', id_msg=current_game.id_message, sign='0'))
    btm_third = InlineKeyboardButton(text='Сложно', callback_data=navigation_btm_callback.new(id_btm='hard', id_msg=current_game.id_message, sign='0'))
    inline_keyboard.row(btm_first, btm_second)
    inline_keyboard.row(btm_third)
    return inline_keyboard