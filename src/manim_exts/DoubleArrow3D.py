from manim import *
import numpy as np

class DoubleArrow3D(VGroup):
    def __init__(
        self,
        start,
        end,
        color=WHITE,
        buff=0,
        cut=0.2,  # distance to trim from each end along the line
        **kwargs,
    ):
        super().__init__()

        # Ensure numpy arrays
        start = np.array(start, dtype=float)
        end = np.array(end, dtype=float)

        # Direction vector from start → end
        direction = end - start
        length = np.linalg.norm(direction)

        if length == 0:
            raise ValueError(
                "Start and end points are identical; arrow has zero length."
            )

        # Normalize
        unit_dir = direction / length

        # Shift both ends inward by `cut` distance
        start_cut = start + unit_dir * cut
        end_cut = end - unit_dir * cut

        # Create two opposing 3D arrows
        arrow1 = Arrow3D(start=start_cut, end=end, color=color, **kwargs)
        arrow2 = Arrow3D(start=end_cut, end=start, color=color, **kwargs)
        self.add(arrow1, arrow2)

