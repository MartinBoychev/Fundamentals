from typing import List
from project.arctic_climber import ArcticClimber
from project.summit_climber import SummitClimber
from project.arctic_peak import ArcticPeak
from project.summit_peak import SummitPeak
from project.base_peak import BasePeak


class SummitQuestManagerApp:
    def __init__(self):
        self.climbers = []
        self.peaks = []

    def register_climber(self, climber_type: str, climber_name: str) -> str:
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

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int) -> str:
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
        if not climber:
            return f"{climber_name} is not registered as a climber."

        peak = next((p for p in self.peaks if p.name == peak_name), None)
        if not peak:
            return f"{peak_name} is not part of the wish list."

        recommended_gear = peak.get_recommended_gear()
        if set(gear) == set(recommended_gear):
            return f"{climber_name} is prepared to climb {peak_name}."
        else:
            missing_gear = sorted(set(recommended_gear) - set(gear))
            climber.is_prepared = False
            return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(missing_gear)}"

    def perform_climbing(self, climber_name: str, peak_name: str):
        climber = next((c for c in self.climbers if c.name == climber_name), None)
        if not climber:
            return f"Climber {climber_name} is not registered yet."

        peak = next((p for p in self.peaks if p.name == peak_name), None)
        if not peak:
            return f"Peak {peak_name} is not part of the wish list."

        if not climber.can_climb() or not climber.is_prepared:
            if not climber.is_prepared:
                return f"{climber_name} will need to be better prepared next time."
            else:
                climber.rest()
                return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

        climber.climb(peak)
        return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."
