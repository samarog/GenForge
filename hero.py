# hero class

class Hero:

    def __init__(self, name: str, hp: int, attack: int, defense: int):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def testing(self):
        return f"Hello, i'm {self.name} and i have {self.hp} HP left."

# hero end

character1 = Hero("Odin", 100, 50, 50)
print(character1.testing())
print(character1.name)
print(character1.hp)