screen1 = Region(Region(521,0,1015,602))
needToCompositeHero = Region(Region(930,277,233,54))

heroMaxRegion1 = Region(Region(794,506,101,83))
heroMaxRegion2 = Region(Region(965,504,107,57))
heroMaxRegion3 = Region(Region(1138,503,106,72))

repeatRegion = Region(Region(1252,490,284,121))

checkCanPutRegioon1 = Region(Region(856,327,73,80))
checkCanPutRegioon2 = Region(Region(851,203,69,78))
checkCanPutRegioon3 = Region(Region(744,286,74,70))

max1 = 0
max2 = 0
max3 = 0
x = 0
y = 40

def CheckHero(CheckHaveMaxheroRegion,inputCheckQuantity):
    if CheckHaveMaxheroRegion.exists("1606480846033.png",3):
        CheckHaveMaxheroRegion.hover("1606480846033.png")
        print("HaveMax")
        return inputCheckQuantity
        
    else :
        print("NoMax")
        return 0

def openHeroList():

    if screen1.exists("1605193259437-3.png",15):
        screen1.hover("1605193259437-3.png")
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)

        wait(3)
        
        type("t")
        screen1.click(Pattern("1606588669117.png").similar(0.85).targetOffset(-88,-1))

        screen1.click(Pattern("1605195121180-2.png").targetOffset(-94,-2))
        wait(1)
        screen1.click(Pattern("1605195168770-2.png").targetOffset(-103,1))
        screen1.click(Pattern("1605230195846-2.png").similar(0.60))
        screen1.click(Pattern("1605193543041-3.png").similar(0.60).targetOffset(-70,-1))
        
        screen1.hover("1605193259437-3.png")
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

if screen1.exists("1606453807369.png",10):
    screen1.hover("1606453807369.png")
    screen1.mouseDown(Button.LEFT)
    wait(1)
    screen1.mouseUp(Button.LEFT)

#if screen1.exists(Pattern("1608355081726.png").similar(0.85),3):
#    screen1.hover(Pattern("1608355081726.png").similar(0.85))
#    screen1.mouseDown(Button.LEFT)
#    wait(1)
#    screen1.mouseUp(Button.LEFT)
#if screen1.exists(Pattern("1605237399963.png").similar(0.80),3):
#    screen1.hover(Pattern("1605237399963-1.png").similar(0.80))
#    screen1.mouseDown(Button.LEFT)
#    wait(1)
#    screen1.mouseUp(Button.LEFT)

#if screen1.exists("1605886539515.png",3):
#    screen1.hover("1605886539515.png")
#    screen1.mouseDown(Button.LEFT)
#    wait(1)
#    screen1.mouseUp(Button.LEFT)

if screen1.exists(Pattern("1605234637320.png").similar(0.75),3):
    screen1.hover(Pattern("1605234637320.png").similar(0.75))
    screen1.mouseDown(Button.LEFT)
    wait(1)
    screen1.mouseUp(Button.LEFT) 

while x<y:
    
    if screen1.exists("1606397270517.png",15):
        wait(1)
        friend = screen1.find("1606397270517-1.png")
        screen1.click(Location(friend.x+70,friend.y+220))
    
    if screen1.exists("1605178407940.png",5):
        screen1.hover("1605178407940.png")
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)
    
    if max1 == 1 or max2 == 2 or max3 == 3:
        
        openHeroList()
    
    if max1 == 1:
        ChangeHero(checkCanPutRegioon1)
        print("ChangeHero1Success")
        if screen1.exists(Pattern("1605426274746.png").targetOffset(-126,-6),1):
            screen1.hover(Pattern("1605426274746.png").targetOffset(-126,-6))
            wait(1)
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)
        max1 = 0
        wait(1)
    
    if max2 == 2:
        ChangeHero(checkCanPutRegioon2)
        if screen1.exists(Pattern("1605426274746.png").targetOffset(-126,-6),1):
            screen1.hover(Pattern("1605426274746.png").targetOffset(-126,-6))
            wait(1)
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)
        print("ChangeHero2Success")
        max2 = 0
        wait(1)
    
    if max3 == 3:
        ChangeHero(checkCanPutRegioon3)
        if screen1.exists(Pattern("1605426274746.png").targetOffset(-126,-6),1):
            screen1.hover(Pattern("1605426274746.png").targetOffset(-126,-6))
            wait(1)
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)
        print("ChangeHero3Success")
        max3 = 0
        wait(1)
    
    if screen1.exists("1605180281291.png",15):
        wait(1)
        screen1.hover("1605180281291.png")
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)
        
#    if screen1.exists("1605236293742.png",2):
#        keyDown(Key.SHIFT) 
#        keyDown(Key.ALT) 
#        type("c")

    if screen1.exists("1606456408543.png",2):   
        keyDown(Key.SHIFT) 
        keyDown(Key.ALT) 
        type("c")
        if needToCompositeHero.exists(Pattern("1606456593665-2.png").similar(0.95),1):
            if needToCompositeHero.exists(Pattern("1606456593665-2.png").similar(0.95),1):
                print("Start")
        
                if screen1.exists(Pattern("1606456429944.png").targetOffset(0,-2),2):
                    screen1.hover(Pattern("1606456429944.png").targetOffset(0,-2))
                    screen1.mouseDown(Button.LEFT)
                    wait(1)
                    screen1.mouseUp(Button.LEFT)
    
                    wait(3)
                    
                    if screen1.exists(Pattern("1606456853561-2.png").similar(0.80),5):
                        screen1.hover(Pattern("1606456853561-2.png").similar(0.80))
                        screen1.mouseDown(Button.LEFT)
                        wait(1)
                        screen1.mouseUp(Button.LEFT)
            
                        wait(3)
                        keyDown(Key.SHIFT) 
                        keyDown(Key.ALT) 
                        type("c")
                        print("handCompositeHero")
        
        
        if screen1.exists(Pattern("1606456429944.png").targetOffset(0,-2),2):
            screen1.hover(Pattern("1606456429944.png").targetOffset(0,-2))
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)
    
            if screen1.exists("1606488119985-1.png",5):
                screen1.hover(Pattern("1606488119985-1.png").targetOffset(-1,26))
                screen1.mouseDown(Button.LEFT)
                wait(1)
                screen1.mouseUp(Button.LEFT)
    
                if screen1.exists(Pattern("1607743625370.png").targetOffset(134,25),2):
                    screen1.hover(Pattern("1607743625370-1.png").targetOffset(134,25))
                    screen1.mouseDown(Button.LEFT)
                    wait(1)
                    screen1.mouseUp(Button.LEFT)
    
                    if screen1.exists(Pattern("1606488196381-1.png").targetOffset(-4,22),2):
                        screen1.hover(Pattern("1606488196381-1.png").targetOffset(-4,22))
                        screen1.mouseDown(Button.LEFT)
                        wait(1)
                        screen1.mouseUp(Button.LEFT)
    
                        wait(1)
    
                        if screen1.exists(Pattern("1606488196381-1.png").targetOffset(-4,22),2):
                            screen1.hover(Pattern("1606488196381-1.png").targetOffset(-4,22))
                            screen1.mouseDown(Button.LEFT)
                            wait(1)
                            screen1.mouseUp(Button.LEFT)
                            
                            if screen1.exists(Pattern("1606488301351-1.png").targetOffset(60,-3),2):
                                screen1.hover(Pattern("1606488301351-1.png").targetOffset(60,-3))
                                screen1.mouseDown(Button.LEFT)
                                wait(1)
                                screen1.mouseUp(Button.LEFT)
                                if screen1.exists(Pattern("1606488340773-1.png").similar(0.85),2):
                                    screen1.hover(Pattern("1606488340773-1.png").similar(0.85))
                                    screen1.mouseDown(Button.LEFT)
                                    wait(1)
                                    screen1.mouseUp(Button.LEFT)
                                    
                                wait(2)
                                while screen1.exists("1606570860653-1.png"):
                                    if screen1.exists("1606570860653-1.png"):
                                        type("x")
                                        type("x")
                                        print("closeBag")
                                        
    while screen1.exists("1605180281291-2.png",10):
        wait(1)
        if screen1.exists("1605180281291-2.png",2):
            type("x")
            screen1.hover("1605180281291-2.png")
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)
        if screen1.exists("1606186199403-1.png",3):
            screen1.hover("1606186199403-1.png")
            screen1.hover(Pattern("1605226161228-1.png").similar(0.80))
            
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)
        if screen1.exists(Pattern("1606389186973-1.png").similar(0.80),2): 
            if screen1.exists("1606389225224-1.png",2):
                screen1.click(Pattern("1606389225224-1.png").targetOffset(82,-4))
        
    #startToBattle
    
    #closeBattle

    while 1:
        if screen1.exists("1607009569477.png",5):
            screen1.hover("1607009569477-1.png")
            wait(1)
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)
        
            if screen1.exists("1607060339692.png",2):
                screen1.hover(Pattern("1607060352157.png").targetOffset(88,-4))
                screen1.mouseDown(Button.LEFT)
                wait(1)
                screen1.mouseUp(Button.LEFT)
        
            if screen1.exists(Pattern("1605241154424-6.png").similar(0.95),2):
                screen1.hover(Pattern("1605241154424-6.png").similar(0.95))
                screen1.mouseDown(Button.LEFT)
                wait(1)
                screen1.mouseUp(Button.LEFT)
    
            checkQuantity = 1
            max1 = CheckHero(heroMaxRegion1,checkQuantity)
            type("x")
            checkQuantity = 2
            max2 = CheckHero(heroMaxRegion2,checkQuantity)
            type("x")
            checkQuantity = 3
            max3 = CheckHero(heroMaxRegion3,checkQuantity)
            type("x")
            
            print(max1)
            print(max2)
            print(max3)

            while screen1.exists("1605184103591-8.png",10):
                if screen1.exists("1605184103591-8.png",10):
                    screen1.hover("1605184103591-7.png")
                    screen1.mouseDown(Button.LEFT)
                    wait(1)
                    screen1.mouseUp(Button.LEFT)
                    wait(1)

                if screen1.exists("1607060339692.png",2):
                    screen1.hover(Pattern("1607060352157.png").targetOffset(88,-4))
                    screen1.mouseDown(Button.LEFT)
                    wait(1)
                    screen1.mouseUp(Button.LEFT)

            print("success")
            x += 1
            print("times：")
            print(x)
            break
        if screen1.exists(Pattern("1607009750496-2.png").similar(0.75),3):
    
            screen1.hover(Pattern("1607009750496-3.png").similar(0.75))
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)

            if screen1.exists("1607060339692.png",2):
                screen1.hover(Pattern("1607060352157.png").targetOffset(88,-4))
                screen1.mouseDown(Button.LEFT)
                wait(1)
                screen1.mouseUp(Button.LEFT)

            if screen1.exists(Pattern("1605241154424-5.png").similar(0.90),2):
                screen1.hover(Pattern("1605241154424-5.png").similar(0.90))
                screen1.mouseDown(Button.LEFT)
                wait(1)
                screen1.mouseUp(Button.LEFT)
                
            print("fail")
            break

    while repeatRegion.exists(Pattern("1607052962267-1.png").similar(0.80),2):
        repeatRegion.hover(Pattern("1607052962267-1.png").similar(0.80))
        repeatRegion.mouseDown(Button.LEFT)
        wait(1)
        repeatRegion.mouseUp(Button.LEFT)
        print("FindRepeat")
        wait(1)
        if screen1.exists("1606390194298-4.png",2):
            screen1.hover(Pattern("1606390194298-4.png").targetOffset(-84,3))
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)









