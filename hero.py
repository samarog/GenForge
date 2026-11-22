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
        return f"the instnace attributes of Hero are: {self.name} for name, {self.hp} for HP left, {self.attack} for attack and {self.defense} for defense."

# hero end

character1 = Hero("Odin", 100, 50, 50)
print(character1.testing())
print(character1.name)
print(character1.hp)

print(character1) # - if no __str__, it only prints object's memory address