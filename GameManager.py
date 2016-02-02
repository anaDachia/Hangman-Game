from api.api_handler import Api_handler
from game_logic.Game import Game
__author__ = 'ana'


if __name__ == "__main__":

    while (True):
        game_data = Api_handler. start_call()
        new_game = Game(game_data['token'], game_data['state'], game_data['remaining_guesses'])
        lost = False
        while(not lost):
            guess = new_game.next_guess()
            print("guess :",  guess)
            res = Api_handler.followup_call(new_game.token,guess)
            print(res)
            new_game.update(res)
            if new_game.if_lost():
                lost = True

