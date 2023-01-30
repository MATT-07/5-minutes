import pyxel

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

pyxel.run(update, draw_lv1)
