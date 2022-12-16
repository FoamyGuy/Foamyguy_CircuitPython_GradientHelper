# SPDX-FileCopyrightText: Copyright (c) 2022 Tim Cocks
#
# SPDX-License-Identifier: MIT
"""
`foamyguy_gradienthelper`
================================================================================

Tools for generating color gradient palettes and shapes.


* Author(s): Tim Cocks

Implementation Notes
--------------------

**Hardware:**


**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads

"""

# imports

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/Foamyguy/Foamyguy_CircuitPython_GradientHelper.git"

try:
    from typing import List, Tuple
except ImportError:
    pass


def tuple_to_hex(tuple_color: Tuple[int, int, int]) -> int:
    return (
        (int(tuple_color[0]) << 16) + (int(tuple_color[1]) << 8) + int(tuple_color[2])
    )


def hex_to_tuple(hex_color: int) -> Tuple[int, int, int]:
    r = hex_color >> 16
    g = (hex_color & 0x00FF00) >> 8
    b = hex_color & 0x0000FF
    return r, g, b


def linear_gradient(
    start_color: int, finish_color: int = 0xFFFFFF, n: int = 10
) -> List[int]:
    """returns a gradient list of (n) colors between
    two hex colors.
    """
    # Starting and ending colors in RGB form
    s = hex_to_tuple(start_color)
    f = hex_to_tuple(finish_color)

    # Initilize a list of the output colors with the starting color
    RGB_list = [tuple_to_hex(s)]
    # Calcuate a color at each evenly spaced value of t from 1 to n
    for t in range(1, n):
        # Interpolate RGB vector for color at the current value of t
        curr_vector = tuple(
            [int(s[j] + (float(t) / (n - 1)) * (f[j] - s[j])) for j in range(3)]
        )
        # Add it to our list of output colors
        RGB_list.append(tuple_to_hex(curr_vector))

    return RGB_list


def polylinear_gradient(colors: List[int], n: int) -> List[int]:
    """returns a list of colors forming linear gradients between
    all sequential pairs of colors. "n" specifies the total
    number of desired output colors"""
    # The number of colors per individual linear gradient
    n_out = int(float(n) / (len(colors) - 1))

    # print(n_out)
    gradient_out = linear_gradient(colors[0], colors[1], n_out)

    if len(colors) > 1:
        for col in range(1, len(colors) - 1):
            if len(colors) > 2:
                next = linear_gradient(colors[col], colors[col + 1], n_out + 1)
            else:
                next = linear_gradient(colors[col], colors[col + 1], n_out)

            gradient_out.extend(next[1:])

    return gradient_out


fact_cache = {}


def fact(n: int) -> int:
    """Memoized factorial function"""
    try:
        return fact_cache[n]
    except (KeyError):
        if n == 1 or n == 0:
            result = 1
        else:
            result = n * fact(n - 1)
        fact_cache[n] = result
        return result


def bernstein(t: float, n: int, i: int) -> float:
    """Bernstein coefficient"""
    binom = fact(n) / float(fact(i) * fact(n - i))
    return binom * ((1 - t) ** (n - i)) * (t**i)


def bezier_gradient(colors: List[int], n_out: int = 100) -> List[int]:
    """Returns a "bezier gradient" list of colors
    using a given list of colors as control
    points."""
    # RGB vectors for each color, use as control points
    RGB_list = [hex_to_tuple(color) for color in colors]
    # print(RGB_list)
    n = len(RGB_list) - 1

    def bezier_interp(t: float) -> List[int]:
        """Define an interpolation function
        for this specific curve"""
        # List of all summands
        summands = [
            list(map(lambda x: int(bernstein(t, n, i) * x), c))
            for i, c in enumerate(RGB_list)
        ]

        # Output color
        out = [0, 0, 0]
        # Add components of each summand together
        for vector in summands:
            vector_list = list(vector)
            for c in range(3):
                out[c] += vector_list[c]

        return out

    gradient = [
        tuple_to_hex(bezier_interp(float(t) / (n_out - 1))) for t in range(n_out)
    ]

    return gradient
