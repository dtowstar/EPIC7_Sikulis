#9-4狗糧迷宮
screen1 = Region(Region(472,0,1064,620))
RunningGame = Region(Region(1214,0,322,131))

heroMaxRegion1 = Region(Region(733,516,112,74))
heroMaxRegion2 = Region(Region(928,526,97,47))
heroMaxRegion3 = Region(Region(1099,526,102,49))

checkCanPutRegioon1 = Region(Region(787,330,128,100))
checkCanPutRegioon2 = Region(Region(786,196,114,107))
checkCanPutRegioon3 = Region(Region(682,277,110,92))
EastRegion = Region(Region(1358,175,122,109))
SouthRegion = Region(Region(1355,382,116,114))
WestRegion = Region(Region(525,379,146,120))
NorthRegion = Region(Region(531,175,151,119))

max1 = 0
max2 = 0
max3 = 0
OpenbackageOpen = 1
x = 0
y = 13

def CheckHero(CheckHaveMaxheroRegion,inputCheckQuantity):
    if CheckHaveMaxheroRegion.exists(Pattern("1623137887756-1.png").similar(0.60),3):
        CheckHaveMaxheroRegion.hover(Pattern("1623137887756-1.png").similar(0.60))
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

        wait(2)
        if screen1.exists(Pattern("1623138308320-2.png").targetOffset(-57,31),15):
            screen1.hover(Pattern("1623138308320-2.png").targetOffset(-57,31))
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)

        if screen1.exists("1623138434812-2.png",15):
#            screen1.click(Pattern("1623138434812-2.png").targetOffset(-43,-38))
            screen1.click(Pattern("1623138434812-2.png").targetOffset(-56,-1))
            screen1.click(Pattern("1623138434812-2.png").targetOffset(-57,34))
            screen1.click(Pattern("1623421120519-2.png").targetOffset(-224,83))
            screen1.click(Pattern("1623421120519-3.png").targetOffset(35,88))
        
    if screen1.exists(Pattern("1623636020832.png").similar(0.75),15):
        screen1.hover(Pattern("1623636020832.png").similar(0.75))
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)
         
    print("openHeroList")
def ChangeHero(InputeCheckCanPutRegioon):
    while not InputeCheckCanPutRegioon.exists("1605195761088-3.png",2):
        clickNextHero = screen1.find("1605195874461-4.png")
        screen1.click(Location(clickNextHero.x+100,clickNextHero.y+80))
        screen1.hover("1605195874461-4.png")
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)
        print("choseHero")

    wait(1)

    if InputeCheckCanPutRegioon.exists("1605195761088-3.png",1):
        InputeCheckCanPutRegioon.hover("1605195761088-3.png")
        InputeCheckCanPutRegioon.click("1605195761088-3.png")
        print("changeHero")

def rejectHeal():
    if screen1.exists(Pattern("1605426274746-1.png").targetOffset(-126,-6),1):
        screen1.hover(Pattern("1605426274746-1.png").targetOffset(-126,-6))
        wait(1)
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)

def backageOpen():
    if screen1.exists(Pattern("1623536070702.png").targetOffset(7,80),5):
        screen1.hover(Pattern("1623536070702.png").targetOffset(7,80))
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)
        print("op")

    wait(1)

    if screen1.exists("1623637381518.png",2):
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

def getNewFriend():

    if screen1.exists("1607060339692-1.png",4):
        screen1.hover(Pattern("1622956597097-1.png").targetOffset(87,2))
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)

while x<y:

    if screen1.exists("1622955228998-1.png",2):
        screen1.hover("1622955228998-1.png")
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)
    if screen1.exists(Pattern("1606397270517-2.png").similar(0.60),15):
        wait(1)
        friend = screen1.find(Pattern("1606397270517-3.png").similar(0.60))
        wait(1)
        screen1.click(Location(friend.x+70,friend.y+220))
        
    if screen1.exists("1605178407940-1.png",5):
        screen1.hover("1605178407940-1.png")
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)
    
    if max1 == 1 or max2 == 2 or max3 == 3:
        
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

    while not RunningGame.exists(Pattern("1623149594846-1.png").similar(0.50),1):
        if screen1.exists("1605180281291-1.png",1):
            wait(1)
            screen1.hover("1605180281291-1.png")
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)
            print("battleStart")

        if screen1.exists("1623638672906.png",1):
            if OpenbackageOpen == 1:
                backageOpen()
            else:
                keyDown(Key.SHIFT) 
                keyDown(Key.ALT) 
                type("c")

        if screen1.exists("1623074049702-1.png",1):
            wait(1)
            screen1.hover(Pattern("1623074049702-1.png").targetOffset(72,-2))
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)

        if screen1.exists("1623225225288-1.png",1):
            wait(1)
            screen1.hover(Pattern("1623225225288-1.png").targetOffset(83,-5))
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)

    if WestRegion.exists("1623475083146-1.png",90):
        print("openMap")
        wait(1)
        if screen1.exists("1623479363685.png",90):
            screen1.hover("1623479363685.png")
            wait(1)
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)  

    if screen1.exists("1623479414537.png",90):
        wait(1)
        screen1.hover("1623479414537.png")
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)

    if screen1.exists("1623475793115.png",90):
        wait(1)
        screen1.hover(Pattern("1623475793115.png").targetOffset(89,94))
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)

    wait(10)

    if EastRegion.exists("1623474584315.png",90):
        wait(1)
        EastRegion.hover("1623474584315.png")
        EastRegion.mouseDown(Button.LEFT)
        wait(1)
        EastRegion.mouseUp(Button.LEFT)   

    wait(10)

    if NorthRegion.exists("1623474788286.png",90):
        wait(1)
        NorthRegion.hover("1623474788286.png")
        NorthRegion.mouseDown(Button.LEFT)
        wait(1)
        NorthRegion.mouseUp(Button.LEFT) 

    wait(10)

    if EastRegion.exists("1623474584315.png",90):
        wait(1)
        EastRegion.hover("1623474584315.png")
        EastRegion.mouseDown(Button.LEFT)
        wait(1)
        EastRegion.mouseUp(Button.LEFT)   

    wait(10)

    if NorthRegion.exists("1623474788286.png",90):
        wait(1)
        NorthRegion.hover("1623474788286.png")
        NorthRegion.mouseDown(Button.LEFT)
        wait(1)
        NorthRegion.mouseUp(Button.LEFT) 

    wait(10)

    if EastRegion.exists("1623474584315.png",90):
        wait(1)
        EastRegion.hover("1623474584315.png")
        EastRegion.mouseDown(Button.LEFT)
        wait(1)
        EastRegion.mouseUp(Button.LEFT)   

    wait(10)

    if SouthRegion.exists("1623475368132.png",90):
        wait(1)
        SouthRegion.hover("1623475368132.png")
        SouthRegion.mouseDown(Button.LEFT)
        wait(1)
        SouthRegion.mouseUp(Button.LEFT)

    wait(10)

    if EastRegion.exists("1623474584315.png",90):
        wait(1)
        screen1.hover(Pattern("1623480467502.png").targetOffset(-10,-63))
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)  

    wait(2)

    if screen1.exists("1623480526122.png",90):
        wait(1)
        screen1.hover(Pattern("1623480526122.png").targetOffset(-76,5))
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)

    if screen1.exists("1623475793115.png",90):
        wait(1)
        screen1.hover(Pattern("1623475793115.png").targetOffset(89,94))
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)

    if screen1.exists("1623475848173.png",90):
        wait(1)
        screen1.hover("1623475848173.png")
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)

    if screen1.exists("1623475875274.png",90):
        wait(1)
        screen1.hover(Pattern("1623475875274.png").targetOffset(79,88))
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)

    while 1:
        if screen1.exists("1607009569477-2.png",1):
            screen1.hover("1607009569477-3.png")
            wait(1)
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)
            getNewFriend()
            break

        if screen1.exists("1623046022621-1.png",1):
            screen1.hover("1623046022621-1.png")
            break

        
    while not screen1.exists("1622955228998-1.png",1):
        
        if screen1.exists("1622969756982-1.png",1):
            checkQuantity = 1
            max1 = CheckHero(heroMaxRegion1,checkQuantity)

            checkQuantity = 2
            max2 = CheckHero(heroMaxRegion2,checkQuantity)

            checkQuantity = 3
            max3 = CheckHero(heroMaxRegion3,checkQuantity)
            screen1.hover(Pattern("1622969756982-1.png").targetOffset(49,0))
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)
            x += 1
            print(x)
        if screen1.exists(Pattern("1623070541310-1.png").targetOffset(-95,-6),1):
            screen1.hover(Pattern("1623070541310-1.png").targetOffset(-95,-6))
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)
            
        screen1.doubleClick(Location(screen1.x+500,screen1.y+200))








