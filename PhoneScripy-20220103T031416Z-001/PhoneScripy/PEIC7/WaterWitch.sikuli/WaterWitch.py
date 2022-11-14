#火討罰
screen1 = Region(Region(392,0,1144,659))
RunningGame = Region(Region(1214,540,322,122))

def rejectHeal():
    if screen1.exists(Pattern("1605426274746-2.png").targetOffset(-126,-6),1):
        screen1.hover(Pattern("1605426274746-2.png").targetOffset(-126,-6))
        wait(1)
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)

def fire11():
    if screen1.exists("1641387563465.png",10):
        screen1.hover(Pattern("1641387563465.png").targetOffset(-149,-2))
        wait(1)
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)

def water12():
    if screen1.exists("1641391202236.png",10):
        screen1.hover(Pattern("1641391202236.png").targetOffset(-176,-20))
        wait(1)
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)

def water13():
    if screen1.exists("1641387586664.png",10):
        screen1.hover(Pattern("1641387586664.png").targetOffset(-129,2))
        wait(1)
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)
x = 0
y = 30
loseT = 0
if screen1.exists("1641387639229.png",10):
    screen1.hover("1641387639229.png")
    Firedragon11 = screen1.find("1641387639229.png")
        
    screen1.dragDrop(Location(Firedragon11.x-200,Firedragon11.y+300),Location(Firedragon11.x-200,Firedragon11.y))

wait(1)

water13()

if screen1.exists(Pattern("1641275531396.png").similar(0.86),5):
    wait(1)
    screen1.hover(Pattern("1641275531396.png").similar(0.86))
    wait(1)
    screen1.mouseDown(Button.LEFT)
    wait(1)
    screen1.mouseUp(Button.LEFT)
    wait(7)

while x<y:

    while not RunningGame.exists(Pattern("1641293336969-2.png").similar(0.50),1):
        if screen1.exists("1641291842762-2.png",1):
            wait(1)
            screen1.hover("1641291842762-2.png")
            screen1.mouseDown(Button.LEFT)
            wait(1)
        if screen1.exists("1641202127022-1.png",1):
            wait(1)
            screen1.hover(Pattern("1641202127022-1.png").targetOffset(83,-2))
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

            loseT += 1
            
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
        











