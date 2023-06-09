from typing import *
from reactpy import html, component
from reactpy.core.types import VdomChildren


@component
def Stack(
    children: VdomChildren,
    direction: Literal["row", "column"] = "row",
    gap: Union[str, int, float] = 4,
    **props,
):
    class_name = " ".join(
        [
            "flex",
            "flex-wrap",
            "gap",
        ]
    )

    if direction == "column":
        class_name += " flex-col"

    class_name += f" gap-{gap}"

    return html._(
        html.div(
            {"class": class_name, **props},
            children,
        )
    )
