# Class: Hero

from character import Character

class Hero(Character):

    def get_role(self) -> str:
        return "Hero"

    def __str__(self):
        return f"the instance attributes of Hero are: {self.name} for name, {self.hp} for HP left, {self.attack} for attack and {self.defense} for defense."

# run

hero = Hero("Odin", 100, 50, 50, 50)

print(hero.get_role())
print(hero.name)
print(hero.hp)

# end run