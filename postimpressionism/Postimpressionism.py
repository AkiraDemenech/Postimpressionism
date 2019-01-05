"""This module implements the peculiar (or those that try to be it) methods of Image Processing"""


try:
	print("Importing...", end="")	# Here we start
	from postimpressionism.Getimpressionism import *	# and then everything begin
except ModuleNotFoundError:
	from Getimpressionism import *	# solving some problems sometimes
	print("Finished", end='!')
else:
	print("The end", end='')		# to finish briefly

def channel (img, ch, gray = False):
	"""Isolating the color channels of an image"""
	img = imopen(img)
	ch = int(ch)

	for x in range(img.shape[0]):
		for y in range(img.shape[1]):
			for c in range(3):
				if(c!=ch):
					if(gray):
						img[x, y][c] = img[x, y][ch]
					else:
						img[x, y][c] = 0
	
	return img

def gradient (img, grad = True, redshift = False, lightblue = False, xgreen = False, grayfirst = False, greengray = True):
	"""Sorting all the image's pixels"""
	img = imopen(img)
	px = []
	
	for x in range(img.shape[0]):
		for y in range(img.shape[1]):
			
			r, g, b = img[x, y]

			p = [r, g, b]

			if(xgreen):
				p = [r, b, g]

			if(lightblue):
				p.reverse()

			if(grayfirst):
				gray = r + int(g) + b
				div = 3
				if(greengray):
					div = 4
					gray += g
				gray /= div
				p = [gray] + p

			px.append(p)
	
	if(grad):
		px.sort()

	if(not redshift):
		px.reverse()
	
	for c in range(len(px)):
		
		if(grayfirst):
			px[c] = px[c][1:]

		if(lightblue):
			px[c].reverse()

		if(xgreen):
			r, b, g = px[c]
			px[c] = [r, g, b]

	return px

def dada (img):
	"""Randomizing the positions of all pixels in the image"""
	img = imopen(img)
	
	ln = img.shape[0]
	col = img.shape[1]

	for x in range(ln):
		for y in range(col):
			img[x, y] = img[x + int(random()*(ln-x)), y + int(random()*(col-y))]

	return img

def purple (img, qtd=1, res=[]):
	"""HSV transforming to magenta, blue and red the pixels"""
	if qtd>1:
		i = 1
		res.append (img)
		while i < qtd:
			img = purple (img, res=res)
			print (str(i) + (('st', 'nd', 'rd')[i-1], 'th')[i>=3] + " image")
			i += 1

	img = imopen(img)
	res.append(img)
	for x in range(img.shape[0]):
		for y in range(img.shape[1]):
			h, s, v = convert(*img[x,y])
			h = (2 + h)/3
			img[x, y] = convert (h, s, v, True)
	return img

def pink (img, black = True, white = False, qtd=1, res=[]):	#The Fauvist Filter is here
	"""RGB transforming to pink, purple, blue and red the pixels as a Fauvist [filter]"""
	if qtd>1:
		img = pink (img, black, white, qtd-1, res)
	else:
		res.append(img)
	
	img = imopen(img)
	res.append (img)
	l = img.shape[0]
	c = img.shape[1]

	print ('\t\t>>>' + str(qtd))
	if(not white):
		print('Róseo seletivo')
		if(black):
			print('Cinza-verde ativado')

	pink = True

	for x in range(l):
		for y in range(c):
			r, g, b = img[x,y]
					#	RuntimeWarning: overflow encountered in ubyte_scalars
						# Maior variação entre as variações dos canais Vermelho e Azul com o Verde
			if(white or (abs(abs(b - g) - abs(r - g)) > 32)):
				if(g>0):
					pink = abs(abs(1 - r/g) - abs(1 - b/g)) > 1/11
							# Maior discrepância entre as razões dos outros canais com o G

				if(pink):
					r += g
					b += r//2
					if(b+r>0):
						g = int(2*g/(b + r))
						
				else:
					gray = r + b
					if(gray==0):
						gray = 1

					r2 = r + g
					g2 = g//gray
					b2 = (gray)//2

					r = r2
					g = g2
					b = b2

				if(r>=256):
					r = 255
				if(b>=256):
					b = 255
				if(g>=256):
					g = 255
				img[x,y] = r, g, b

			elif(black):
				p = [int(r), int(g), int(b)]
				w = 1
				for z in range(3):
					if((r + g*2 + b)/4 < 192):	# mais escuro
						w = 1/(z + 1) #	quanto mais Azul, mais será reduzido	[1, 1/2, 1/3]
					else:
						w = 2 - z/2	#	quanto mais Azul, menos será aumentado	[2, 1.5, 1]
					p[z] **= w	# proporção por exponenciação

				img[x,y] = p	

	return img

def strip (img, *gargs):
	"""Antidiagonal pixel sorting"""
	if(img.__class__ == str):
		img = imopen(img)
	
	pixels = report(gradient, img, *gargs)
	
	down = True
	into = False
	
	x = y = 0

	for p in pixels:

		img[x, y] = p

		if(not into):

			if((x==0 or x==img.shape[0]-1) and y<img.shape[1]-1):
				y += 1
			else:
				x += 1

			down = (x==0 or y==img.shape[1]-1)
			into = True

		else:
			if(down):
				x += 1
				y -= 1
			else:
				x -= 1
				y += 1
			
			into = not ((x==0 or y==0 or x==img.shape[0]-1 or y==img.shape[1]-1))

	return img

#def vortex (img, *gargs):
#	"""Em breve...."""
#	img = imopen(img)
#	
#	pixels = report(gradient, img, *gargs)


	# The End 
print('?\n')