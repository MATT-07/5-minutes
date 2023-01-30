import pyxel

pyxel.init(60*16, 20*16)
h = 320 
l = 960 #dimensions de la fenêtre
ymax = 216
ymin = 152 #coordonées maximales et minimales de déplacement
x,y = 22,22 #coordonnées du personnage
niveau = 1 #variable pour savoir dans quel niveau on se trouve

def deplacement(x,y):
    if pyxel.btn(pyxel.KEY_RIGHT):
        if x < l and y >= ymin :
            x = x + 2
    if pyxel.btn(pyxel.KEY_LEFT):
        if x > 0 and y >= ymin :
            x = x - 2
    if pyxel.btn(pyxel.KEY_DOWN):
        if y < ymax:
            y = y+2
    if pyxel.btn(pyxel.KEY_UP):
        if y > ymin :
            y = y-2
    
    return x,y #fonction de déplacement avec les flèches du clavier à l'intérieur des coordonnées de déplacement

def update():
    global x,y,ymin,ymax,niveau
    x,y = deplacement(x,y) #fonction de mise à jour des coordonnées du personnage en fonction des touches appuyées, à l'aide de la fonction deplacement

def draw(): #
    global x,y,niveau,ymin,ymax
    if niveau ==  1 :
        pyxel.cls(0)
        pyxel.line(0,ymin,l,ymin,6)
        pyxel.line(0,ymax+20,l,ymax+20,6)
        pyxel.line(64,0,64,h,6) #limites de déplacement et couloir de sortie de la salle de classe
    pyxel.rect(x,y, 20, 20, 11)

pyxel.run(update, draw) 


===============================================================================================================================================================

import pyxel
import random

pyxel.init(60*16, 20*16)
h = 20*16 #320
l = 60*16 #960
hmax =184+16+16
hmin =136+16
x,y = 22,22
lv1 = True
lv2 = False

def deplacement(x,y):
    if pyxel.btn(pyxel.KEY_RIGHT):
        if x < l and y >= hmin :
            x = x + 2
    if pyxel.btn(pyxel.KEY_LEFT):
        if x > 0 and y >= hmin :
            x = x - 2
    if pyxel.btn(pyxel.KEY_DOWN):
        if y < hmax:
            y = y+2
    if pyxel.btn(pyxel.KEY_UP):
        if y > hmin :
            y = y-2
   

    return x,y
    #Piege quand il passe a 64*8 il y a  30% de chance de perdre
    if x == 64*8:
        for i in range (1,2):
            m = random()
            if m<0.3:
               pyxel.quit() 
            
 /////////////////////////////
    if x == 64*8:

     m = random()
            if m<0.3:
               pyxel.quit() 
            

def update():
    global x,y,hmin,hmax,lv1,lv2
    x,y = deplacement(x,y)
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw_lv1():
    global x,y,lv1,lv2,hmin,hmax
    if lv1 ==  True :
        pyxel.cls(0)
        pyxel.rect(x,y, 20, 20, 11)
        pyxel.line(0,hmin,l,hmin,6)
        pyxel.line(0,hmax+20,l,hmax+20,6)
        pyxel.line(64,0,64,h,6)
        pyxel.line(64*8,0,64*8,h,6)
                #Bloc ennemi
        pyxel.rect(20*6,hmax-20, 16, 16, 9)
        pyxel.rect(20*7,hmax, 16, 16, 9)
        pyxel.rect(20*7,hmax-1*20, 16, 16, 9)
        pyxel.rect(20*7,hmax-2*20, 16, 16, 9)
        pyxel.rect(20*8,hmax-1*20, 16, 16, 9)
        pyxel.rect(20*9,hmax-3*20, 16, 16, 9)
        pyxel.rect(20*9,hmax-1*20, 16, 16, 9)
        pyxel.rect(20*10,hmax-0*20, 16, 16, 9)
        pyxel.rect(20*11,hmax-2*20, 16, 16, 9)
        pyxel.rect(20*11,hmax-3*20, 16, 16, 9)
        pyxel.rect(20*11,hmax-0*20, 16, 16, 9)
        pyxel.rect(20*12,hmax-0*20, 16, 16, 9)
        pyxel.rect(20*13,hmax-2*20, 16, 16, 9)
        pyxel.rect(20*14,hmax-2*20, 16, 16, 9)
        pyxel.rect(20*14,hmax-1*20, 16, 16, 9)
        pyxel.rect(20*15,hmax-3*20, 16, 16, 9)
        pyxel.rect(20*16,hmax-0*20, 16, 16, 9)
        pyxel.rect(20*16,hmax-1*20, 16, 16, 9)
        pyxel.rect(20*17,hmax-3*20, 16, 16, 9)
        pyxel.rect(20*17,hmax-1*20, 16, 16, 9)
        pyxel.rect(20*18,hmax-0*20, 16, 16, 9)
        pyxel.rect(20*19,hmax-1*20, 16, 16, 9)
        pyxel.rect(20*19,hmax-2*20, 16, 16, 9)
        pyxel.rect(20*19,hmax-1*20, 16, 16, 9)






pyxel.run(update, draw_lv1)
