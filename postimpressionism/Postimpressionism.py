"""This module implements the peculiar (or those that try to be it) methods of Image Processing"""
try:
	print("Importing...", end="")	# Here we start
	from postimpressionism.Getimpressionism import *	# and then everything begin
except ModuleNotFoundError:
	from Getimpressionism import *	# solving some problems sometimes
	print("Finished", end='!')
else:
	print("The end", end='')		# to finish briefly

def channels (img, *ch):
	"""Permuting the color channels of an image"""
	if len(ch)==1:
		ch = ch*3
	img = imopen(img)
	for x in range(img.shape[0]):
		for y in range(img.shape[1]):
			#b = []
			#for c in ch:
			#	b.append (img[x,y][c])
			img[x, y] = img[x,y][ch[0]], img[x,y][ch[1]], img[x,y][ch[2]] #b
	return img

def sort (img, redshift=True):
	"""Sorting the color channels of an image"""
	img = imopen(img)
	for x in range(img.shape[0]):
		for y in range(img.shape[1]):
			a = list(img[x, y])
			a.sort()
			if redshift:
				a.reverse()
			img[x, y] = a
	return img

def neg (img, once=True):
	"""Negative of the image, possibly sorting the bigger channels (once=False)"""
	img = imopen(img)
	for x in range(img.shape[0]):
		for y in range(img.shape[1]):
			a = list(img[x, y])
			c = len(a)
			while c > 0:
				c -= 1
				a[c] = 255 - a[c]
			if once:
				img[x, y] = a
				continue
			c = len(a)
			b = c*[0]
			while c > 0:
				c -= 1
				d = len(a)
				while d > 0:
					d -= 1
					b[c] += a[d] > a[c]
			c = len(a)
			a.sort()
			while c > 0:
				c -= 1
				b[c] = a[b[c]]
			img[x, y] = b
	return img

def gradient (img, grad = True, redshift = False, lightblue = False, xgreen = False, grayfirst = False, greengray = True, hsvbased = False):
	"""Sorting all the image's pixels"""
	img = imopen(img)
	px = []
	
	for x in range(img.shape[0]):
		for y in range(img.shape[1]):
			
			r, g, b = img[x, y]
			if(hsvbased):
				r, g, b = convert (r,g,b)

			p = [r, g, b]

			if(xgreen):
				p = [r, b, g]

			if(lightblue):
				p.reverse()

			if(grayfirst):
				gray = r + g + b
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

		if(hsvbased):
			px[c] = convert(*px[c],True)

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
			n = time ()
			img = purple (img, res=res)
			print (str(i) + ('st','nd','rd', 'th')[[i-1, 3][i>3]] + " image == " + str (time() - n) + ' s')
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
		global pink
		img = pink(img, black, white, qtd-1, res)
	else:
		res.append (img)
	
	img = imopen(img)
	res.append(img)
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
	img = imopen(img)
	
	
	
	down = True
	into = False
	
	x = y = 0

	for p in gradient (img, *gargs):

		img[x, y] = p



		if into:
			if(down):
				x += 1
				y -= 1
			else:
				x -= 1
				y += 1
			
			into = not ((x==0 or y==0 or x==img.shape[0]-1 or y==img.shape[1]-1))

		else:

			if((x==0 or x==img.shape[0]-1) and y<img.shape[1]-1):
				y += 1
			else:
				x += 1

			down = (x==0 or y==img.shape[1]-1)
			into = True

	return img

def spiral (img, clockwise=True, *gargs):
	"""Rectangle vortex pixel sorting"""
	img = imopen(img)
	
	v = x = y = 0
	dx = clockwise
	dy = not dx
	

	for p in gradient (img, *gargs):

		img[x, y] = p
		

		if x == img.shape[0]-dx-v:
			dx = 0
			dy = (2*clockwise) - 1
		elif y == img.shape[1]-dy-v:
			dx = 1 - (2*clockwise) 
			dy = 0
		elif x == v and dx<0:
			dx = 0
			dy = 1 - (2*clockwise)
			v += clockwise
		elif y == v and dy<0:
			dx = (2*clockwise) - 1
			dy = 0
			v += not clockwise

		x += dx
		y += dy
	return img

def tv_noise (img, operation = add, inv_op = sub, id = 0):
	"""An strange manipulation"""
	img = imopen(img)


	for x in range(img.shape[0]):
		for y in range(img.shape[1]):
			t = id 
			for c in img[x][y]: 
				t = operation(c,t)
			img[x][y] = [inv_op(t,c)%256 for c in img[x][y]]	
	return img		


	

	# The End 
print('?\n')