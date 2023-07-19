#火討罰
screen1 = Region(Region(0,7,1536,757))

def fire11():
    if screen1.exists("1641295676393.png",10):
        screen1.hover(Pattern("1641295676393.png").targetOffset(-169,-18))
        wait(1)
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)
        
def fire13():
    if screen1.exists("1689155476449.png",10):
        screen1.hover(Pattern("1689155476449.png").targetOffset(-166,-6))
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)

def Tesrdrop():
    if screen1.exists("1641295730822.png",10):
        screen1.hover("1641295730822.png")
        Firedragon11 = screen1.find("1641295730822.png")
            
        screen1.dragDrop(Location(Firedragon11.x-200,Firedragon11.y+300),Location(Firedragon11.x-200,Firedragon11.y))

def buyEnergy():
    if screen1.exists("1689134726303-2.png",2):
        screen1.hover("1689134726303-2.png")
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)

x = 0
y = 20
loseT = 0

fire13()

if screen1.exists(Pattern("1689156253306.png").targetOffset(16,39),5):
    wait(1)
    screen1.hover(Pattern("1689156253306.png").targetOffset(16,39))
    wait(1)
    screen1.mouseDown(Button.LEFT)
    wait(1)
    screen1.mouseUp(Button.LEFT)
    wait(3)

while x<y:

    while not screen1.exists(Pattern("1689156465416.png").similar(0.60),1):
        wait(1)
        if screen1.exists("1689156405086.png",2):
            screen1.hover("1689156405086.png")
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)
            
        buyEnergy()

    while 1:
        if screen1.exists("1689132570769.png",1):
            screen1.hover("1689132570769.png")
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)
            x += 1
            break

        if screen1.exists("1689135172102.png",1):
            screen1.hover("1689135172102.png")
            loseT = loseT+1
            break
    wait(3)

    while not screen1.exists("1689156859585.png",1):
        wait(1)
        if screen1.exists("1689156825016.png",1):
            screen1.hover(Pattern("1689156825016.png").targetOffset(71,-4))
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)
        if screen1.exists("1689156690371.png",1):
            screen1.hover(Pattern("1689156690371.png").targetOffset(-110,-4))
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)
            
        screen1.doubleClick(Location(screen1.x+500,screen1.y+200))
            
    if screen1.exists("1689156859585.png",5):
        screen1.hover("1689156859585.png")
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)
        wait(1)
        print("win")
        print(x)
        print("lose")
        print(loseT)
        











