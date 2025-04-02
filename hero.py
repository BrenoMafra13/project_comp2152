import random
from character import Character

class Hero(Character):
    def __init__(self, combat_strength=None, health_points=None):
        if combat_strength is None:
            combat_strength = random.randint(1, 6) * 10
        if health_points is None:
            health_points = random.randint(1, 6) * 20
        super().__init__(combat_strength, health_points)
        self.inventory = []
        self.weapon = None
        self.shield = 0
        self.lifesteal = 0

    def __del__(self):
        print("The Hero is being destroyed.")
        super().__del__()

    def hero_attacks(self):
        attack_damage = random.randint(1, 10)
        print(f"Hero attacks: {attack_damage} damage to monster.")
        return attack_damage
