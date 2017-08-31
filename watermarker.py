from PIL import Image, ImageDraw, ImageFont, ImageChops
import textwrap

def place_trademark(im, trademark, font):
	draw = ImageDraw.Draw(im)
	bbox =  im.getbbox()
	W = bbox[2]
	H = bbox[3]
	draw.text(((W-800/2)/2, 1010), trademark, font=font)
	return im

def main():
	im_path = ("in/meme.jpg")
	wm_text = ("@drunkentimes")
	font = ImageFont.truetype('utils/BebasNeue.otf', 30)
	im = Image.open(im_path).resize((1080,1080))
	im = place_trademark(im, wm_text, font)
	im.show()

main()