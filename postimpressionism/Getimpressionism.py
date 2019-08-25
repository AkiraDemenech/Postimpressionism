"""This module implements the main basic methods to Image Processing."""
try:
	from postimpressionism.Setimpressionism import *
except ModuleNotFoundError:
	from Setimpressionism import *
	#	If I am testing from the directory . . .

img_path = "C:\\"
def _path_ (p = None):
	"""Setter and Getter for default path to the image files"""
	global img_path; #Python reserved word and where to find them
	if(p.__class__() != str):
		return img_path

	img_path = p

def show (img, title=''):
	"""Image output from matplotlib.pyplot"""
	if(img.__class__ == str):
		if(title==''):
			title = img
		img = imopen(input) 
	plot.imshow(img)
	plot.title(title)
	plot.show()

def imsave (image, name):
	"""Image file is saved"""
	image = imopen(image)
	im.fromarray(image).save(name)

def imopen (image, noalpha = True):
	"""Image open from system file"""
	if(image.__class__ == str):
		image = im.open(image)

	if(image.__class__ != array):
		image = asarray(image)
		image.setflags(write=1)

	if(noalpha and image.shape[2]>3):
		return image[:,:,0:3]
	else:
		image = image.copy()
	return image

def convert (a, b, c, is_hsv=False):
	"""Convert RGB and HSV"""
	if is_hsv:
		a = list(hsv_to_rgb(a,b,c))
		for c in range(3):
			a[c] = int(255*a[c])
		return a
	
	return list (rgb_to_hsv (a/255, b/255, c/255))

	# We finally finished the basic things.
print("\tAll basic\tmethods imported.")