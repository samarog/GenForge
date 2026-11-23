# Abstract Class: Character

from abc import ABC, abstractmethod
class Character(ABC):

# constructor
    def __init__(self, name: str, hp: int, attack: int, defense: int, speed: int):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
# end constructor

# behaviors
    def take_damage(self, damage: int) -> None:
        if damage < 0:
            raise ValueError("Damage cannot be negative.") # stop negative values from raising hp
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0

    def attack_target(self, target: Character) -> None:
        if not self.is_alive or not target.is_alive:
            return

        damage: int = max(1, self.attack - target.defense)
        target.take_damage(damage)

    @property
    def is_alive(self) -> bool:
        return self.hp > 0
# end behaviors

# interfaces
    @abstractmethod
    def get_role(self) -> str:
        pass
# end interfaces

