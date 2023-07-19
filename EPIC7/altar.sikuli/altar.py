#任意一種屬性祭壇
screen1 = Region(Region(472,0,1064,620))
RunningGame = Region(Region(1218,0,318,136))

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
        if screen1.exists(Pattern("1623138308320-1.png").targetOffset(-57,31),15):
            screen1.hover(Pattern("1623138308320-1.png").targetOffset(-57,31))
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)

        if screen1.exists("1623138434812-1.png",15):
            screen1.click(Pattern("1623138434812-1.png").targetOffset(-43,-38))
            screen1.click(Pattern("1623138434812-1.png").targetOffset(-56,-1))
            screen1.click(Pattern("1623138434812-1.png").targetOffset(-57,34))
            screen1.click(Pattern("1624826714500.png").targetOffset(-272,88))
            screen1.click(Pattern("1624826714500.png").targetOffset(0,88))
        
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

    if screen1.exists("1607060339692.png",4):
        screen1.hover(Pattern("1622956597097.png").targetOffset(87,2))
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)

max1 = 0
max2 = 0
max3 = 0
x = 0
y = 10
        
if screen1.exists("1624171027188.png",5):
    screen1.hover("1624171027188.png")
    screen1.mouseDown(Button.LEFT)
    wait(1)
    screen1.mouseUp(Button.LEFT)

while x<y:
    
    
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
    
    print("rt")
    wait(1)

    if screen1.exists("1624679206376-1.png",5):
        screen1.hover(Pattern("1624679206376-1.png").targetOffset(-8,9))
        wait(1)
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)
        print("battleStart")
    
    while not screen1.exists(Pattern("1623471600171.png").similar(0.60),1):

        print("loading")
        if screen1.exists("1624679206376.png",1):
            screen1.hover(Pattern("1624679206376.png").targetOffset(-8,9))
            wait(1)
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)
            print("battleStart")

        if screen1.exists("1623638672906.png",1):
            keyDown(Key.SHIFT) 
            keyDown(Key.ALT) 
            type("c")
            
        if screen1.exists("1623074049702.png",1):
            wait(1)
            screen1.hover(Pattern("1623074049702.png").targetOffset(72,-2))
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)
        
        if screen1.exists("1623225225288.png",1):
            wait(1)
            screen1.hover(Pattern("1623225225288.png").targetOffset(83,-5))
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)

    while 1:
        print("waiting")
        if screen1.exists("1607009569477.png",1):
            screen1.hover("1607009569477-1.png")
            wait(1)
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)
            break

        if screen1.exists("1623046022621.png",1):
            screen1.hover("1623046022621.png")
            break
    while not screen1.exists(Pattern("1623046080154.png").similar(0.80),1):
        
        if screen1.exists("1622969756982.png",1):
            checkQuantity = 1
            max1 = CheckHero(heroMaxRegion1,checkQuantity)

            checkQuantity = 2
            max2 = CheckHero(heroMaxRegion2,checkQuantity)

#            checkQuantity = 3
#            max3 = CheckHero(heroMaxRegion3,checkQuantity)
            screen1.hover(Pattern("1622969756982.png").targetOffset(49,0))
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)
            x += 1
        if screen1.exists(Pattern("1623070541310.png").targetOffset(-95,-6),1):
            screen1.hover(Pattern("1623070541310.png").targetOffset(-95,-6))
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)
            
        screen1.doubleClick(Location(screen1.x+500,screen1.y+200))
            
    if screen1.exists(Pattern("1623046080154.png").similar(0.80),5):
        screen1.hover(Pattern("1623046080154.png").similar(0.80))
        wait(1)
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)
        print("FindRepeat")
        print(x)

    










