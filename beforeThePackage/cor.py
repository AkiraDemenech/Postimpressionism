""""""
from scipy import misc
import time

img = 'IMG-20200828-WA0022.'
output0 = img+'..png'
output1 = img+'...png'
img+='jpg'

input0 = misc.imread(img)
input1 = misc.imread(img)

l = input0.shape[0]
c = input1.shape[1]

print('\n %d x %d [%d] \n' %(l, c, (l*c)))

start = time.time()
for x in range(l):
	#print(x,end='\t')
	for y in range(c):
		zero = list(input0[x,y])
		um = list(input1[x,y])
		if x%2 == y%2:
			#verde no 0
			zero[0] = zero[2] = (zero[0] + zero[2])//2
		#	zero[0] = zero[2] = (int(zero[0]) + int(zero[2]))//2
			#cinza no 1
			um[0]=um[1]=um[2] = (um[0]+um[1]+um[1]+um[2])//4
		#	um[0]=um[1]=um[2] = (int(um[0])+int(um[1])+int(um[1])+int(um[2]))//4
		elif y%2 == 0:
			#vermelho no 0
			zero[1] = zero[2] = (zero[1] + zero[2])//2
		#	zero[1] = zero[2] = (int(zero[1]) + int(zero[2]))//2
			#verde no 1
			um[0] = um[2] = (um[0] + um[2])//2
		#	um[0] = um[2] = (int(um[0]) + int(um[2]))//2
		else:
			#azul no 0
			zero[1] = zero[0] = (zero[1] + zero[0])//2
		#	zero[1] = zero[0] = (int(zero[1]) + int(zero[0]))//2
			if x%2 == 0:
				#vermelho no 1
				um[1] = um[2] = (um[1] + um[2])//2
		#		um[1] = um[2] = (int(um[1]) + int(um[2]))//2
			else:
				#azul no 1
				um[1] = um[0] = (um[1] + um[0])//2
		#		um[1] = um[0] = (int(um[1]) + int(um[0]))//2
		input0[x,y] = zero
		input1[x,y] = um

t = time.time() - start
print('%f s \a' %t)
print('%d px \t\t %f px/s \t %f s/px' %(l*c, (l*c)/t, t/(l*c)))
print('%d ln \t\t %f ln/s \t %f s/ln' %(l, l/t, t/l))
print('%d col \t\t %f col/s \t %f s/col' %(c, c/t, t/c))
misc.imsave(output1, input1)
misc.imsave(output0, input0)
#time.sleep(11)

input0 = misc.imread(img)
input1 = misc.imread(img)

start = time.time()
for x in range(l):
	#print(x,end='\t')
	for y in range(c):
		zero = list(input0[x,y])
		um = list(input1[x,y])
		if x%2 == y%2:
			#verde no 0
			zero[0] = zero[2] = (int(zero[0]) + int(zero[2]))//2
			#cinza no 1
			um[0]=um[1]=um[2] = (int(um[0])+int(um[1])+int(um[1])+int(um[2]))//4
		elif y%2 == 0:
			#vermelho no 0
			zero[1] = zero[2] = (int(zero[1]) + int(zero[2]))//2
			#verde no 1
			um[0] = um[2] = (int(um[0]) + int(um[2]))//2
		else:
			#azul no 0
			zero[1] = zero[0] = (int(zero[1]) + int(zero[0]))//2
			if x%2 == 0:
				#vermelho no 1
				um[1] = um[2] = (int(um[1]) + int(um[2]))//2
			else:
				#azul no 1
				um[1] = um[0] = (int(um[1]) + int(um[0]))//2
		input0[x,y] = zero
		input1[x,y] = um

t = time.time() - start
print('%f s \a' %t)
print('%d px \t\t %f px/s \t %f s/px' %(l*c, (l*c)/t, t/(l*c)))
print('%d ln \t\t %f ln/s \t %f s/ln' %(l, l/t, t/l))
print('%d col \t\t %f col/s \t %f s/col' %(c, c/t, t/c))

misc.imsave(output1+'.png', input1)
misc.imsave(output0+'.png', input0)