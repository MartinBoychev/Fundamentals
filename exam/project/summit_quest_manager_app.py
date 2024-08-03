from typing import List
from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    def __init__(self):
        self.climbers = []
        self.peaks = []

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type == "ArcticClimber":
            climber = ArcticClimber(climber_name)
        elif climber_type == "SummitClimber":
            climber = SummitClimber(climber_name)
        else:
            return f"{climber_type} doesn't exist in our register."

        if any(c.name == climber_name for c in self.climbers):
            return f"{climber_name} has been already registered."

        self.climbers.append(climber)
        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type == "ArcticPeak":
            peak = ArcticPeak(peak_name, peak_elevation)
        elif peak_type == "SummitPeak":
            peak = SummitPeak(peak_name, peak_elevation)
        else:
            return f"{peak_type} is an unknown type of peak."

        self.peaks.append(peak)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):
        climber = next((c for c in self.climbers if c.name == climber_name), None)
        if climber is None:
            return f"{climber_name} is not registered yet."

        peak = next((p for p in self.peaks if p.name == peak_name), None)
        if peak is None:
            return f"Peak {peak_name} is not part of the wish list."

        recommended_gear = peak.get_recommended_gear()
        missing_gear = sorted(set(recommended_gear) - set(gear))
        if not missing_gear:
            return f"{climber_name} is prepared to climb {peak_name}."
        else:
            climber.is_prepared = False
            return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(missing_gear)}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        climber = next((c for c in self.climbers if c.name == climber_name), None)
        if climber is None:
            return f"Climber {climber_name} is not registered yet."

        peak = next(filter(lambda p: p.name == peak_name, self.peaks), None)

        if peak is None:
            return f"Peak {peak_name} is not part of the wish list."

        if climber.can_climb() and climber.is_prepared:
            climber.climb(peak)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.calculate_difficulty_level()}."
        elif not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."
        else:
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    @property
    def get_statistics(self):
        # Collect all climbed peaks
        climbed_peaks = []
        for climber in self.climbers:
            climbed_peaks.extend(climber.conquered_peaks)

        # Remove duplicates and sort alphabetically
        climbed_peaks = sorted(set(climbed_peaks))

        # Count the total number of climbed peaks
        total_climbed_peaks = len(climbed_peaks)

        # Collect climbers' information who successfully conquered peaks
        climbers_info = {}
        for climber in self.climbers:
            if climber.conquered_peaks:
                climbers_info[climber.name] = climber

        # Sort climbers based on the number of conquered peaks in descending order
        sorted_climbers = sorted(climbers_info.items(), key=lambda x: (len(x[1].conquered_peaks), x[0]), reverse=True)

        # Generate statistics output
        output = [f"Total climbed peaks: {total_climbed_peaks}", "**Climber's statistics:**"]
        for climber_name, climber in sorted_climbers:
            conquered_peaks = sorted(climber.conquered_peaks)
            output.append(f"{climber}")
        return '\n'.join(output)


# Example usage:
climbing_app = SummitQuestManagerApp()
print(climbing_app.register_climber("ArcticClimber", "Alice"))
print(climbing_app.register_climber("SummitClimber", "Bob"))
print(climbing_app.register_climber("ExtremeClimber",
                                    "Dave"))  # Should return message that the climber type doesn't exist
print(climbing_app.register_climber("ArcticClimber", "Charlie"))
print(climbing_app.register_climber("ArcticClimber",
                                    "Alice"))  # Should return message that the climber is already registered
print(climbing_app.register_climber("SummitClimber", "Eve"))
print(climbing_app.register_climber("SummitClimber", "Frank"))
print(climbing_app.peak_wish_list("ArcticPeak", "MountEverest", 4000))
print(climbing_app.peak_wish_list("SummitPeak", "K2", 3000))
print(climbing_app.peak_wish_list("ArcticPeak", "Denali", 2500))
print(climbing_app.peak_wish_list("UnchartedPeak", "MysteryMountain", 2000))
print(climbing_app.check_gear("Alice", "MountEverest", ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]))
print(climbing_app.check_gear("Bob", "K2", ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]))
print(climbing_app.check_gear("Charlie", "Denali", ["Ice axe", "Crampons"]))
print(climbing_app.perform_climbing("Alice", "MountEverest"))
print(climbing_app.perform_climbing("Bob", "K2"))
print(climbing_app.perform_climbing("Kelly", "Denali"))
print(climbing_app.perform_climbing("Alice", "K2"))
print(climbing_app.perform_climbing("Alice", "MysteryMountain"))
print(climbing_app.perform_climbing("Eve", "MountEverest"))
print(climbing_app.perform_climbing("Charlie", "MountEverest"))
print(climbing_app.perform_climbing("Frank", "K2"))
print(climbing_app.perform_climbing("Frank", "Denali"))
print(climbing_app.perform_climbing("Frank", "MountEverest"))
print(climbing_app.get_statistics)