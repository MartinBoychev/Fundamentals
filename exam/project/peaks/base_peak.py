from abc import ABC, abstractmethod


class BasePeak(ABC):
    def __init__(self, name: str, elevation: int):
        self.name = name
        self.elevation = elevation
        if len(name) < 2:
            raise ValueError("Peak name cannot be less than 2 symbols!")
        if elevation < 1500:
            raise ValueError("Peak elevation cannot be below 1500m.")

    @abstractmethod
    def get_recommended_gear(self):
        pass

    @abstractmethod
    def calculate_difficulty_level(self):
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Peak name cannot be less than 2 symbols!")
        self._name = value

    @property
    def elevation(self):
        return self._elevation

    @elevation.setter
    def elevation(self, value):
        if value < 1500:
            raise ValueError("Peak elevation cannot be below 1500m.")
        self._elevation = value