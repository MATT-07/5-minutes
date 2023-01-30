import pyxel

pyxel.init(60*16, 20*16)
h = 320 
l = 960 #dimensions de la fenêtre
ymax = 216
ymin = 152 #coordonées maximales de déplacement
x,y = 22,22
lv1 = True
lv2 = False

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
    
    return x,y

def update():
    global x,y,ymin,ymax,lv1,lv2
    x,y = deplacement(x,y)
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw_lv1():
    global x,y,lv1,lv2,ymin,ymax
    if lv1 ==  True :
        pyxel.cls(0)
        pyxel.rect(x,y, 20, 20, 11)
        pyxel.line(0,ymin,l,ymin,6)
        pyxel.line(0,ymax+20,l,ymax+20,6)
        pyxel.line(64,0,64,h,6)

pyxel.run(update, draw_lv1)
