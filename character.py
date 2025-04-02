import random

class Character:
    def __init__(self, combat_strength=1, health_points=10):
        self._combat_strength = combat_strength
        self._health_points = health_points

    @property
    def combat_strength(self):
        return self._combat_strength

    @combat_strength.setter
    def combat_strength(self, value):
        if 1 <= value <= 6:
            self._combat_strength = value

    @property
    def health_points(self):
        return self._health_points

    @health_points.setter
    def health_points(self, value):
        self._health_points = max(0, value)

    def is_alive(self):
        return self._health_points > 0

    def __del__(self):
        print(f"{self.__class__.__name__} object destroyed.")
