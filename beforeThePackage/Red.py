
from postimpressionism import imsave,show
import random
from numpy import empty, uint8

	
ln = 768
col = 1366
delta = 16
output = 'GERAçãO.pNG'
redonly = empty((ln,col,3),uint8)
redlike = empty((ln,col,3),uint8)

def variar	(of,var = delta,lim=256,t=uint8):
	return t(of + (var*random.random()*(1-((random.random() < 0.5)*2))))%lim
	
red = 256*random.random()
for y in range(ln):
	for x in range(col):
		if x:
			red = redonly[y,x-1,0]
			if y:
				red = (red + redonly[y-1,x,0] + redonly[y-1,x-1,0])/3
		elif y:
			red = redonly[y-1,x,0]
		red = variar(red)
		redonly[y,x] = redlike[y,x] = red,red,red
		red *= random.random() > 0.5
		if random.random() > 0.5:	
			if random.random() > 0.5:	
				red = uint8(red*random.random())
			redonly[y,x,2] = redonly[y,x,1] = redlike[y,x,1] = red
			redlike[y,x,2] = uint8(red*random.random())	

		
	print(y,end='')


		
show(redlike)
show(redonly)
imsave(redonly,'0'+output)
imsave(redlike,'1'+output)