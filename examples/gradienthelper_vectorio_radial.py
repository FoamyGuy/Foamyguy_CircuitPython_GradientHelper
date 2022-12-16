# SPDX-FileCopyrightText: Copyright (c) 2022 Tim Cocks
#
# SPDX-License-Identifier: MIT
from simpleio import map_range

from foamyguy_gradienthelper import (
    linear_gradient,
    polylinear_gradient,
    bezier_gradient,
)
from displayio import Group, Palette
import vectorio
import board

display = board.DISPLAY

COLOR_COUNT = 67

main_group = Group()

bezier_gradient = bezier_gradient((0xff00ff, 0x00ffff, 0x00ff00), COLOR_COUNT)

rect_group = Group()

bezier_palette = Palette(COLOR_COUNT)

for i, color in enumerate(bezier_gradient):
    bezier_palette[i] = color

    circle = vectorio.Circle(
        pixel_shader=bezier_palette,
        x=display.width//2, y=134//2,
        radius=(80)-i,
        color_index=i)
    rect_group.append(circle)

rectangle = vectorio.Rectangle(
    pixel_shader=bezier_palette,
    width=display.width,
    height=display.height,
    x=0, y=0,
    color_index=0)

main_group.append(rectangle)
main_group.append(rect_group)

display.show(main_group)

while True:
    pass
