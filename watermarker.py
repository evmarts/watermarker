from PIL import Image, ImageDraw, ImageFont, ImageChops
import textwrap

def place_trademark(im, trademark, font, wm_loc_num):
	draw = ImageDraw.Draw(im)
	bbox =  im.getbbox()
	w, h = draw.textsize(trademark, font=font)
	W = bbox[2]
	H = bbox[3]
	buf = W / 6

	if wm_loc_num == "1":
		wm_loc = ((0 - w)/2 + buf ,(0-h)/2 + buf)
	if wm_loc_num == "2":
		wm_loc = ((W - w)/2 , (0-h)/2 + buf)
	if wm_loc_num == "3":
		wm_loc = ((W - w) - buf/2 , (0-h)/2 + buf)
	if wm_loc_num == "4":
		wm_loc = ((0 - w)/2 + buf, (H - h)/2)
	if wm_loc_num == "5":
		wm_loc = ((W - w)/2, (H - h)/2)
	if wm_loc_num == "6":
		wm_loc = ((W - w) - buf/2 , (H - h)/2)
	if wm_loc_num == "7":
		wm_loc = ((0 - w)/2 + buf ,(H-h/2) - buf)
	if wm_loc_num == "8":
		wm_loc = ((W - w)/2 , (H-h/2) - buf)
	if wm_loc_num == "9":
		wm_loc = ((W - w) - buf/2 ,(H-h/2) - buf)
	draw.text(wm_loc, trademark, font=font)
	return im

def get_wm_loc_num():
	print "Enter a location to place the watermark on the image: (1-9)"
	interface = "  locations: \n  1 | 2 | 3 \n ----------- \n  4 | 5 | 6 \n ----------- \n  7 | 8 | 9 "
	print interface
	wm_loc_num = raw_input()
	return wm_loc_num

def main():
	while True:
		try:
			im_path = "in/" + raw_input("Enter image path: in/")
			im = Image.open(im_path)
			im = im.convert("RGB")
		except:
			print "file does not exist!"
			continue
		break

	wm_text = raw_input("Enter watermark text: ")
	wm_loc_num = get_wm_loc_num()

	# hardcoded for debugging
	# wm_text = "hey there"
	# wm_loc_num = "5"
	# im_path = "in/meme.jpg"

	W = im.getbbox()[2]
	font_size = int(W * 0.03)
	font = ImageFont.truetype('utils/HelveticaNeue.dfont', font_size)
	im = place_trademark(im, wm_text, font, wm_loc_num)
	im.save("out/meme.jpg")
	print "Watermark added!"

main()