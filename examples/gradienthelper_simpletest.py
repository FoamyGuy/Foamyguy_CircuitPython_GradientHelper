# SPDX-FileCopyrightText: Copyright (c) 2022 Tim Cocks
#
# SPDX-License-Identifier: MIT
from foamyguy_gradienthelper import (
    linear_gradient,
    polylinear_gradient,
    bezier_gradient,
)


def print_palette(palette):
    out_str = "["
    for color in palette:
        out_str = f"{out_str}{color:#0{8}x}, "
    out_str = out_str[:-2]
    out_str = f"{out_str}]"
    print(out_str)


linear_colors = linear_gradient(0xFF0000, 0x0000FF, 10)
print_palette(linear_colors)

polylinear_colors = polylinear_gradient((0x00FF00, 0xFFFF00, 0x00FFFF), 30)
print_palette(polylinear_colors)

bezier_colors = bezier_gradient((0xFF00FF, 0x00FFFF, 0x00FF00), 100)
print_palette(bezier_colors)
