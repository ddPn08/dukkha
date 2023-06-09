from reactpy import html
from dukkha.components import Stack, Button, Checkbox, Input, Select


demos = {
    "Button": lambda: Stack(
        html._(
            Button("Submit"),
            Button("Submit", variant="secondary"),
            Button("Submit", variant="tertiary"),
            Button("Submit", variant="danger"),
            Button("Submit", disabled=True),
            Button("Submit", compact=True),
        ),
    ),
    "Checkbox": lambda: Stack(
        html._(
            Checkbox("Checkbox"),
            Checkbox("Checkbox", disabled=True),
        )
    ),
    "Input": lambda: Stack(
        html._(
            Input(placeholder="Placeholder"),
            Input(placeholder="Placeholder", disabled=True),
        )
    ),
    "Select": lambda: Stack(
        html._(
            Select(
                html._(
                    html.option("Option 1"),
                    html.option("Option 1"),
                )
            )
        )
    ),
}
