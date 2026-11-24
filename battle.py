# Simulator Class: Battle

from hero import Hero
from monster import Monster

class Battle:
    def __init__(self, hero: Hero, monster: Monster):
        self.hero = hero
        self.monster = monster
        self.turn = 0

# run

odin = Hero("Odin", 100, 50, 30, 20)
gojira = Monster("Gojira", 100, 40, 20, 15)

battle = Battle(odin, gojira)

odin.take_damage(40)

print(odin.hp)
print(battle.hero.hp)

# end run