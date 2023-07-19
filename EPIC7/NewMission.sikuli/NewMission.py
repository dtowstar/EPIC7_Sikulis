
screen1 = Region(Region(0,7,1536,757))

def buyEnergy():
    if screen1.exists(Pattern("1689134726303.png").similar(0.60),2):
        screen1.hover(Pattern("1689134726303.png").targetOffset(94,6))
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)

x = 0
y = 20
loseT = 0
if screen1.exists("1689503554015.png",8):
    screen1.hover(Pattern("1689503554015.png").targetOffset(-182,-17))
    wait(1)
    screen1.mouseDown(Button.LEFT)
    wait(1)
    screen1.mouseUp(Button.LEFT)
    

if screen1.exists("1689131996004.png",5):
    screen1.hover("1689131996004.png")
    screen1.mouseDown(Button.LEFT)
    wait(1)
    screen1.mouseUp(Button.LEFT)
    wait(5)

while x<y:

    while not screen1.exists("1689472779124.png",5):
        if screen1.exists("1689132091224.png",5):
            screen1.hover("1689132091224.png")
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)
        if screen1.exists(Pattern("1689134726303.png").similar(0.60),2):
            buyEnergy()
            wait(3) 

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

    while not screen1.exists("1689132644633.png",1):
        wait(1)
        if screen1.exists("1689132605369.png",1):
            screen1.hover(Pattern("1689132605369.png").targetOffset(59,7))
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)

            
#        screen1.doubleClick(Location(screen1.x+500,screen1.y+200))
            
    if screen1.exists("1689132644633.png",5):
        screen1.hover("1689132644633.png")
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)
        wait(1)
        buyEnergy()
        print("win")
        print(x)
        print("lose")
        print(loseT)
        











