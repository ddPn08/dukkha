from typing import *
from reactpy import html, component
from reactpy.core.types import VdomChildren


@component
def Button(
    children: VdomChildren,
    compact: bool = False,
    disabled: bool = False,
    radius: Union[Literal["xs", "sm", "md", "lg", "xl"], float] = "md",
    type: Literal["button", "submit", "reset"] = "button",
    variant: Literal["primary", "secondary", "tertiary", "danger"] = "primary",
    **props,
):
    class_name = " ".join(
        [
            "inline-flex",
            "items-center",
            "justify-center",
            "border",
            "border-transparent",
            "font-medium",
            "rounded",
            "shadow-sm",
            "text-white",
            "focus:outline-none",
            "focus:ring-2",
            "focus:ring-offset-2",
            "focus:ring-indigo-500",
        ]
    )

    if variant == "primary":
        class_name += " bg-indigo-600 hover:bg-indigo-700 focus:ring-indigo-500"
    elif variant == "secondary":
        class_name += " bg-gray-600 hover:bg-gray-700 focus:ring-gray-500"
    elif variant == "tertiary":
        class_name += " bg-transparent hover:bg-gray-100 focus:ring-gray-500"
    elif variant == "danger":
        class_name += " bg-red-600 hover:bg-red-700 focus:ring-red-500"

    if compact:
        class_name += " px-2.5 py-1.5 text-xs"
    else:
        class_name += " px-4 py-2 text-sm"

    if isinstance(radius, float):
        class_name += f" rounded-{radius}"
    elif isinstance(radius, str):
        class_name += f" rounded-{radius}"

    if disabled:
        class_name += " opacity-50 cursor-not-allowed"

    return html._(
        html.button(
            {
                "class": class_name,
                "type": type,
                "disabled": disabled,
                **props,
            },
            children,
        )
    )
