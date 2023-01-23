import pyxel

pyxel.init(60*16, 20*16)

def deplacement(x,y):
    if pyxel.btn(pyxel.KEY_RIGHT):
        if x < 120:
            x = x + 2
    if pyxel.btn(pyxel.KEY_LEFT):
        if x > 0:
            x = x - 2
    if pyxel.btn(pyxel.KEY_UP):
        y = y+1
    
    return x,y

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw():
    pyxel.cls(0)
    pyxel.rect(10, 10, 20, 20, 11)

pyxel.run(update, draw)
