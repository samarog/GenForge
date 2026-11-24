# Simulator Class: Battle

from hero import Hero
from monster import Monster

class Battle:
    def __init__(self, hero: Hero, monster: Monster, turn: int):
        self.hero = hero
        self.monster = monster
        self.turn = turn