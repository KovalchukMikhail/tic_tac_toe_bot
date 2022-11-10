# модуль содержит обработчики команд

from aiogram import types
from aiogram.types import ReplyKeyboardRemove, InputFile, InputMediaPhoto
from loader import dp
from loader import bot
from keyboards import start_game, another_game, navigation_btm_callback, start_game_inline_keyboard, game_inline_keyboard, finish_game, choosing_option, difficulty_level
from Classes import Player, game_list


@dp.message_handler(text=['Еще одна игра'])
@dp.message_handler(commands='start')
async def answer_start_command(message: types.Message):
    current_game = Player(message.from_user.id, message.message_id)
    game_list.append(current_game)
    await message.answer(text=f'Выберите кем будете играть "X" или "O". "X" ходит первым!', reply_markup=choosing_option(current_game))
    await message.answer(text=f'Для выбора еще одной игры нажмите кнопку под строкой ввода', reply_markup=another_game)


@dp.callback_query_handler(navigation_btm_callback.filter(id_btm=['X', 'O']))
async def answer_chose_game_command(call: types.CallbackQuery):
    id_msg = int(call.data.split(':')[2])
    id_btm = call.data.split(':')[1]
    id_player = call.from_user.id
    index = 0
    for i in range(len(game_list)):
        if (game_list[i].id_player == id_player) and (game_list[i].id_message == id_msg):
            index = i
    game_list[index].save_sign(id_btm)
    await bot.edit_message_text(text='Выберите уровень сложности', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=difficulty_level(current_game=game_list[index]))

@dp.callback_query_handler(navigation_btm_callback.filter(id_btm=['easy', 'normal', 'hard']))
async def answer_chose_level_command(call: types.CallbackQuery):
    id_msg = int(call.data.split(':')[2])
    id_btm = call.data.split(':')[1]
    id_player = call.from_user.id
    index = 0
    for i in range(len(game_list)):
        if (game_list[i].id_player == id_player) and (game_list[i].id_message == id_msg):
            index = i
    game_list[index].level = id_btm
    await bot.edit_message_text(text='.......Ваш ход.......', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=start_game_inline_keyboard(current_game=game_list[index]))


@dp.callback_query_handler(navigation_btm_callback.filter(id_btm=['0', '1', '2', '3', '4', '5', '6', '7', '8'], sign='0'))
async def game(call: types.CallbackQuery):
    id_msg = int(call.data.split(':')[2])
    id_btm = int(call.data.split(':')[1])
    id_player = call.from_user.id
    index = 0
    print(f'зашел {call}')
    for i in range(len(game_list)):
        if (game_list[i].id_player == id_player) and (game_list[i].id_message == id_msg):
            index = i
    await bot.edit_message_text(text='.......Ваш ход.......', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=game_inline_keyboard(current_game=game_list[index], id_btm=id_btm))
    if game_list[index].finish_game == 1:
        await bot.edit_message_text(text='....Вы победили!....', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=finish_game(current_game=game_list[index]))
    elif game_list[index].finish_game == 2:
        await bot.edit_message_text(text='.....Победил bot.....', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=finish_game(current_game=game_list[index]))
    elif game_list[index].finish_game == 3:
        await bot.edit_message_text(text='........Ничья........', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=finish_game(current_game=game_list[index]))


@dp.callback_query_handler(navigation_btm_callback.filter(id_btm='restart'))
async def restart_answer(call: types.CallbackQuery):
    id_msg = int(call.data.split(':')[2])
    id_player = call.from_user.id
    index = 0
    print(f'зашел {call}')
    for i in range(len(game_list)):
        if (game_list[i].id_player == id_player) and (game_list[i].id_message == id_msg):
            index = i
    game_list[index].new_game()
    await bot.edit_message_text(text=f'Выберите кем будете играть "X" или "O". "X" ходит первым!', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=choosing_option(game_list[index]))

