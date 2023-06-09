import random
from typing import *
from reactpy import html, component
from reactpy.core.types import VdomChildren


@component
def Checkbox(
    children: VdomChildren,
    disabled: bool = False,
    **props,
):
    random_id = props.get(
        "id", "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=20))
    )

    classname = {
        "container": "flex items-center mb-4",
        "input": "w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600",
        "label": "ml-2 text-sm font-medium text-gray-900 dark:text-gray-300",
    }

    if disabled:
        classname["input"] += " opacity-50 cursor-not-allowed"

    return html.div(
        {
            "class": classname["container"],
        },
        html.input(
            {
                "class": classname["input"],
                "type": "checkbox",
                "disabled": disabled,
                "id": random_id,
            },
        ),
        html.label(
            {
                "class": classname["label"],
                "for": random_id,
            },
            children,
        ),
    )
