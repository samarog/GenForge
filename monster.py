# Class: Monster

from character import Character

class Monster(Character):

    def get_role(self) -> str:
        return "Monster"

    def __str__(self):
        return f"the instance attributes of Monster are: {self.name} for name, {self.hp} for HP left, {self.attack} for attack and {self.defense} for defense."

# run

gojira = Monster("Gojira", 100, 50, 50, 50)

gojira.take_damage(30)

print(gojira.name)
print(gojira.hp)