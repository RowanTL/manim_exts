from manim import *
from manim_exts import AugmentedMatrix
import numpy as np


class AugmentedMatrixScene(Scene):
    def construct(self):
        aug: AugmentedMatrix = AugmentedMatrix(
            np.array([[2, 2, 3], [3, 4, 5]]),
        )
        self.add(aug)
