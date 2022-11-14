screen1 = Region(Region(389,0,1147,655))
RunningGame = Region(Region(1231,558,305,116))

heroMaxRegion1 = Region(Region(733,516,112,74))
heroMaxRegion2 = Region(Region(928,526,97,47))
heroMaxRegion3 = Region(Region(976,530,212,121))


checkCanPutRegioon1 = Region(Region(787,330,128,100))
checkCanPutRegioon2 = Region(Region(786,196,114,107))
checkCanPutRegioon3 = Region(Region(682,277,110,92))
EastRegion = Region(Region(1358,175,122,109))
SouthRegion = Region(Region(1355,382,116,114))
WestRegion = Region(Region(525,379,146,120))
NorthRegion = Region(Region(531,175,151,119))

def getNewFriend():

    if screen1.exists("1641190817890.png",4):
        screen1.hover(Pattern("1641190829499.png").targetOffset(89,-6))
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
def openHeroList():

    if screen1.exists("1646793161591.png",15):
        screen1.hover(Pattern("1646793161591.png").targetOffset(-47,-8))
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)

        wait(3)
        if screen1.exists("1646793218134.png",15):
            screen1.hover(Pattern("1646793218134.png").targetOffset(-70,40))
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)

        if screen1.exists("1623138434812-2.png",15):
            screen1.click(Pattern("1623138434812-2.png").targetOffset(-43,-38))
            screen1.click(Pattern("1623138434812-2.png").targetOffset(-56,-1))
            screen1.click(Pattern("1623138434812-2.png").targetOffset(-57,34))
            screen1.click(Pattern("1623421120519-1.png").targetOffset(-224,83))
            screen1.click(Pattern("1623421120519-2.png").targetOffset(35,88))
        
    if screen1.exists(Pattern("1623636020832-2.png").similar(0.75),15):
        screen1.hover(Pattern("1623636020832-2.png").similar(0.75))
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)
         
    print("openHeroList")
def CheckHero(CheckHaveMaxheroRegion,inputCheckQuantity):
    if CheckHaveMaxheroRegion.exists(Pattern("1623137887756.png").similar(0.60),3):
        CheckHaveMaxheroRegion.hover(Pattern("1623137887756.png").similar(0.60))
        print("HaveMax")
        return inputCheckQuantity
        
    else :
        print("NoMax")
        return 0

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
    if screen1.exists(Pattern("1623536070702-1.png").targetOffset(7,80),5):
        screen1.hover(Pattern("1623536070702-1.png").targetOffset(7,80))
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)
        print("op")

    wait(1)

    if screen1.exists("1623637381518.png",2):
        keyDown(Key.SHIFT) 
        keyDown(Key.ALT) 
        type("c")

    if screen1.exists("1623536192720-1.png",5):
        screen1.hover(Pattern("1623536192720-1.png").targetOffset(127,21))
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)

    if screen1.exists("1623536281956-1.png",5):
        screen1.hover(Pattern("1623536281956-1.png").targetOffset(3,25))
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)
    
    wait(2)
    if screen1.exists("1623536495859-1.png",5):
        screen1.hover(Pattern("1623536495859-1.png").targetOffset(49,-19))
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)

    if screen1.exists("1623536554710-1.png",5):
        screen1.hover(Pattern("1623536554710-1.png").targetOffset(60,21))
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)

    if screen1.exists("1623536605975-1.png",5):
        screen1.hover(Pattern("1623536605975-1.png").targetOffset(84,-2))
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)

    if screen1.exists("1623536676002-1.png",5):
        screen1.hover(Pattern("1623536676002-1.png").targetOffset(-74,15))
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)

openHeroList()
