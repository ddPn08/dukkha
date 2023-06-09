from typing import *
from reactpy import html, component


@component
def Input(
    disabled: bool = False,
    **props,
):
    class_name = " ".join(
        [
            "block",
            "w-full",
            "px-3",
            "py-2",
            "text-base",
            "placeholder-gray-500",
            "border",
            "border-gray-300",
            "rounded-md",
            "shadow-sm",
            "focus:outline-none",
            "focus:ring-2",
            "focus:ring-indigo-500",
            "focus:border-indigo-500",
            "sm:text-sm",
        ]
    )

    if disabled:
        class_name += " opacity-50 cursor-not-allowed"

    return html._(
        html.input(
            {
                "class": class_name,
                "type": "text",
                "disabled": disabled,
                **props,
            },
        )
    )
