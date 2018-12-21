"""
isto não é um script
"""
from scipy import misc
from random import random
from matplotlib import pyplot as plot


img = 'fonte.jpg'
output = 'fonte.png'
img = misc.imread(img)

ln = img.shape[0]
col = img.shape[1]
for x in range(ln):
	for y in range(col):
		#if(random()>0.5):
		#if(random()<0.5):  
		#if(random()*(img.shape[0]+img.shape[1])>(x+y)):
		#if(random()*(img.shape[0]+img.shape[1])<(x+y)):
			#img[x, y] = img[int(random()*(x+1)), int(random()*(y+1))]
		img[x, y] = img[x + int(random()*(ln-x)), y + int(random()*(col-y))]
			#img[x, y] = img[int(random()*img.shape[0]), int(random()*img.shape[1])]
			#img[x, y] = img[int(random()*img.shape[0]), int(random()*img.shape[1])]

#misc.imsave(output, img)
plot.imshow(img)
plot.title('Dada Image')
plot.show()