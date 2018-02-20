from PIL import Image, ImageDraw, ImageFont, ImageChops
import os
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

# determine is the given path is an image
def is_img(path):
	ext = path[-4:]
	if (ext == ".jpg") or (ext == ".png") or (ext == "jpeg"):
		return True
	return False

# gets the paths of the images to be used
def get_im_paths(files):
	pic_paths = []
	for file in files:
		if is_img(file):
			pic_paths.append(file)
	return pic_paths

def main():
	dir_paths = os.listdir("../watermarker/in")
	im_paths = get_im_paths(dir_paths)
	wm_text = raw_input("Enter watermark text: ")
	wm_loc_num = get_wm_loc_num()

	for im_path in im_paths:
		im = Image.open("../watermarker/in/" + str(im_path))
		im = im.convert("RGB")

		W = im.getbbox()[2]
		font_size = int(W * 0.03)
		font = ImageFont.truetype('utils/HelveticaNeue.dfont', font_size)
		im = place_trademark(im, wm_text, font, wm_loc_num)
		im.save("out/" + str(im_path))
		print "Watermark added!"

main()