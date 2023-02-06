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
niveau = 1
casier = 0

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

            
 #/////////////////////////////
    #if x == 64*8:

     #m = random.randint(1,3)
      #      if m == 3:
       #        pyxel.rect(5,hmax-1*20, 16, 16, 9) 
            


def update():
    global x,y,hmin,hmax,niveau,casier
    x,y = deplacement(x,y)
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw_lv1():
    global x,y,niveau,hmin,hmax,casier
    if niveau ==  1 :
        
        pyxel.cls(0)
        if 64*8-2 <= x <= 64*8+2:
            for i in range (1,2):
                m = random.randint(1,3)
                if m == 3:
                    pyxel.rect(5,5, 50, 50, 5)
                    casier = 1
        if casier == 1 :
            pyxel.rect(5,5, 50, 50, 5)
            
            
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



















------------------------------------------------------------------------------------------------------------------------------------------------
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
def arriver(wcx1, wcx2, wcy1, wcy2, jx, jy, niveau):
    """
    fonction qui permet de definir le point d arriver 
    
    >>> arriver(100, 150, 20, 30, 145, 25, 1)
    2
    
    >>> arriver(100, 150, 20, 30, 90, 25, 1)
    1
    
    >>> arriver(100, 150, 20, 30, 100, 25, 1)
    1
    
    >>> arriver(100, 150, 20, 30, 150, 25, 1)
    1
    
    >>> arriver(100, 150, 20, 30, 160, 25, 1)
    1
    
    >>> arriver(100, 150, 20, 30, 145, 10, 1)
    1
    
    >>> arriver(100, 150, 20, 30, 145, 20, 1)
    1
    
    >>> arriver(100, 150, 20, 30, 145, 30, 1)
    1
    
    >>> arriver(100, 150, 20, 30, 145, 35, 1)
    1
    """
    if jx > wcx1 and jx < wcx2 and jy > wcy1 and jy < wcy2:
        return niveau+1
    else:
        return niveau

def update():
    global x,y,ymin,ymax,niveau,l
    x,y = deplacement(x,y) #fonction de mise à jour des coordonnées du personnage en fonction des touches appuyées, à l'aide de la fonction deplacement
    niveau = arriver(l-22, l-18, ymin, ymax+20, x, y, niveau)
    
def draw(): #
    global x,y,niveau,ymin,ymax
    pyxel.cls(0)
    if niveau ==  1 :
        pyxel.line(0,ymin,l,ymin,6)
        pyxel.line(0,ymax+20,l,ymax+20,6)
        pyxel.line(64,0,64,h,6) #limites de déplacement et couloir de sortie de la salle de classe
    elif niveau ==  2 :
        pyxel.line(0,ymin,l,ymin,7)
        pyxel.line(0,ymax+20,l,ymax+20,7)
        pyxel.line(120,0,120,h,7) #limites de déplacement et couloir de sortie de la salle de classe
    pyxel.rect(x,y, 20, 20, 11)

pyxel.run(update, draw) 
