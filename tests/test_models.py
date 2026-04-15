"""Unit tests for dashboard data models."""

from dashboard.models import MetricCard, DashboardData, ActivityItem


class TestMetricCard:
    def test_format_currency_millions(self):
        assert MetricCard.format_currency(2_500_000) == "$2.5M"

    def test_format_currency_thousands(self):
        assert MetricCard.format_currency(128_400) == "$128.4K"

    def test_format_currency_small(self):
        assert MetricCard.format_currency(42.50) == "$42.50"

    def test_format_percentage(self):
        assert MetricCard.format_percentage(12.5) == "+12.5%"

    def test_format_percentage_negative(self):
        assert MetricCard.format_percentage(-3.2) == "-3.2%"

    def test_growth_indicator_positive(self):
        assert MetricCard.growth_indicator(110, 100) == "up"

    def test_growth_indicator_negative(self):
        assert MetricCard.growth_indicator(90, 100) == "down"

    def test_growth_indicator_zero(self):
        assert MetricCard.growth_indicator(100, 100) == "neutral"

    def test_growth_indicator_zero_previous(self):
        assert MetricCard.growth_indicator(50, 0) == "neutral"

    def test_trend_icon_up(self):
        card = MetricCard("Test", "100", "+5%", "up")
        assert card.trend_icon == "+"

    def test_trend_icon_down(self):
        card = MetricCard("Test", "100", "-5%", "down")
        assert card.trend_icon == "-"

    def test_trend_dir(self):
        card = MetricCard("Test", "100", "+5%", "up")
        assert card.trend_dir == "up"


class TestDashboardData:
    def test_get_metrics_returns_list(self):
        metrics = DashboardData.get_metrics()
        assert isinstance(metrics, list)
        assert len(metrics) == 4

    def test_metric_has_required_fields(self):
        metrics = DashboardData.get_metrics()
        for m in metrics:
            assert hasattr(m, "title")
            assert hasattr(m, "value")
            assert hasattr(m, "trend")
            assert hasattr(m, "trend_direction")

    def test_get_performance_returns_list(self):
        perf = DashboardData.get_performance()
        assert isinstance(perf, list)
        assert len(perf) == 3

    def test_get_activities_returns_list(self):
        activities = DashboardData.get_activities()
        assert isinstance(activities, list)
        assert len(activities) == 3

    def test_activity_has_required_fields(self):
        activities = DashboardData.get_activities()
        for a in activities:
            assert isinstance(a, ActivityItem)
            assert a.title
            assert a.description
            assert a.time

    def test_get_all_keys(self):
        data = DashboardData.get_all()
        assert "metrics" in data
        assert "performance" in data
        assert "activities" in data
