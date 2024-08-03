from project.base_climber import BaseClimber


class ArcticClimber(BaseClimber):
    def __init__(self, name: str):
        super().__init__(name, 200)

    def can_climb(self):
        return self.strength >= 100

    def climb(self, peak):
        if not self.can_climb():
            raise ValueError("Climber does not have enough strength to climb.")
        difficulty_multiplier = 2 if peak.difficulty_level == "Extreme" else 1.5
        self.strength -= 20 * difficulty_multiplier
        self.conquered_peaks.append(peak.name)
