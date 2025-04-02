import random
from character import Character

class Monster(Character):
    def __init__(self, combat_strength=None, health_points=None):
        if combat_strength is None:
            combat_strength = random.randint(1, 6) * 10
        if health_points is None:
            health_points = random.randint(1, 6) * 20
        super().__init__(combat_strength, health_points)
        self.magic_power = ""

    def __del__(self):
        print("The Monster is being destroyed.")
        super().__del__()

    def monster_attacks(self):
        attack_damage = random.randint(1, 15)
        print(f"Monster attacks: {attack_damage} damage to hero.")
        return attack_damage
