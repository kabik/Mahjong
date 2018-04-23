import random
import copy

from src.core import tile
from src.core import player
from src.core import hand

full_wall = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,11,11,11,11,12,12,12,12,13,13,13,13,14,14,14,14,15,15,15,15,16,16,16,16,17,17,17,17,18,18,18,18,19,19,19,19,21,21,21,21,22,22,22,22,23,23,23,23,24,24,24,24,25,25,25,25,26,26,26,26,27,27,27,27,28,28,28,28,29,29,29,29,30,30,30,30,31,31,31,31,32,32,32,32,33,33,33,33,34,34,34,34,35,35,35,35,36,36,36,36]

initial_point = 25000
max_game = 8
winds = ['TON', 'NAN', 'SHA', 'PEI']

class Board():
    def __init__(self):
        self.players = []
        for i in range(0,4):
            self.players.append(player.Player(i))
            self.players[i].set_point(initial_point)
        self.dealer_num = random.randint(0,3)
        self.turn = self.dealer_num
        self.wall = []
        self.dead_wall = []
        self.dora_display = []
        self.dora = []
        self.rivers = [ [],[],[],[] ]

    def game_init(self):
        # player turn
        self.turn = self.dealer_num

        # wall
        self.wall = copy.deepcopy( full_wall )

        # dead wall
        for i in range(0,14):
            index = random.randint(0,len(self.wall)-1)
            n = self.wall.pop(index)
            self.dead_wall.append(n)

        # dora
        index = random.randint(0, len(self.dead_wall)-1)
        n = self.dead_wall.pop(index)
        self.dora_display.append(n)
        self.dora.append( tile.dora_index_by_display_index(n) )

        # player's hands
        for p in self.players:
            for i in range(0,13):
                index = random.randint(0,len(self.wall)-1)
                n = self.wall.pop(index)
                p.draw(n)

    def rest_num_wall(self):
        return len(self.wall)

    def get_next_turn(self):
        return (self.turn + 1) % 4
