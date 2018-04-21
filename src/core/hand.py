import copy

from src.core import tile

empty_tile_set = [0,0,0,0,0,0,0,0,0,0,
                  0,0,0,0,0,0,0,0,0,0,
                  0,0,0,0,0,0,0,0,0,0,
                  0,0,0,0,0,0,0]

class Hand():
    def __init__(self, id):
        self.id = id
        self.main_hand = copy.deepcopy( empty_tile_set )
        self.open_sets = []
        self.claimed_tile = []
        self.claimed_player = []
        self.winning_tile_list = []

        for i in range(0,4):
            self.open_sets.append( copy.deepcopy(empty_tile_set) )

    def can_win(self, index):
        pass
        """
        h = copy.deepcopy(self.main_hand)
        h[index] += 1
        return calc_shanten(h) == -1
        """

    def can_pong(self, index):
        return self.main_hand[index] >= 2

    def can_chow(self, index):
        if tile.Tile(index).is_honor():
            return False
        elif not tile.Tile(index).is_terminal():
            return (self.main_hand[index-2] > 0 and self.main_hand[index-1] > 0) or \
                   (self.main_hand[index-1] > 0 and self.main_hand[index+1] > 0) or \
                   (self.main_hand[index+1] > 0 and self.main_hand[index+2] > 0)
        elif index % 10 == 1:
            return  self.main_hand[index+1] > 0 and self.main_hand[index+2] > 0
        else:
            return  self.main_hand[index-2] > 0 and self.main_hand[index-1] > 0

    def can_daiminkan(self, index):
        return self.main_hand[index] == 3

    def can_kakan(self, index):
        for set in self.open_sets:
            if set[index] == 3:
                return True
        return False

    # this function is called before new tile is added to hand
    def can_ankan(self, index):
        return self.main_hand[index] == 3

    # pong or chow or shouminkan
    def claim(self, by_main_hand, tile_index, claimed_player):
        length = len(self.claimed_player)

        # delete from main_hand
        for i in by_main_hand:
            self.main_hand[i] -= 1

        # add to open_sets
        self.open_sets.append(copy.deepcopy( empty_tile_set ))
        for i in by_main_hand:
            self.open_sets[length][i] += 1

        # register claimed_tile and clamed_player
        self.claimed_tile.append(tile_index)
        self.claimed_player.append(claimed_player)

    def kakan(self, index):
        for s in self.open_sets:
            if s[index] == 3:
                s[index] += 1

    def ankan(self, index):
        self.claim([index,index,index], index, self.id)

    def add(self, index):
        self.main_hand[index] += 1

    def discard(self, index):
        self.main_hand[index] -= 1

    def isOpen(self):
        for p in self.claimed_player:
            if p != self.id:
                return True
        return False


"""
len(l) = 37
"""
def calc_shanten_seven(l):
    seven = 6
    for n in l:
        if n >= 2:
            seven -= 1
    return seven


"""
len(l) = 37
"""
def calc_shanten_kokushi(l):
    indexes = [1,9,11,19,21,29,30,31,32,33,34,35,36]
    kokushi = 13
    pair_counted = False
    for i in indexes:
        n = l[i]
        if n == 0:
            continue
        elif n == 1:
            kokushi -= 1
        elif pair_counted:
            kokushi -= 1
        else:
            kokushi -= 2
            pair_counted = True
    return kokushi

"""
len(l) = 37
"""
def calc_shanten_normal(l):
    normal = 8
    head_indexes = []
    for i in range(0, 37):
        if l[i] >= 2:
            head_indexes.append(i)
    for i in head_indexes:
        h = copy.deepcopy(l)
        h[i] -= 2

        # manzu
        man_m, man_t = calc_mentsu_tatsu(h[0:10])
        # pinzu
        pin_m, pin_t = calc_mentsu_tatsu(h[10:20])
        # souzu
        sou_m, sou_t = calc_mentsu_tatsu(h[20:30])
        # honor
        hon_m, hon_t = calc_mentsu_tatsu_honor(h[30:37])

        mentsu = man_m + pin_m + sou_m + hon_m
        tatsu = min(man_t + pin_t + sou_t + hon_t, 4 - mentsu)

        s = 8 - mentsu * 2 - tatsu - 1
        if s < normal:
            normal = s

    h = copy.deepcopy(l)
    man_m, man_t = calc_mentsu_tatsu(h[0:10])
    # pinzu
    pin_m, pin_t = calc_mentsu_tatsu(h[10:20])
    # souzu
    sou_m, sou_t = calc_mentsu_tatsu(h[20:30])
    # honor
    hon_m, hon_t = calc_mentsu_tatsu_honor(h[30:37])

    mentsu = man_m + pin_m + sou_m + hon_m
    tatsu = min(man_t + pin_t + sou_t + hon_t, 4 - mentsu)

    s = 8 - mentsu * 2 - tatsu
    if s < normal:
        normal = s

    return normal

"""
len(l) = 37
"""
def calc_shanten(l):
    seven   = calc_shanten_seven(l)
    kokushi = calc_shanten_kokushi(l)
    normal  = calc_shanten_normal(l)
    return min(seven, kokushi, normal)

"""
len(l) = 10
"""
def calc_mentsu_tatsu(l):
    m_candidate_indexes = []
    t_candidate_indexes = []
    mentsu = 0
    tatsu = 0
    shanten = 8
    # kotsu
    for i in range(0,10):
        if l[i] >= 3:
            m_candidate_indexes.append([i,i,i])
    # shuntsu
    for i in range(0,8):
        if l[i] > 0 and l[i+1] > 0 and l[i+2] > 0:
            m_candidate_indexes.append([i,i+1,i+2])
    # pair
    for i in range(0,10):
        if l[i] == 2:
            t_candidate_indexes.append([i,i])
    # tatsu
    for i in range(0,9):
        if l[i] > 0 and l[i+1] > 0:
            t_candidate_indexes.append([i,i+1])

    for indexes in m_candidate_indexes:
        l2 = copy.deepcopy(l)
        for i in indexes:
            l2[i] -= 1
        m, t = calc_mentsu_tatsu(l2)
        m += 1
        t = min(t, 4 - m)
        s = 8 - m * 2 - t
        if s < shanten:
            shanten = s
            mentsu = m
            tatsu = t
    for indexes in t_candidate_indexes:
        l2 = copy.deepcopy(l)
        for i in indexes:
            l2[i] -= 1
        m, t = calc_mentsu_tatsu(l2)
        t += 1
        t = min(t, 4 - m)
        s = 8 - m * 2 - t
        if s < shanten:
            shanten = s
            mentsu = m
            tatsu = t

    return mentsu, tatsu

"""
len(l) = 7
"""
def calc_mentsu_tatsu_honor(l):
    mentsu = 0
    tatsu = 0
    for n in l:
        if n >= 3:
            mentsu += 1
        elif n == 2:
            tatsu += 1
    return mentsu, tatsu
