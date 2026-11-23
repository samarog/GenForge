# Class: Hero

from character import Character

class Hero(Character):

    def get_role(self) -> str:
        return "Hero"

    def __str__(self):
        return f"the instance attributes of Hero are: {self.name} for name, {self.hp} for HP left, {self.attack} for attack and {self.defense} for defense."

# run

hero = Hero("Odin", 100, 50, 50, 50)
monster = Hero("Loki", 100, 55, 45, 60)
turn = 0
while hero.is_alive and monster.is_alive:
    hero.attack_target(monster)
    monster.attack_target(hero)
    turn += 1

if hero.is_alive:
    print(f"{hero.name} wins in {turn} turns.")
else:
    print(f"{monster.name} wins in {turn} turns.")

# end run