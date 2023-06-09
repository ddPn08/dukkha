from fastapi import FastAPI
from uvicorn import run
from reactpy import component, html, hooks
from reactpy.backend.fastapi import configure, Options

from dukkha.utils import head
import demo

app = FastAPI()


def Components():
    for name, component in demo.demos.items():
        yield html.div(
            {
                "class": "p-4 border-2 border-gray-200 rounded-lg shadow-md my-4",
            },
            html.h2(
                {
                    "class": "text-2xl font-bold mb-4",
                },
                name,
            ),
            component(),
        )


@component
def Root():
    dark, set_dark = hooks.use_state(False)

    return html.main(
        {
            "class": "dark" if dark else "",
        },
        html.button(
            {
                "class": "fixed bottom-4 right-4 p-2 rounded-full shadow-md",
                "on_click": lambda _: set_dark(not dark),
            },
            html.span(
                {
                    "class": "text-2xl",
                },
                "🌞" if dark else "🌚",
            ),
        ),
        html.div(
            {
                "class": "bg-gray-100 min-h-screen dark:bg-gray-900 dark:text-white",
            },
            html.div(
                {
                    "class": "container mx-auto p-4",
                },
                html.h1(
                    {
                        "class": "text-6xl font-bold mb-4",
                    },
                    "components",
                ),
                html.div(
                    *Components(),
                ),
            ),
        ),
    )


configure(
    app,
    Root,
    Options(head=head.create_head(tailwind_config={})),
)

if __name__ == "__main__":
    run(app)
