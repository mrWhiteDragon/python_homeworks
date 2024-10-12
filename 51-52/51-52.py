import random

class Player:
    def __init__(self, name):
        self.name = name
        self.victories = 0

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play_round(self):
        players = [player1, player2]
        results = []
        for player in players:
            sum = 0
            for throw in range(2):
                dice = random.randint(1, 6)
                sum += dice
            print(f'{player.name} выбросил {sum}')
            results.append(sum)

        if results[0] > results[1]:
            print(f'Победил {players[0].name}\n')
            players[0].victories += 1
        elif results[0] < results[1]:
            print(f'Победил {players[1].name}\n')
            players[1].victories += 1
        else:
            print('Ничья\n')

    def get_statistics(self):
        print(f'{player1.name} - Побед {player1.victories}')
        print(f'{player2.name} - Побед {player2.victories}')


player1 = Player('Alice')
player2 = Player('Вов')

game = Game(player1, player2)

game.play_round()
game.play_round()

game.get_statistics()



