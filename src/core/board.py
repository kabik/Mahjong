import random
import copy

from src.core import tile
from src.core import player
from src.core import hand

full_wall = [
    1,1,1,1,      # 1 man
    2,2,2,2,      # 2 man
    3,3,3,3,      # 3 man
    4,4,4,4,      # 4 man
    5,5,5,5,      # 5 man
    6,6,6,6,      # 6 man
    7,7,7,7,      # 7 man
    8,8,8,8,      # 8 man
    9,9,9,9,      # 9 man
    11,11,11,11,  # 1 pin
    12,12,12,12,  # 2 pin
    13,13,13,13,  # 3 pin
    14,14,14,14,  # 4 pin
    15,15,15,15,  # 5 pin
    16,16,16,16,  # 6 pin
    17,17,17,17,  # 7 pin
    18,18,18,18,  # 8 pin
    19,19,19,19,  # 9 pin
    21,21,21,21,  # 1 sou
    22,22,22,22,  # 2 sou
    23,23,23,23,  # 3 sou
    24,24,24,24,  # 4 sou
    25,25,25,25,  # 5 sou
    26,26,26,26,  # 6 sou
    27,27,27,27,  # 7 sou
    28,28,28,28,  # 8 sou
    29,29,29,29,  # 9 sou
    30,30,30,30,  # 東 East
    31,31,31,31,  # 南 South
    32,32,32,32,  # 西 West
    33,33,33,33,  # 北 North
    34,34,34,34,  # 白 White Dragon
    35,35,35,35,  # 発 Green Dragon
    36,36,36,36   # 中 Red Dragon
]

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
