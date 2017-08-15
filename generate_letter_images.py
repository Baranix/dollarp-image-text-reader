from PIL import Image, ImageDraw, ImageFont
import numpy as np
import dollarpy
from itertools import count
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from unicodedata import name as unicodename
import config

font_name = 'GeosansLight'
font_type = '.ttf'
font = ImageFont.truetype(font_name+font_type, 32)

def generate_images(character_set):
	for char in character_set:
		print(char)
		img = Image.new("1", (50,50), "white")
		canvas = ImageDraw.Draw(img)

		canvas.text((0, 0), char, "black", font=font)
		img.save(config._DIR_IMAGE + font_name + "/" + unicodename(char).lower().replace(" ", "_") + ".png")

def main():
	generate_images(ascii_lowercase)
	generate_images(ascii_uppercase)
	generate_images(digits)
	generate_images(punctuation)

main()