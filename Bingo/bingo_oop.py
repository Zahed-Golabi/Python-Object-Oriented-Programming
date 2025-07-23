import random


class BingoGame:

    player_list = []

    def __init__(self):
        self.name = input("Please enter your name: ")
        self.__rand_num = random.randint(0, 10)
        self.__guess_left = 4
        self.__won_state = False
        BingoGame.player_list.append(self)

    def check_answer(self):
        answer = int(input(f"\n{self.name} Please enter your guess: "))
        if answer > self.__rand_num:
            print("Choose smaller number ")
        elif answer < self.__rand_num:
            print("Choose bigger number ")
        elif answer == self.__rand_num:
            print("Bingo!")
            self.__won_state = True
        self.__guess_left -= 1
        print(f"{self.__guess_left} guesses left!")

    def has_guess_left(self):
        return self.__guess_left > 0
    
    def has_won(self):
        return self.__won_state
    
    @classmethod
    def game_has_winner(cls):
        if any(player.has_won() for player in cls.player_list):
            return True
        return False
    

class GameController:
    def __init__(self):
        while True:
            for player in BingoGame.player_list:
                if (player.has_guess_left()) and (not player.has_won()):
                    player.check_answer()
                else:
                    BingoGame.player_list.clear()
                    break
            if BingoGame.game_has_winner():
                BingoGame.player_list.clear()
                break
            
if __name__ == "__main__":
    while True:
        order = input("What do you want to do?\norder: ")
        if order == "add":
            BingoGame()
        elif order == "start":
            GameController()
        elif order == "exit":
            break
        