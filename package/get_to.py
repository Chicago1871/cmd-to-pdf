import textwrap
from PIL import *
import sys
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# Saves text as PNG with white background AND returns my_text
def get_to():
	my_text = input("TO:  ")
	wrapper = textwrap.TextWrapper(width=75)
	word_list = wrapper.wrap(text=my_text)
	new_text = ""
	for word in word_list[:-1]:
	    new_text = new_text + word + '\n'
	new_text += word_list[-1]

	font = ImageFont.truetype('RobotoMono-Regular', 48)

	img = Image.new('RGB', (1000, 65), color = (255, 255, 255))

	d = ImageDraw.Draw(img)
	d.text((15,0),new_text, fill=(0,0,0),font=font)
	 
	img.save('emto_text.png')

	return my_text
