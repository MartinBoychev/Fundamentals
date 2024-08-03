from project.climbers.base_climber import BaseClimber


class SummitClimber(BaseClimber):
    def __init__(self, name: str):
        super().__init__(name, 150)

    def can_climb(self):
        return self.strength >= 75

    def climb(self, peak):
        if self.can_climb():
            factor = 1.3 if peak.calculate_difficulty_level() == "Advanced" else 2.5
            reduction = 30 * factor
            self.strength -= reduction
            self.conquered_peaks.append(peak.name)
