class BaseClimber:
    def __init__(self, name: str, strength: float):
        if not name.strip():
            raise ValueError("Climber name cannot be null or empty!")
        if strength <= 0:
            raise ValueError("A climber cannot have negative strength or strength equal to 0!")
        self.name = name
        self.strength = strength
        self.conquered_peaks = []
        self.is_prepared = True

    def can_climb(self):
        raise NotImplementedError("Subclasses must implement this method")

    def climb(self, peak):
        raise NotImplementedError("Subclasses must implement this method")

    def rest(self):
        self.strength += 15

    def __str__(self):
        return f"{type(self).__name__}: /// Climber name: {self.name} * Left strength: {self.strength:.1f} * Conquered peaks: {', '.join(self.conquered_peaks)} ///"
