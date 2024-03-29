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
