from PIL import Image
import time
import json
import os
ASCII_CHARS = ['⠀','⠄','⠆','⠖','⠶','⡶','⣩','⣪','⣫','⣾','⣿']
'''
RECOMMEND USING THOSE CHARS FOR COMMAND PROMPT

$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\"^`
'''


def resized_gray_image(image ,new_width=70):
	width,height = image.size
	aspect_ratio = height/width
	new_height = 20
	resized_gray_image = image.resize((new_width,new_height)).convert('L')
	return resized_gray_image

def pix2chars(image):
	pixels = image.getdata()
	characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
	return characters

def generate_frame(image,new_width=70):
	new_image_data = pix2chars(resized_gray_image(image,new_width=new_width))
	total_pixels = len(new_image_data)
	output = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, total_pixels, new_width)])
	return output

with open('config.json') as penis:
    data = json.load(penis)
import discord
import os
from discord.ext import commands
PREFIX = data["prefix"]
rick = commands.Bot(command_prefix=PREFIX, self_bot=True)


@rick.event
async def on_ready():
	print('im in')


@rick.command()
async def start(ctx):
		i = 0
		isCreated = False
		msg = None
		while i < 4053:
			i = i + 3
			img = Image.open(f"frames/frame{i}.jpg")
			frame = generate_frame(img,60);
			if frame != None:
				if isCreated == False:
					msg = await ctx.send("```"+frame+"```"); os.system('cls' if os.name=='nt' else 'clear'); print(frame+"\n\n\nzerotwo n1")
					isCreated = True
					time.sleep(0.1)
				else:
					await msg.edit(content="```"+frame+"```"); os.system('cls' if os.name=='nt' else 'clear'); print(frame+"\n\n\nzerotwo n1")
					time.sleep(0.5)
					
		await ctx.send(".....................................................")
				


rick.run(data["token"], bot=False)
