from abc import ABC, abstractmethod


class BaseInfluencer(ABC):
    def __init__(self, username: str, followers: int, engagement_rate: float):
        self.username = username
        self.followers = followers
        self.engagement_rate = engagement_rate
        self.campaigns_participated = []

    @abstractmethod
    def calculate_payment(self, campaign):
        pass

    @abstractmethod
    def reached_followers(self, campaign_type: str):
        pass

    def display_campaigns_participated(self):
        if not self.campaigns_participated:
            return f"{self.username} has not participated in any campaigns."
        else:
            report = [f"{self.__class__.__name__} :) {self.username} :) participated in the following campaigns:"]
            for campaign in self.campaigns_participated:
                reached_followers = self.reached_followers(campaign.__class__.__name__)
                report.append(
                    f"  - Campaign ID: {campaign.campaign_id}, Brand: {campaign.brand}, Reached followers: {reached_followers}"
                )
            return "\n".join(report)
