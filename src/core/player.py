from src.core import tile
from src.core import hand

class Player():
    def __init__(self, id):
        self.id = id
        self.hand = hand.Hand(id)
        self.point = 0

    def set_point(self, point):
        self.point = point

    def draw(self, index):
        self.hand.add(index)

    def discard(self, index):
        self.hand.discard(index)
