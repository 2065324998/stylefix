"""Dashboard data models and sample data."""

from dataclasses import dataclass
from typing import List


@dataclass
class MetricCard:
    title: str
    value: str
    trend: str
    trend_direction: str  # "up", "down", "neutral"

    @property
    def trend_dir(self):
        return self.trend_direction

    @property
    def trend_icon(self):
        icons = {"up": "+", "down": "-", "neutral": "~"}
        return icons.get(self.trend_direction, "~")

    @staticmethod
    def format_currency(amount: float) -> str:
        if amount >= 1_000_000:
            return f"${amount / 1_000_000:.1f}M"
        if amount >= 1_000:
            return f"${amount / 1_000:.1f}K"
        return f"${amount:.2f}"

    @staticmethod
    def format_percentage(value: float) -> str:
        return f"{value:+.1f}%"

    @staticmethod
    def growth_indicator(current: float, previous: float) -> str:
        if previous == 0:
            return "neutral"
        change = (current - previous) / previous
        if change > 0.01:
            return "up"
        elif change < -0.01:
            return "down"
        return "neutral"


@dataclass
class ActivityItem:
    title: str
    description: str
    time: str


class DashboardData:
    """Provides sample data for the dashboard."""

    @staticmethod
    def get_metrics() -> List[MetricCard]:
        return [
            MetricCard("Revenue", "$128.4K", "+12.5%", "up"),
            MetricCard("Users", "8,429", "+3.2%", "up"),
            MetricCard("Orders", "1,247", "-2.1%", "down"),
            MetricCard("Conversion", "3.6%", "+0.4%", "up"),
        ]

    @staticmethod
    def get_performance() -> List[MetricCard]:
        return [
            MetricCard("Uptime", "99.97%", "+0.02%", "up"),
            MetricCard("Avg Response", "142ms", "-8ms", "up"),
            MetricCard("Error Rate", "0.03%", "-0.01%", "up"),
        ]

    @staticmethod
    def get_activities() -> List[ActivityItem]:
        return [
            ActivityItem(
                "Deploy v2.4.1",
                "Production deployment completed successfully",
                "2 hours ago",
            ),
            ActivityItem(
                "Database Migration",
                "Schema update applied to analytics cluster",
                "5 hours ago",
            ),
            ActivityItem(
                "Alert Resolved",
                "High memory usage on worker-03 resolved",
                "1 day ago",
            ),
        ]

    @staticmethod
    def get_all():
        return {
            "metrics": DashboardData.get_metrics(),
            "performance": DashboardData.get_performance(),
            "activities": DashboardData.get_activities(),
        }
