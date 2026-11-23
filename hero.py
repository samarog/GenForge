# hero class

class Hero:

    def __init__(self, name: str, hp: int, attack: int, defense: int):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def __str__(self):
        return f"the instance attributes of Hero are: {self.name} for name, {self.hp} for HP left, {self.attack} for attack and {self.defense} for defense."

    def take_damage(self, damage: int) -> None:
        if damage < 0:
            raise ValueError("Damage cannot be negative.") # stop negative values from raising hp
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0

    def attack_target(self, target: Hero) -> None:
        damage: int = max(1, self.attack - target.defense)
        target.take_damage(damage)

    @property
    def is_alive(self) -> bool:
        return self.hp > 0
# hero end

# run

hero = Hero("Odin", 100, 50, 50)
monster = Hero("Loki", 100, 30, 15)

hero.attack_target(monster)
print(f"Hero has {hero.hp} HP left.")
print(f"Monster has {monster.hp} HP left.")

hero.attack_target(monster)
print(f"Hero has {hero.hp} HP left.")
print(f"Monster has {monster.hp} HP left.")

hero.attack_target(monster)
print(f"Hero has {hero.hp} HP left.")
print(f"Monster has {monster.hp} HP left.")

# end run