# This work is licensed under the MIT license.
# Copyright (c) 2013-2023 OpenMV LLC. All rights reserved.
# https://github.com/openmv/openmv/blob/master/LICENSE
#
# Draw Image Example
#
# This example shows off how to draw images in the frame buffer.

import sensor
import time
import image

sensor.reset()
sensor.set_pixformat(sensor.RGB565)  # or GRAYSCALE...
sensor.set_framesize(sensor.QVGA)  # or QQVGA...
sensor.skip_frames(time=2000)
clock = time.clock()

while True:
    clock.tick()

    img = sensor.snapshot()
    small_img = img.scale(x_scale=0.25, y_scale=0.25, hint=image.AREA, copy=True)

    x = (img.width() // 2) - (small_img.width() // 2)
    y = (img.height() // 2) - (small_img.height() // 2)
    # Draws an image in the frame buffer.Pass an optional
    # mask image to control what pixels are drawn.
    img.draw_image(small_img, x, y, x_scale=1, y_scale=1)

    print(clock.fps())
