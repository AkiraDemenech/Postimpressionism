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

def methodTime (met, tsec=None):
	"""The Great Method Chronometer"""

	try:
		met = met.__name__ 
	except AttributeError:
		pass

	try:
		f = open(arq, "r")
		lines = f.read()
		if (not met in lines and not tsec):
			f.close()
			return []
		lines = lines.split()
		m = []
		
		if(tsec):
			f.close()
			f = open(arq, "w")
		
		for ln in lines:
			
			if(met in ln): 

				n = ln.split(':')[1].split(';')
				
				for c in range(len(n)):
					n[c] = float(n[c])
				
				if(not tsec):
					f.close()
					return n
				else:
					m = n + [tsec]
					ln += ';' + str(tsec)
			if(tsec):
				f.write(ln + '\n')
		if(tsec and len(m)==0):
			f.write(met + ':' + str(tsec))
		f.close()
		return m

	except FileNotFoundError:
		open('__pycache__\\method.log', "w").close()
		return methodTime(met, tsec)

def report (met, *args, exp=True):
	"""The Great Method Eficiency Reporter"""

	image = args[0]
	
	if(image.__class__ == str):
		image = imopen(image)

	ln = image.shape[0]
	col = image.shape[1]
	px = ln*col

	print('\n\t %d x %d \t [%d]' %(ln, col, px))

	if(exp):
		t = 0
		temp = methodTime(met)
		for c in temp:
			t += c
		try:
			t /= len(temp)
			print('\t\t ~%fs \t [%f px/s or %f s/px]' %(px/t, t, 1/t))
		except ZeroDivisionError:
			pass

	start = time()
	result = met(*args)
	t = time() - start

	print('\n\t %f s \a\n' %t)
	methodTime(met, px/t)
	print('%d px\t\t %f px/s \t %f s/px' %(px, px/t, t/px))
	print('%d ln  \t\t %f ln/s \t %f s/ln' %(ln, ln/t, t/ln))
	print('%d col \t\t %f col/s \t %f s/col' %(col, col/t, t/col))

	return result

	# We finally finished the basic things.
print("\tAll basic\tmethods imported.")