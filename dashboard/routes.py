"""Route handlers for the dashboard."""

from flask import render_template, jsonify

from .models import DashboardData
from .config import Config


def register_routes(app):

    @app.route("/")
    def index():
        data = DashboardData.get_all()
        return render_template(
            "dashboard.html",
            metrics=data["metrics"],
            performance=data["performance"],
            activities=data["activities"],
            announcement=Config.ANNOUNCEMENT,
            sections=Config.SECTIONS,
        )

    @app.route("/api/metrics")
    def api_metrics():
        data = DashboardData.get_all()
        return jsonify({
            "metrics": [
                {"title": m.title, "value": m.value, "trend": m.trend}
                for m in data["metrics"]
            ],
            "performance": [
                {"title": m.title, "value": m.value, "trend": m.trend}
                for m in data["performance"]
            ],
        })
