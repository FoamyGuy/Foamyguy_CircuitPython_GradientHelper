# SPDX-FileCopyrightText: Copyright (c) 2022 Tim Cocks
#
# SPDX-License-Identifier: MIT

import board
from displayio import Group, Palette
import vectorio
from foamyguy_gradienthelper import (
    bezier_gradient,
)

display = board.DISPLAY

COLOR_COUNT = 67

main_group = Group()

bezier_gradient = bezier_gradient((0xFF00FF, 0x00FFFF, 0x00FF00), COLOR_COUNT)

rect_group = Group()

bezier_palette = Palette(COLOR_COUNT)
for i, color in enumerate(bezier_gradient):
    bezier_palette[i] = color
    rectangle = vectorio.Rectangle(
        pixel_shader=bezier_palette,
        width=display.width - (i * 2),
        height=134 - (i * 2),
        x=0 + i,
        y=0 + i,
        color_index=i,
    )
    rect_group.append(rectangle)

main_group.append(rect_group)

display.show(main_group)

while True:
    pass
