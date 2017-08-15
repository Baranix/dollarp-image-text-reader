from PIL import Image
import numpy as np
import dollarpy
from itertools import count
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from unicodedata import name as unicodename
import config

"""
	Initialize fonts.
"""

template_font = "GeosansLight"
read_font = "calibril"

"""
	Get letter template.
"""
def generate_template_set(character_set):
	template_set = []
	for char in character_set:
		char_name = unicodename(char).lower().replace(" ", "_")
		template_letter = Image.open(config._DIR_IMAGE + template_font + "/" + char_name + ".png")
		template_pixels = np.asarray(template_letter)
		# print(template_pixels)

		black_points = []

		for col_index, row in zip(count(), template_pixels):
			# print(col_index)
			for row_index, pixel in zip(count(), row):
				if not pixel:
					# print(pixel)
					point = dollarpy.Point(col_index, row_index)
					# print("black_point at " + str(point))
					black_points.append(point)

		# print(black_points)

		template_set.append(dollarpy.Template(char_name, black_points))

	return template_set

def generate_recognizer():
	all_templates = []
	all_templates.extend(generate_template_set(ascii_lowercase))
	all_templates.extend(generate_template_set(ascii_uppercase))
	all_templates.extend(generate_template_set(digits))
	all_templates.extend(generate_template_set(punctuation))

	return dollarpy.Recognizer(all_templates)


def SAMPLE_template():
	template_letter = Image.open(config._DIR_IMAGE + "A_calibri.png")
	template_pixels = np.asarray(template_letter)
	# print(template_pixels)

	black_points = []

	for col_index, row in zip(count(), template_pixels):
		# print(col_index)
		for row_index, pixel in zip(count(), row):
			if np.array_equal(pixel, np.array([0,0,0])):
				# print(pixel)
				point = dollarpy.Point(col_index, row_index)
				# print("black_point at " + str(point))
				black_points.append(point)

	template_A = dollarpy.Template('A', black_points)
	return dollarpy.Recognizer([template_A])

"""
	Letter to be read.
"""

def SAMPLE_read():
	read_letter = Image.open(config._DIR_IMAGE + "A_timesnewroman.png")
	read_pixels = np.asarray(read_letter)

	points = []

	for col_index, row in zip(count(), read_pixels):
		# print(col)
		for row_index, pixel in zip(count(), row):
			#if not pixel:
			if np.array_equal(pixel, np.array([0,0,0])):
				point = dollarpy.Point(col_index, row_index)
				# print("point at " + str(point))
				points.append(point)


def read():
	# char_name = unicodename(char).lower().replace(" ", "_")
	read_letter = Image.open(config._DIR_IMAGE + read_font + "/latin_capital_letter_b.png")
	read_pixels = np.asarray(read_letter)

	points = []

	for col_index, row in zip(count(), read_pixels):
		for row_index, pixel in zip(count(), row):
			if not pixel:
				point = dollarpy.Point(col_index, row_index)
				points.append(point)

	return points

recognizer = generate_recognizer()
result = recognizer.recognize(read())

print("RESULTS:")
print(result)