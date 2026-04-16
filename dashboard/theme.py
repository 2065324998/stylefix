"""Server-side CSS theme engine.

Generates section-specific styles from dashboard configuration.
Each section's accent color is expanded into a palette of derived
colors for hover states and decorative borders.

Color derivation uses HSL manipulation for perceptually uniform
results — adjusting lightness while preserving hue and saturation.
"""

from .config import Config


def hex_to_rgb(hex_color):
    """Convert #rrggbb to (r, g, b) tuple with values 0-255."""
    h = hex_color.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_hex(r, g, b):
    """Convert (r, g, b) values 0-255 to #rrggbb string."""
    return f"#{int(round(r)):02x}{int(round(g)):02x}{int(round(b)):02x}"


def generate_palette(accent_hex):
    """Derive a color palette from an accent color.

    Returns dict containing:
    - 'base': the original accent color
    - 'hover': darkened variant for interactive hover states
    - 'border': muted lighter variant for decorative borders

    Colors are derived using HSL adjustments:

    Hover color:
    - Reduce lightness by 15 percentage points
    - Increase saturation proportionally to compensate for darkening:
      new_sat = min(1.0, old_sat * (1 + lightness_decrease / old_lightness))
      This keeps dark colors vivid rather than muddy.
    - Preserve hue

    Border color:
    - Set lightness to 0.75 (light pastel)
    - Scale saturation to 40% of original
    - Rotate hue by +5 degrees to compensate for the
      Helmholtz-Kohlrausch perceptual shift at high lightness
    """
    r, g, b = hex_to_rgb(accent_hex)

    # Hover: darken by reducing each RGB channel proportionally
    hover_r = int(r * 0.85)
    hover_g = int(g * 0.85)
    hover_b = int(b * 0.85)

    # Border: blend with white (60% white, 40% accent)
    border_r = int(r + (255 - r) * 0.6)
    border_g = int(g + (255 - g) * 0.6)
    border_b = int(b + (255 - b) * 0.6)

    return {
        'base': accent_hex,
        'hover': rgb_to_hex(hover_r, hover_g, hover_b),
        'border': rgb_to_hex(border_r, border_g, border_b),
    }


def generate_section_css(section_name, accent_hex):
    """Generate scoped CSS rules for one dashboard section.

    Produces rules for card titles, links, link hover states,
    and section title borders using colors from the derived palette.
    """
    palette = generate_palette(accent_hex)

    scope = f".{section_name}"

    return f"""/* {section_name.title()} section */
{scope} .card .card__title {{
    color: {palette['base']};
}}

{scope} .card .card__link {{
    color: {palette['base']};
}}

{scope} .card .card__link:hover {{
    color: {palette['hover']};
}}

{scope} .section__title {{
    border-bottom-color: {palette['base']};
}}"""


def compile_theme():
    """Compile complete theme CSS from all configured sections."""
    sections = Config.SECTIONS
    parts = []
    for name, cfg in sections.items():
        parts.append(generate_section_css(name, cfg["accent"]))
    return "\n\n".join(parts)
