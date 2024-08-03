from project.climbers.base_climber import BaseClimber


class ArcticClimber(BaseClimber):
    def __init__(self, name: str):
        super().__init__(name, 200)

    def can_climb(self):
        return self.strength >= 100

    def climb(self, peak):
        if self.can_climb():
            factor = 2 if peak.calculate_difficulty_level() == "Extreme" else 1.5
            reduction = 20 * factor
            self.strength -= reduction
            self.conquered_peaks.append(peak.name)
        self.conquered_peaks.append(peak.name)
