from enum import IntEnum

characters = ['?','🀇','🀈','🀉','🀊','🀋','🀌','🀍','🀎','🀏',
              '?','🀙','🀚','🀛','🀜','🀝','🀞','🀟','🀠','🀡',
              '?','🀐','🀑','🀒','🀓','🀔','🀕','🀖','🀗','🀘',
              '🀀','🀁','🀂','🀃','🀆','🀅','🀄']

dora_table = [6 , 2, 3, 4, 5, 6, 7, 8, 9, 1,
              16,12,13,14,15,16,17,18,19,11,
              26,22,23,24,25,26,27,28,29,21,
              31,32,33,30,35,36,34]

class Tile(IntEnum):
    """
    Manzu (Characters in English)
    """
    #M0 = 0  # red 5
    M1 = 1
    M2 = 2
    M3 = 3
    M4 = 4
    M5 = 5
    M6 = 6
    M7 = 7
    M8 = 8
    M9 = 9

    """
    Pinzu (Circles in English)
    """
    #P0 = 10 # red 5
    P1 = 11
    P2 = 12
    P3 = 13
    P4 = 14
    P5 = 15
    P6 = 16
    P7 = 17
    P8 = 18
    P9 = 19

    """
    Souzu (Bamboo in English)
    """
    #S0 = 20  # red 5
    S1  = 21
    S2  = 22
    S3  = 23
    S4  = 24
    S5  = 25
    S6  = 26
    S7  = 27
    S8  = 28
    S9  = 29

    """
    Winds
    """
    TON = 30  # 東 East
    NAN = 31  # 南 South
    SHA = 32  # 西 West
    PEI = 33  # 北 North

    """
    Dragons
    """
    HAK = 34  # 白 White Dragon
    HAT = 35  # 発 Green Dragon
    CHN = 36  # 中 Red Dragon

    def is_manzu(self):
        return 1 <= self.value < 10

    def is_pinzu(self):
        return 11 <= self.value <= 19

    def is_souzu(self):
        return 21 <= self.value <= 29

    def is_wind(self):
        return 30 <= self.value <= 33

    def is_dragon(self):
        return 34 <= self.value <= 36

    def is_suit(self):
        return self.value <= 29

    def is_honor(self):
        return not self.is_suit()

    def is_terminal(self):
        return (self.value % 10) == 1 or (self.value % 10) == 9

    def is_terminal_or_honor(self):
        return self.is_honor() or self.is_terminal()

    def get_char(self):
        return characters[self.value]

def dora_index_by_display_index(index):
    return dora_table[index]
