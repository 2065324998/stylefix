# StyleFix Dashboard

An admin dashboard built with Flask, featuring component-based CSS architecture
with section-specific theming.

## Setup

```bash
pip install -e ".[dev]"
playwright install chromium
```

## Running

```bash
flask --app dashboard.app run
```

## Testing

```bash
pytest tests/ -v
```

## Architecture

- `dashboard/` - Flask application package
- `static/css/` - Layered CSS: base → layout → components → dashboard
- `templates/` - Jinja2 templates
- `tests/` - Unit and integration tests
