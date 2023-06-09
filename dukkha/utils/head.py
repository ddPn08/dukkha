import json
from reactpy import html


DEFAULT_TAILWIND_CONFIG = {
    "darkMode": "class",
}


def create_head(head=[], tailwind_config={}):
    return (
        html.title("components"),
        html.link(
            {
                "href": "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap",
                "rel": "stylesheet",
            }
        ),
        html.script({"src": "https://cdn.tailwindcss.com"}, ""),
        html.script(
            f"""
            tailwind.config = {json.dumps(
                {
                    **DEFAULT_TAILWIND_CONFIG,
                    **tailwind_config,
                }
            )}
            """
        ),
        *head,
    )
