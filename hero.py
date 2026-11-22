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
        if damage < 0:
            raise ValueError("Damage cannot be negative.") # stop negative values from raising hp
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0

    @property
    def is_alive(self) -> bool:
        return self.hp > 0
# hero end

# run

hero = Hero("Odin", 100, 50, 50)

hero.take_damage(40)

print(f"Still breathing! You have {hero.hp} HP" if hero.is_alive else f"You dead...")

hero.take_damage(70)

print(f"Still breathing! You have {hero.hp} HP" if hero.is_alive else f"You dead...")

# end run