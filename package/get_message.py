import textwrap
from PIL import *


def get_message():
	print("Enter your message after the prompt below:")
	print("-No White Space Chars")
	print("-Max 1,000 char\n")
	my_text = input("MESSAGE: ")

	wrapper = textwrap.TextWrapper(width=68)
	word_list = wrapper.wrap(text=my_text)
	new_text = ""
	for word in word_list[:-1]:
	    new_text = new_text + word + '\n'
	new_text += word_list[-1]

	font = ImageFont.truetype('RobotoMono-Regular', 48)

	img = Image.new('RGB', (2100, 2000), color = (255, 255, 255))

	d = ImageDraw.Draw(img)
	d.text((10,5),new_text, fill=(0,0,0),font=font)
	 
	img.save('msg_text.png')

	return my_text

