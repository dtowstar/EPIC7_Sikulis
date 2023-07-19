#有等級制的關卡
screen1 = Region(Region(392,0,1144,659))
RunningGame = Region(Region(1214,540,322,122))

heroMaxRegion1 = Region(Region(733,516,112,74))
heroMaxRegion2 = Region(Region(928,526,97,47))
heroMaxRegion3 = Region(Region(971,530,210,115))

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

    if screen1.exists("1623204664737.png",15):
        screen1.hover(Pattern("1623204664737.png").targetOffset(-49,-9))
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)

        wait(3)
        if screen1.exists(Pattern("1623138308320-1.png").targetOffset(-57,31),15):
            screen1.hover(Pattern("1623138308320-1.png").targetOffset(-57,31))
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)

        if screen1.exists("1623138434812-1.png",15):
            screen1.click(Pattern("1623138434812-1.png").targetOffset(-43,-38))
            screen1.click(Pattern("1623138434812-1.png").targetOffset(-56,-1))
            screen1.click(Pattern("1623138434812-1.png").targetOffset(-57,34))
            screen1.click(Pattern("1623421120519-1.png").targetOffset(-224,83))
            screen1.click(Pattern("1623421120519-2.png").targetOffset(35,88))
        
    if screen1.exists(Pattern("1623636020832-1.png").similar(0.75),15):
        screen1.hover(Pattern("1623636020832-1.png").similar(0.75))
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)
         
    print("openHeroList")
def ChangeHero(InputeCheckCanPutRegioon):
    while not InputeCheckCanPutRegioon.exists("1605195761088-2.png",2):
        clickNextHero = screen1.find("1605195874461-3.png")
        screen1.click(Location(clickNextHero.x+100,clickNextHero.y+80))
        screen1.hover("1605195874461-3.png")
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)
        print("choseHero")

    wait(1)

    if InputeCheckCanPutRegioon.exists("1605195761088-2.png",1):
        InputeCheckCanPutRegioon.hover("1605195761088-2.png")
        InputeCheckCanPutRegioon.click("1605195761088-2.png")
        print("changeHero")

def rejectHeal():
    if screen1.exists(Pattern("1605426274746.png").targetOffset(-126,-6),1):
        screen1.hover(Pattern("1605426274746.png").targetOffset(-126,-6))
        wait(1)
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)

def getNewFriend():

    if screen1.exists("1641190817890.png",4):
        screen1.hover(Pattern("1641190829499.png").targetOffset(89,-6))
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)

def backageOpen():
    if screen1.exists("1647061081992.png",1):
        screen1.hover("1647061081992.png")
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

def Superior():
    if screen1.exists("1641192388787.png",10):
        screen1.hover("1641192388787.png")
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)

def Hell():
    if screen1.exists("1641193649311.png",10):
        screen1.hover("1641193649311.png")
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)

max1 = 0
max2 = 0
max3 = 0
OpenbackageOpen = 1
x = 0
y = 30

if screen1.exists("1622955228998-1.png",2):
    screen1.hover("1622955228998.png")
    screen1.mouseDown(Button.LEFT)
    wait(1)
    screen1.mouseUp(Button.LEFT)

#Hell()
Superior()

#if screen1.exists("1623045547554.png",10):
#    screen1.hover("1623045547554.png")
#    screen1.mouseDown(Button.LEFT)
#    wait(1)
#    screen1.mouseUp(Button.LEFT)

while x<y:
           
    if screen1.exists("1641187837656-2.png",10):
        wait(1)
        #定義friend的圖片x 和 y的平面軸，國中數學
        friend = screen1.find("1641187837656-2.png")
        wait(1)
        #點選 friend圖片的XY軸的X+70Y+220的像數點位置
        screen1.click(Location(friend.x+70,friend.y+270))
        
    if screen1.exists("1605178407940.png",5):
        screen1.hover("1605178407940.png")
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)
    
    if max1 == 1 or max2 == 2 or max3 == 5:
        
        openHeroList()
    
        if max1 == 1:
            ChangeHero(checkCanPutRegioon1)
            rejectHeal()
            print("ChangeHero1Success")
            max1 = 0
            wait(1)
        
        if max2 == 2:
            ChangeHero(checkCanPutRegioon2)
            rejectHeal()
            print("ChangeHero2Success")
            max2 = 0
            wait(1)
        
        if max3 == 3:
            ChangeHero(checkCanPutRegioon3)
            rejectHeal()
            print("ChangeHero3Success")
            max3 = 0
            wait(1)

    while not RunningGame.exists(Pattern("1641293336969-1.png").similar(0.50),1):
        
        if screen1.exists("1605180281291.png",3):
            wait(1)
            screen1.hover("1605180281291.png")
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)
        if screen1.exists("1641202127022.png",1):
            wait(1)
            screen1.hover(Pattern("1641202127022.png").targetOffset(83,-2))
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)

        if screen1.exists("1623225225288.png",1):
            wait(1)
            screen1.hover(Pattern("1623225225288.png").targetOffset(83,-5))
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)
    
        if screen1.exists("1623638672906.png",1):
            
            if OpenbackageOpen == 1:
                backageOpen()
            else:
                keyDown(Key.SHIFT) 
                keyDown(Key.ALT) 
                type("c")

    while 1:
        if screen1.exists("1641192829642.png",1):
            screen1.hover("1641192829642-1.png")
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)
            print("WIN")
            break

        if screen1.exists("1641193970814.png",1):
            screen1.hover("1641193970814.png")
            print("LOSE")
            break

    while not screen1.exists("1641187770939-2.png",1):
        getNewFriend()
        if screen1.exists("1641187669242.png",1):
            #checkQuantity = 1
            #max1 = CheckHero(heroMaxRegion1,checkQuantity)

            #checkQuantity = 2
            #max2 = CheckHero(heroMaxRegion2,checkQuantity)

            checkQuantity = 3
            max3 = CheckHero(heroMaxRegion3,checkQuantity)
            screen1.hover(Pattern("1641187669242-1.png").targetOffset(70,-2))
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)
            x += 1
        if screen1.exists("1641193204619.png",1):
            screen1.hover(Pattern("1641193204619.png").targetOffset(-117,-2))
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
        print("FindRepeat")
        print(x)
    










