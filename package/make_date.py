from datetime import datetime
from datetime import timedelta
import textwrap
from PIL import *
import sys
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def make_date():
	#Sent = today's date
	sent = datetime.date(datetime.now())

	#sent = today's date minus 2from datetime import datetime
	arrive = sent + timedelta(days=3)

	my_text = f"Sent:        {sent}  Arrive(est): {arrive}"
	wrapper = textwrap.TextWrapper(width=25)
	word_list = wrapper.wrap(text=my_text)
	new_text = ""
	for word in word_list[:-1]:
	    new_text = new_text + word + '\n'
	new_text += word_list[-1]

	font = ImageFont.truetype('RobotoMono-Regular', 48)

	img = Image.new('RGB', (675, 110), color = (255, 255, 255))

	d = ImageDraw.Draw(img)
	d.text((5,-10),new_text, fill=(0,0,0),font=font)
	 
	img.save('date_text.png')

	return my_text