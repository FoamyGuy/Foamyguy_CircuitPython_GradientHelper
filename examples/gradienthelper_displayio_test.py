# SPDX-FileCopyrightText: Copyright (c) 2022 Tim Cocks
#
# SPDX-License-Identifier: MIT
import board
from simpleio import map_range
from displayio import Group, Bitmap, TileGrid, Palette
from foamyguy_gradienthelper import (
    linear_gradient,
    polylinear_gradient,
    bezier_gradient,
)

display = board.DISPLAY

COLOR_COUNT = 60

main_group = Group()

linear_colors = linear_gradient(0xFF0000, 0x0000FF, COLOR_COUNT)

linear_bitmap = Bitmap(display.width, 30, COLOR_COUNT)

linear_palette = Palette(COLOR_COUNT)
for i, color in enumerate(linear_colors):
    linear_palette[i] = color

linear_tilegrid = TileGrid(
    linear_bitmap,
    pixel_shader=linear_palette,
    tile_width=linear_bitmap.width,
    tile_height=linear_bitmap.height,
)

main_group.append(linear_tilegrid)

polylinear_colors = polylinear_gradient((0xFF00FF, 0x00FFFF, 0x00FF00), COLOR_COUNT)

polylinear_bitmap = Bitmap(display.width, 30, COLOR_COUNT)

polylinear_palette = Palette(COLOR_COUNT)
for i, color in enumerate(polylinear_colors):
    polylinear_palette[i] = color

polylinear_tilegrid = TileGrid(
    polylinear_bitmap,
    pixel_shader=polylinear_palette,
    tile_width=polylinear_bitmap.width,
    tile_height=polylinear_bitmap.height,
    y=30 + 20,
)

main_group.append(polylinear_tilegrid)

bezier_colors = bezier_gradient((0xFF00FF, 0x00FFFF, 0x00FF00), COLOR_COUNT)

bezier_bitmap = Bitmap(display.width, 30, COLOR_COUNT)

bezier_palette = Palette(COLOR_COUNT)
for i, color in enumerate(bezier_colors):
    bezier_palette[i] = color

bezier_tilegrid = TileGrid(
    bezier_bitmap,
    pixel_shader=bezier_palette,
    tile_width=bezier_bitmap.width,
    tile_height=bezier_bitmap.height,
    y=50 + 30 + 20,
)

main_group.append(bezier_tilegrid)

display.show(main_group)

for x in range(linear_bitmap.width):
    for y in range(linear_bitmap.height):
        # print(f"x: {x}, y: {y} = {cur_color}")
        # bitmap[x, y] = cur_color

        col_color = int(map_range(x, 0, linear_bitmap.width, 0, COLOR_COUNT))
        linear_bitmap[x, y] = col_color
        polylinear_bitmap[x, y] = col_color
        bezier_bitmap[x, y] = col_color

while True:
    pass
