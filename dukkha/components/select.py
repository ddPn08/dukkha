from typing import *
from reactpy import html, component
from reactpy.core.types import VdomChildren


@component
def Select(
    children: VdomChildren,
    disabled: bool = False,
    **props,
):
    classname = {
        "container": "relative",
        "select": "block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md",
        "icon": "absolute inset-y-0 right-0 flex items-center px-2 pointer-events-none",
    }

    if disabled:
        classname["select"] += " opacity-50 cursor-not-allowed"

    return html.div(
        {
            "class": classname["container"],
        },
        html.select(
            {
                "class": classname["select"],
                "disabled": disabled,
            },
            children,
        ),
    )
