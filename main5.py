import pyxel

pyxel.init(60*16, 20*16)
h = 20*16 #320
l = 60*16 #960
hmax =
hmin =
x,y = 10,10

def deplacement(x,y):
    if pyxel.btn(pyxel.KEY_RIGHT):
        if x < h :
            x = x + 2
    if pyxel.btn(pyxel.KEY_LEFT):
        if x > 0:
            x = x - 2
    if pyxel.btn(pyxel.KEY_DOWN):
        if y < hmax:
        y = y+2
    if pyxel.btn(pyxel.KEY_UP):
        y = y-2
    
    return x,y

def update():
    global x,y
    x,y = deplacement(x,y)
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw():
    global x,y
    pyxel.cls(0)
    pyxel.rect(x,y, 20, 20, 11)

pyxel.run(update, draw)
