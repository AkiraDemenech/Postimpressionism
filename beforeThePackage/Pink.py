"""Primeiro filtro fovista"""
from scipy import misc
import time
pink = False
black = True    #   Verdadeiro para inverter o cinza-verde escuro
white = False   #   Falso para selecionar cores para modificação
fileout = False  #   Verdadeiro para não criar novo arquivo de saída

img = 'img\\matisse.jpg'
output = 'img\\matisse.png'
if(fileout):
    output = img

input = misc.imread(img)

l = input.shape[0]
c = input.shape[1]

if(not white):
    print('Róseo seletivo')
    if(black):
        print('Cinza-verde ativado')

print('\n\t' + img)
if(not fileout):
    print('\t' + output)
print('\n %d x %d [%d] \n' %(l, c, (l*c)))

start = time.time()
for x in range(l):
    for y in range(c):
        r, g, b = input[x,y]
        if(white or (abs(abs(b - g) - abs(r - g)) > 32)):
            if(g>0):
                pink = abs(abs(1 - r/g) - abs(1 - b/g)) > 1/11

            if(pink):
                r = r + g
                b = b + r//2
                if(b+r>0):
                    g = int(2*g/(b + r))
            else:
                gray = r + b
                if(gray==0):
                    gray = 1
                r2 = r + g
                g2 = g//gray
                b2 = (b + r)//2
                r = r2
                g = g2
                b = b2

            if(r>=256):
                r = 255
            if(b>=256):
                b = 255
            if(g>=256):
                g = 255
            input[x,y] = r, g, b

        elif(black):
            p = [int(r), int(g), int(b)]
            m = w = 1
            for z in p:
                if(m < z):
                    m = 1
            for z in range(3):
                if((r + g*2 + b)/4 < 192):
                    w = 1/(z + 1)
                else:
                    w = 2 - z/2
                p[z] = int((p[z]/m)**(w) * m)
            

            input[x,y] = p

t = time.time() - start
misc.imsave(output, input)
print('%f s \a' %t)
print('%d px \t\t %f px/s \t %f s/px' %(l*c, (l*c)/t, t/(l*c)))
print('%d ln \t\t %f ln/s \t %f s/ln' %(l, l/t, t/l))
print('%d col \t\t %f col/s \t %f s/col' %(c, c/t, t/c))