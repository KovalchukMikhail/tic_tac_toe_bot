# модуль содержит класс характеризующий текущее состояние игры

game_list = []

class Player:
    id_player: str
    id_message: str
    current_game_player: list
    current_game_computer: list
    list_btm: list
    sign: str
    sign_computer: str
    finish_game: int
    level: str

    def __init__(self, id_player: str, id_message: str):
        self.id_player = id_player
        self.id_message = id_message
        self.current_game_player = []
        self.current_game_computer = []
        self.list_btm = []
        self.finish_game = 0
        self.level = 'easy'

    def new_game(self):
        self.current_game_player.clear()
        self.current_game_computer.clear()
        self.list_btm.clear()
        self.finish_game = 0

    def save_sign(self, sign: str):
        self.sign = sign
        self.sign_computer = 'X' if self.sign == 'O' else 'O'


