import pyxel
import random

pyxel.init(60 * 16, 20 * 16)
h = 320
l = 960  # dimensions de la fenêtre
hmax = 216
hmin = 152  # coordonées maximales et minimales de déplacement
x, y = 22, 22  # coordonnées du personnage
niveau = 1  # variable pour savoir dans quel niveau on se trouve
arrive = False
trentièmes = 30
secondes = 59
minutes = 1
casier = 0
m = 0

def deplacement(x, y):
    if pyxel.btn(pyxel.KEY_RIGHT):
        if x < l and y >= hmin:
            x = x + 2
    if pyxel.btn(pyxel.KEY_LEFT):
        if x > 0 and y >= hmin:
            x = x - 2
    if pyxel.btn(pyxel.KEY_DOWN):
        if y < hmax:
            y = y + 2
    if pyxel.btn(pyxel.KEY_UP):
        if y > hmin:
            y = y - 2

    return x, y  # fonction de déplacement avec les flèches du clavier à l'intérieur des coordonnées de déplacement


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
        return True

def update():
    global x, y, hmin, hmax, niveau, l, arrive, trentièmes, secondes, minutes
    x, y = deplacement(x, y)  # fonction de mise à jour des coordonnées du personnage en fonction des touches appuyées, à l'aide de la fonction deplacement
    arrive = arriver(l - 22, l - 18, hmin, hmax + 20, x, y, niveau)
    if arrive == True:
        niveau+=1
        x,y = 22, 180
    #chronomètre
    trentièmes -= 1
    if trentièmes == 0:
        secondes -= 1
        trentièmes = 30

    if secondes == 0:
        minutes -= 1
        secondes = 59

def draw():  #
    global x, y, niveau, hmin, hmax, trentièmes, secondes, minutes, casier, m, niveau
    pyxel.cls(0)
    #chronomètre
    if minutes >= 0 :
        pyxel.text(150, 32, "Timer : "+ str(minutes)+":"+ str(secondes), 8)
    else : 
        pyxel.cls(0)
        pyxel.text(60*16/2, 20*16/2,"GAME OVER :(", 8)
    
    #affichage nb niveau
    pyxel.text(5,250,"Niveau :"+str(niveau), 4)
    
    #Personnage
    pyxel.rect(x,y, 20, 20, 11)
    pyxel.rect(x+19,y, 1, 1, 8) #un pixel a chaque angle pour faciliter les collisions
    pyxel.rect(x+19,y+19, 1, 1, 8)
    pyxel.rect(x,y+19, 1, 1, 8)
        
    if niveau == 1:
        
        if 64*8-2 <= x <= 64*8+2: #Piege quand il passe a 64*8 il y a  30% de chance de perdre
            m = random.randint(1,3)
            if m == 3: #choisit un nombre entre 1 et 3, si il est égal à 3, éxecute cette boucle, il y a donc 1/3 de chances qu'elle soit éxécutée
                pyxel.rect(5,5,50,50,5)
        
    #Limites de déplacement et couloir de sortie de la salle de classe
        pyxel.line(0,hmin,l,hmin,6)
        pyxel.line(0,hmax+20,l,hmax+20,6)
        pyxel.line(64,0,64,h,6)
        pyxel.line(64*8,0,64*8,h,6) 
        
        #obstacle niveau 1
        pyxel.rect(20 * 6, hmax - 20, 16, 16, 9)
        pyxel.rect(20 * 7, hmax, 16, 16, 9)
        pyxel.rect(20 * 7, hmax - 1 * 20, 16, 16, 9)
        pyxel.rect(20 * 7, hmax - 2 * 20, 16, 16, 9)
        pyxel.rect(20 * 8, hmax - 1 * 20, 16, 16, 9)
        pyxel.rect(20 * 9, hmax - 3 * 20, 16, 16, 9)
        pyxel.rect(20 * 9, hmax - 1 * 20, 16, 16, 9)
        pyxel.rect(20 * 10, hmax - 0 * 20, 16, 16, 9)
        pyxel.rect(20 * 11, hmax - 2 * 20, 16, 16, 9)
        pyxel.rect(20 * 11, hmax - 3 * 20, 16, 16, 9)
        pyxel.rect(20 * 11, hmax - 0 * 20, 16, 16, 9)
        pyxel.rect(20 * 12, hmax - 0 * 20, 16, 16, 9)
        pyxel.rect(20 * 13, hmax - 2 * 20, 16, 16, 9)
        pyxel.rect(20 * 14, hmax - 2 * 20, 16, 16, 9)
        pyxel.rect(20 * 14, hmax - 1 * 20, 16, 16, 9)
        pyxel.rect(20 * 15, hmax - 3 * 20, 16, 16, 9)
        pyxel.rect(20 * 16, hmax - 0 * 20, 16, 16, 9)
        pyxel.rect(20 * 16, hmax - 1 * 20, 16, 16, 9)
        pyxel.rect(20 * 17, hmax - 3 * 20, 16, 16, 9)
        pyxel.rect(20 * 17, hmax - 1 * 20, 16, 16, 9)
        pyxel.rect(20 * 18, hmax - 0 * 20, 16, 16, 9)
        pyxel.rect(20 * 19, hmax - 1 * 20, 16, 16, 9)
        pyxel.rect(20 * 19, hmax - 2 * 20, 16, 16, 9)
        pyxel.rect(20 * 19, hmax - 1 * 20, 16, 16, 9)
    elif niveau == 2:
        pyxel.line(0, hmin, l, hmin, 7)
        pyxel.line(0, hmax + 20, l, hmax + 20, 7)
    elif niveau == 3:
            pyxel.line(0, hmin, l, hmin, 10)
            pyxel.line(0, hmax + 20, l, hmax + 20, 10)
                
    

pyxel.run(update, draw)
