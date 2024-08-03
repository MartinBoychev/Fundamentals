from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    def __init__(self):
        self.influencers = []
        self.campaigns = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in ["PremiumInfluencer", "StandardInfluencer"]:
            return f"{influencer_type} is not an allowed influencer type."

        for influencer in self.influencers:
            if influencer.username == username:
                return f"{username} is already registered."

        if influencer_type == "PremiumInfluencer":
            influencer = PremiumInfluencer(username, followers, engagement_rate)
        else:
            influencer = StandardInfluencer(username, followers, engagement_rate)

        self.influencers.append(influencer)
        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in ["HighBudgetCampaign", "LowBudgetCampaign"]:
            return f"{campaign_type} is not a valid campaign type."

        for campaign in self.campaigns:
            if campaign.campaign_id == campaign_id:
                return f"Campaign ID {campaign_id} has already been created."

        if campaign_type == "HighBudgetCampaign":
            campaign = HighBudgetCampaign(campaign_id, brand, required_engagement)
        else:
            campaign = LowBudgetCampaign(campaign_id, brand, required_engagement)

        self.campaigns.append(campaign)
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        influencer = next((x for x in self.influencers if x.username == influencer_username), None)
        if not influencer:
            return f"Influencer '{influencer_username}' not found."

        campaign = next((x for x in self.campaigns if x.campaign_id == campaign_id), None)
        if not campaign:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility(influencer.engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."

        payment = influencer.calculate_payment(campaign)
        if payment > 0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= payment
            influencer.campaigns_participated.append(campaign)

        return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self):
        reached_followers = {}
        for influencer in self.influencers:
            for campaign in influencer.campaigns_participated:
                reached_followers[campaign] = reached_followers.get(campaign, 0) + influencer.reached_followers(
                    campaign.__class__.__name__)
        return reached_followers

    def influencer_campaign_report(self, username: str):
        influencer = next((x for x in self.influencers if x.username == username), None)
        if not influencer:
            return f"{username} has not participated in any campaigns."
        else:
            return influencer.display_campaigns_participated()

    def campaign_statistics(self):
        sorted_campaigns = sorted(self.campaigns, key=lambda x: (len(x.approved_influencers), -x.budget))
        report = ["$$ Campaign Statistics $$"]
        for campaign in sorted_campaigns:
            total_reached_followers = sum(influencer.reached_followers(campaign.__class__.__name__) for influencer in
                                          campaign.approved_influencers)
            report.append(
                f"  * Brand: {campaign.brand}, Total influencers: {len(campaign.approved_influencers)}, Total budget: ${campaign.budget:.2f}, Total reached followers: {total_reached_followers}")
        return "\n".join(report)
