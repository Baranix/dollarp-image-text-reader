from PIL import Image
import numpy as np
import dollarpy
from itertools import count

_DIR_IMAGE = "img/"

"""
	Get letter template.
"""

template_letter = Image.open(_DIR_IMAGE + "A_calibri.png")
template_pixels = np.asarray(template_letter)

# print(pixels)

# for pixel in pixels:
# 	print(pixel)

# black_points = [(col_index, row_index) for col_index, row in zip(count(), pixels) for row_index, pixel in zip(count(), row) if np.array_equal(pixel, np.array([0,0,0]))]

black_points = []

for col_index, row in zip(count(), template_pixels):
	# print(col)
	for row_index, pixel in zip(count(), row):
		if np.array_equal(pixel, np.array([0,0,0])):
			point = dollarpy.Point(col_index, row_index)
			print("black_point at " + str(point))
			black_points.append(point)

# print(black_points)

template_A = dollarpy.Template('A', black_points)

recognizer = dollarpy.Recognizer([template_A])

"""
	Letter to be read.
"""

read_letter = Image.open(_DIR_IMAGE + "A_timesnewroman.png")
read_pixels = np.asarray(read_letter)

black_points = []

for col_index, row in zip(count(), template_pixels):
	# print(col)
	for row_index, pixel in zip(count(), row):
		if np.array_equal(pixel, np.array([0,0,0])):
			point = dollarpy.Point(col_index, row_index)
			print("black_point at " + str(point))
			black_points.append(point)

# print(black_points)

result = recognizer.recognize(black_points)

print("####")
print("RESULTS:")
print(result)