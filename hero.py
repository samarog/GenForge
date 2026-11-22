# hero class

class Hero:

    def __init__(self, name: str, hp: int, attack: int, defense: int):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def testing(self):
        return f"Hello, i'm {self.name} and i have {self.hp} HP left."

    def __str__(self):
        return f"the instance attributes of Hero are: {self.name} for name, {self.hp} for HP left, {self.attack} for attack and {self.defense} for defense."

    def take_damage(self, damage: int):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
# hero end

character1 = Hero("Odin", 100, 50, 50)

character1.take_damage(30)
character1.take_damage(30)
character1.take_damage(30)
character1.take_damage(30)

print(character1.hp)