"""Dashboard configuration."""


class Config:
    SECRET_KEY = "dev-secret-key"
    DEBUG = False
    TESTING = False

    # Dashboard sections and their theme colors
    SECTIONS = {
        "metrics": {
            "title": "Key Metrics",
            "accent": "#1a73e8",
        },
        "performance": {
            "title": "Performance",
            "accent": "#34a853",
        },
        "activity": {
            "title": "Recent Activity",
            "accent": "#ea4335",
        },
    }

    ANNOUNCEMENT = {
        "message": "System maintenance scheduled for April 20, 2026.",
        "link_text": "Learn more",
        "link_url": "#maintenance-info",
    }
