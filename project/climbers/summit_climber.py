from project.base_climber import BaseClimber


class SummitClimber(BaseClimber):
    def __init__(self, name: str):
        super().__init__(name, 150)

    def can_climb(self):
        return self.strength >= 75

    def climb(self, peak):
        if not self.can_climb():
            raise ValueError("Climber does not have enough strength to climb.")
        difficulty_multiplier = 1.3 if peak.difficulty_level == "Advanced" else 2.5
        self.strength -= 30 * difficulty_multiplier
        self.conquered_peaks.append(peak.name)
