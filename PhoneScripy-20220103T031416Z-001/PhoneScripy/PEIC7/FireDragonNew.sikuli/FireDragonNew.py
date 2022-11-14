#火討罰
screen1 = Region(Region(394,0,1142,658))
RunningGame = Region(Region(1211,559,325,98))

def rejectHeal():
    if screen1.exists(Pattern("1605426274746-2.png").targetOffset(-126,-6),1):
        screen1.hover(Pattern("1605426274746-2.png").targetOffset(-126,-6))
        wait(1)
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)

def fire11():
    if screen1.exists("1641295676393.png",10):
        screen1.hover(Pattern("1641295676393.png").targetOffset(-169,-18))
        wait(1)
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)
        
def fire13():
    if screen1.exists("1641295699613.png",10):
        screen1.hover(Pattern("1641295699613.png").targetOffset(-148,-34))
        wait(1)
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)
x = 0
y = 3
loseT = 0
if screen1.exists("1641295730822.png",10):
    screen1.hover("1641295730822.png")
    Firedragon11 = screen1.find("1641295730822.png")
        
    screen1.dragDrop(Location(Firedragon11.x-200,Firedragon11.y+300),Location(Firedragon11.x-200,Firedragon11.y))

wait(1)

fire13()

if screen1.exists(Pattern("1641275531396.png").similar(0.86),5):
    wait(1)
    screen1.hover(Pattern("1641275531396.png").similar(0.86))
    wait(1)
    screen1.mouseDown(Button.LEFT)
    wait(1)
    screen1.mouseUp(Button.LEFT)
    wait(5)

while x<y:

    while not RunningGame.exists(Pattern("1647604818216.png").similar(0.65),1):
        wait(1)
        if screen1.exists("1605180281291.png",2):
            screen1.hover(Pattern("1605180281291.png").targetOffset(10,0))
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)
        if screen1.exists("1641202127022.png",1):
            wait(1)
            screen1.hover(Pattern("1641202127022.png").targetOffset(83,-2))
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)

    while 1:
        if screen1.exists("1641192829642.png",1):
            screen1.hover("1641192829642-1.png")
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)
            x += 1
            break

        if screen1.exists("1641193970814.png",1):
            screen1.hover("1641193970814.png")
            loseT = loseT+1
            break

    wait(5)

    while not screen1.exists("1641187770939-2.png",1):
        wait(1)
        if screen1.exists("1641187669242.png",1):
            screen1.hover(Pattern("1641187669242-1.png").targetOffset(70,-2))
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)
        if screen1.exists("1641310163806.png",1):
            screen1.hover(Pattern("1641310163806.png").targetOffset(-101,-6))
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)
            
        screen1.doubleClick(Location(screen1.x+500,screen1.y+200))
            
    if screen1.exists("1641187770939-1.png",5):
        screen1.hover(Pattern("1641187770939-1.png").targetOffset(2,-1))
        wait(1)
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)
        wait(1)
        print("win")
        print(x)
        print("lose")
        print(loseT)
        











