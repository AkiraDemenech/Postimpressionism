
from postimpressionism import imsave,show
from random import random
from numpy import empty

	
ln = 768
col = 1366
delta = 16
output = 'GERAçãO.pNG'
redonly = empty((ln,col,3),int)
redlike = empty((ln,col,3),int)

def variar	(of,var = delta,lim=256,t=int):
	return t(of + var*random()*(1-((random() < 0.5)*2)))%lim
	
red = 256*random()
for y in range(ln):
	for x in range(col):
		if x:
			red = redonly[y,x-1,0]
			if y:
				red += redonly[y-1,x,0]# + redonly[y-1,x-1,0]
				red /= 2
		elif y:
			red = redonly[y-1,x,0]
		red = redonly[y,x,0] = redlike[y,x,0] = variar(red)
		red = redonly[y,x,2] = redonly[y,x,1] = redlike[y,x,1] = int(red*random())
		redlike[y,x,2] = int(red*random())
		
	print(y)


		
show(redlike)
show(redonly)
imsave(redonly,'0'+output)
imsave(redlike,'1'+output)
#C:\Users\Guilherme A D Mori\Documents\GitHub\Postimpressionism\beforeThePackage