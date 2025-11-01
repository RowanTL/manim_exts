from manim import *
import numpy as np


class FlashColor(Animation):
    """
    Temporarily sets a mobject to a color and then back
    """

    def __init__(
        self, vmobject: VMobject | OpenGLVMobject, color: ManimColor, **kwargs
    ) -> None:
        super().__init__(vmobject, **kwargs)
        self.color = color

    def begin(self) -> None:
        pass
