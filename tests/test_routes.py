"""Route tests for the dashboard application."""


class TestDashboardRoutes:
    def test_index_returns_200(self, client):
        response = client.get("/")
        assert response.status_code == 200

    def test_index_contains_dashboard_title(self, client):
        response = client.get("/")
        assert b"Admin Dashboard" in response.data

    def test_index_contains_cards(self, client):
        response = client.get("/")
        assert b"card__title" in response.data

    def test_index_contains_sidebar(self, client):
        response = client.get("/")
        assert b"sidebar" in response.data

    def test_static_css_base_accessible(self, client):
        response = client.get("/static/css/base.css")
        assert response.status_code == 200

    def test_static_css_components_accessible(self, client):
        response = client.get("/static/css/components.css")
        assert response.status_code == 200

    def test_static_css_dashboard_accessible(self, client):
        response = client.get("/static/css/dashboard.css")
        assert response.status_code == 200

    def test_static_js_accessible(self, client):
        response = client.get("/static/js/dashboard.js")
        assert response.status_code == 200

    def test_api_metrics_returns_json(self, client):
        response = client.get("/api/metrics")
        assert response.status_code == 200
        data = response.get_json()
        assert "metrics" in data
        assert "performance" in data

    def test_announcement_bar_rendered(self, client):
        response = client.get("/")
        assert b"announcement-bar" in response.data

    def test_modal_markup_present(self, client):
        response = client.get("/")
        assert b"detail-modal" in response.data

    def test_toast_container_present(self, client):
        response = client.get("/")
        assert b"toast-container" in response.data
