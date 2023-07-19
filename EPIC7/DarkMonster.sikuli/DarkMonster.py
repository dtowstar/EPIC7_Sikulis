screen1 = Region(Region(392,0,1144,659))
RunningGame = Region(Region(1214,540,322,122))

heroMaxRegion1 = Region(Region(733,516,112,74))
heroMaxRegion2 = Region(Region(928,526,97,47))
heroMaxRegion3 = Region(Region(1099,526,102,49))

checkCanPutRegioon1 = Region(Region(787,330,128,100))
checkCanPutRegioon2 = Region(Region(786,196,114,107))
checkCanPutRegioon3 = Region(Region(682,277,110,92))

def CheckHero(CheckHaveMaxheroRegion,inputCheckQuantity):
    if CheckHaveMaxheroRegion.exists(Pattern("1623137887756.png").similar(0.60),3):
        CheckHaveMaxheroRegion.hover(Pattern("1623137887756.png").similar(0.60))
        print("HaveMax")
        return inputCheckQuantity
        
    else :
        print("NoMax")
        return 0

def openHeroList():

    if screen1.exists(Pattern("1623636020832.png").similar(0.75),15):
        screen1.hover(Pattern("1623636020832.png").similar(0.75))
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)

        wait(3)
        if screen1.exists(Pattern("1623138308320.png").targetOffset(-57,31),15):
            screen1.hover(Pattern("1623138308320.png").targetOffset(-57,31))
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)

        if screen1.exists("1623138434812.png",15):
            screen1.click(Pattern("1623138434812.png").targetOffset(-43,-38))
            screen1.click(Pattern("1623138434812.png").targetOffset(-56,-1))
            screen1.click(Pattern("1623138434812.png").targetOffset(-57,34))
            screen1.click(Pattern("1623421120519-1.png").targetOffset(-224,83))
            screen1.click(Pattern("1623403414833-1.png").targetOffset(-50,193))
        
    if screen1.exists(Pattern("1623636020832-1.png").similar(0.75),15):
        screen1.hover(Pattern("1623636020832-1.png").similar(0.75))
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)
         
    print("openHeroList")

def ChangeHero(InputeCheckCanPutRegioon):
    while not InputeCheckCanPutRegioon.exists("1605195761088-1.png",2):
        clickNextHero = screen1.find("1605195874461-2.png")
        screen1.click(Location(clickNextHero.x+100,clickNextHero.y+80))
        screen1.hover("1605195874461-2.png")
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)
        print("choseHero")

    wait(1)

    if InputeCheckCanPutRegioon.exists("1605195761088-1.png",1):
        InputeCheckCanPutRegioon.hover("1605195761088-1.png")
        InputeCheckCanPutRegioon.click("1605195761088-1.png")
        print("changeHero")
        
def backageOpen():
    if screen1.exists(Pattern("1623536070702.png").targetOffset(7,80),5):
        screen1.hover(Pattern("1623536070702.png").targetOffset(7,80))
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)

    wait(1)

    if screen1.exists("1623637381518-1.png",2):
        keyDown(Key.SHIFT) 
        keyDown(Key.ALT) 
        type("c")

    if screen1.exists("1623536192720.png",5):
        screen1.hover(Pattern("1623536192720.png").targetOffset(127,21))
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)

    if screen1.exists("1623536281956.png",5):
        screen1.hover(Pattern("1623536281956.png").targetOffset(3,25))
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)
    
    wait(2)
    if screen1.exists("1623536495859.png",5):
        screen1.hover(Pattern("1623536495859.png").targetOffset(49,-19))
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)

    if screen1.exists("1623536554710.png",5):
        screen1.hover(Pattern("1623536554710.png").targetOffset(60,21))
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)

    if screen1.exists("1623536605975.png",5):
        screen1.hover(Pattern("1623536605975.png").targetOffset(84,-2))
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)

    if screen1.exists("1623536676002.png",5):
        screen1.hover(Pattern("1623536676002.png").targetOffset(-74,15))
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)

def rejectHeal():
    if screen1.exists(Pattern("1605426274746-1.png").targetOffset(-126,-6),1):
        screen1.hover(Pattern("1605426274746-1.png").targetOffset(-126,-6))
        wait(1)
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)

def dark11():
    if screen1.exists("1641275432883.png",10):
        screen1.hover(Pattern("1641275432883.png").targetOffset(-126,7))
        wait(1)
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)
        
def dark13():
    if screen1.exists("1641275459954.png",10):
        screen1.hover(Pattern("1641275459954.png").targetOffset(-159,-2))
        wait(1)
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)
        
max1 = 0
max2 = 0
max3 = 0
OpenbackageOpen = 0
x = 0
y = 50
loseT = 0

if screen1.exists("1641275351986.png",10):
    screen1.hover("1641275351986.png")
    tree11 = screen1.find("1641275351986.png")
        
    screen1.dragDrop(Location(tree11.x-200,tree11.y+300),Location(tree11.x-200,tree11.y))

wait(1)

dark13()
        
if screen1.exists(Pattern("1641275531396.png").similar(0.86),5):
    wait(1)
    screen1.hover(Pattern("1641275531396.png").similar(0.86))
    wait(1)
    screen1.mouseDown(Button.LEFT)
    wait(1)
    screen1.mouseUp(Button.LEFT)
    wait(7)

while x<y:
    
    if max1 == 1:
        
        openHeroList()

        if max1 == 1:
            ChangeHero(checkCanPutRegioon1)
            print("ChangeHero1Success")
            rejectHeal()
            max1 = 0

    while not RunningGame.exists(Pattern("1641293336969-2.png").similar(0.50),1):
        if screen1.exists("1641291842762-1.png",1):
            wait(1)
            screen1.hover("1641291842762-1.png")
            screen1.mouseDown(Button.LEFT)
            wait(1)
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
            loseT += 1
            break

    wait(5)
    
    while not screen1.exists("1641187770939-3.png",1):
        wait(1)
        if screen1.exists("1641187669242-2.png",1):
            screen1.hover(Pattern("1641187669242-3.png").targetOffset(70,-2))
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










