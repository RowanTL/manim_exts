__version__ = "0.1.0"

from manim import *
import numpy as np


class AugmentedMatrix(VGroup):
    def __init__(
        self,
        mat,
        sep_col=-1,
        line_stroke_width: int | float = 2,
        matrix_args: dict = {},
        line_args: dict = {},
        **kwargs,
    ):
        """
        A custom augmented matrix class. No need to pass the `start` and `end` parameters
        to line_args (they are calculated automatically).

        parameters:
            mat (Any 2D python sequence): The matrix to be created.
            sep_col (int, default=-1): The column to place the augmented matrix separator to the left of.
                Accepts negative indices.
            line_stroke_width (int | float, default=2): The stroke_width of the separator line. Made this a parameter
                because it may be commonly modified.
            matrix_args (dict): Any extra args to pass to the matrix constructor.
            line_args (dict): Any extra args to pass to the line constructor. `start` and `end` args are not mandatory.
            **kwargs: VGroup constructor args.
        """
        super().__init__(**kwargs)

        self.matrix: Matrix = Matrix(mat, **matrix_args)
        col: VGroup = self.matrix.get_columns()[sep_col]
        # now have the center point of the line
        line_center = col.get_center()
        # move line_center to correct x coordinate
        line_center[0] -= self.matrix.h_buff / 2
        # grab half the height so can add to center later
        # print(self.matrix.get_brackets()[0].height)
        temp_bracket = self.matrix.get_brackets()[0]
        bracket_v_delta = temp_bracket.height / 2
        # copy center matrix and subtract height for starting position
        line_start = line_center.copy()
        line_start[1] -= bracket_v_delta
        # copy center matrix and add height for end position
        line_end = line_center.copy()
        line_end[1] += bracket_v_delta
        self.line = Line(
            start=line_start,
            end=line_end,
            stroke_width=line_stroke_width,
            **line_args,
        )

        self.add(self.matrix, self.line)


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
