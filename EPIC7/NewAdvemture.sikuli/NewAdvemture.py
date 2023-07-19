#IDE使用說明：

#螢幕截圖 可截圖螢幕使其可被搜索 可點選螢幕截圖所截圖的圖片 對比圖片、調整相似度、指定滑鼠點選圖片位置
#Region() 工具欄中 可指定要搜尋的範圍 點選Region()中的圖片會進入重新指定搜尋範圍的螢幕截圖
#插入圖片 找選同樣用此IDE所截圖的圖片但複製貼上還比較快
#Location() 完全不知跟region()有啥差別= =
#offSet() 沒用過
#執行 執行程式
#慢動作執行 已經夠慢了就不用更慢了
#重要快捷鍵 同時按下 SHIFT+ALT+C能終止程式別進入無限迴圈
#重要快捷鍵 同時按下 SHIFT+ALT+C能終止程式別進入無限迴圈
#重要快捷鍵 同時按下 SHIFT+ALT+C能終止程式別進入無限迴圈
#重要所以說三次

#參數說明:

#screen1指定右上方螢幕限制搜尋範圍
#RunningGame指定右上方進入遊戲跑動標示
#heroMaxRegion1 完成關卡時確認位置1有無MAX等級英雄
#heroMaxRegion2 完成關卡時確認位置2有無MAX等級英雄
#heroMaxRegion3 完成關卡時確認位置3有無MAX等級英雄
#checkCanPutRegioon1 確認heroMaxRegion1有可換MAX等級圖片時可以點選
#checkCanPutRegioon2 確認heroMaxRegion2有可換MAX等級圖片時可以點選
#checkCanPutRegioon3 確認heroMaxRegion3有可換MAX等級圖片時可以點選
screen1 = Region(Region(392,0,1144,659))
RunningGame = Region(Region(1214,540,322,122))

heroMaxRegion1 = Region(Region(733,516,112,74))
heroMaxRegion2 = Region(Region(928,526,97,47))
heroMaxRegion3 = Region(Region(1099,526,102,49))

checkCanPutRegioon1 = Region(Region(787,330,128,100))
checkCanPutRegioon2 = Region(Region(786,196,114,107))
checkCanPutRegioon3 = Region(Region(682,277,110,92))

#有無MAX等級英雄查看
def CheckHero(CheckHaveMaxheroRegion,inputCheckQuantity):
    if CheckHaveMaxheroRegion.exists(Pattern("1623137887756.png").similar(0.60),3):
        CheckHaveMaxheroRegion.hover(Pattern("1623137887756.png").similar(0.60))
        print("HaveMax")
        return inputCheckQuantity
        
    else :
        print("NoMax")
        return 0


#打開選取英雄列表 我的想法是把要當肥料的英雄鎖定和是MAX等級英雄隱藏使其在列表排列時能快速點選
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

#當英雄列表出現時一個一個依序點選並在可更換時更換英雄
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


#打開背包並販售所有等級低的裝備並在打開英雄背包時結束程式
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


#不治愈英雄
def rejectHeal():
    if screen1.exists(Pattern("1605426274746.png").targetOffset(-126,-6),1):
        screen1.hover(Pattern("1605426274746.png").targetOffset(-126,-6))
        wait(1)
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)


#當顯示出要不邀請新朋友時邀請

def getNewFriend():

    if screen1.exists("1641190817890-1.png",4):
        screen1.hover(Pattern("1641190829499-1.png").targetOffset(89,-6))
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)

#初始MAX等級位置辨識參數可不管，永遠初始為零
max1 = 0
max2 = 0
max3 = 0
#OpenbackageOpen當要販售裝備時請更改參數為1不想販售為0 當參數為零時會自動終止程式
#OpenbackageOpen當要販售裝備時請更改參數為1不想販售為0 當參數為零時會自動終止程式
#OpenbackageOpen當要販售裝備時請更改參數為1不想販售為0 當參數為零時會自動終止程式
OpenbackageOpen = 0
#x初始迴圈數 Y想要執行的迴圈數
x = 0
y = 15

#點選準備戰鬥圖像，最好是用此點選法，先將滑鼠移動到圖片上方再按下一秒再點選穩定度較高
#找尋Region() = screen1 是否有準備戰鬥圖像有的話執行IF 沒有的話跳過
#語法介紹 screen1 之前定義的Region參數第25行 exists() 有無存在圖片可在exists(螢幕截圖,重複尋找秒數)
if screen1.exists("1622955228998.png",3):
    #把滑鼠移動到準備戰鬥圖片上 hover()
    screen1.hover("1622955228998.png")
    #按下滑鼠
    screen1.mouseDown(Button.LEFT)
    #等待一秒
    wait(1)
    #放開滑鼠
    screen1.mouseUp(Button.LEFT)

#進入迴圈
while x<y:

    if screen1.exists("1641187837656.png",10):
        wait(1)
        #定義friend的圖片x 和 y的平面軸，國中數學
        friend = screen1.find("1641187837656.png")
        wait(1)
        #點選 friend圖片的XY軸的X+70Y+220的像數點位置
        screen1.click(Location(friend.x+70,friend.y+270))
        
    if screen1.exists("1605178407940.png",5):
        screen1.hover("1605178407940.png")
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)
    #當有MAX英雄時執行跟換英雄位置
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

#當遊戲未進入時重複執行下列動作
    while not RunningGame.exists(Pattern("1641293336969.png").similar(0.50),1):

        print("finding")
        if screen1.exists("1605180281291.png",1):
            wait(1)
            screen1.hover("1605180281291.png")
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)
            print("battleStart")

        if screen1.exists("1641202127022.png",1):
            wait(1)
            screen1.hover(Pattern("1641202127022.png").targetOffset(83,-2))
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)

        if screen1.exists("1623225225288-1.png",1):
            wait(1)
            screen1.hover(Pattern("1623225225288-1.png").targetOffset(83,-5))
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)
    
        if screen1.exists("1623638672906-1.png",1):
            
            if OpenbackageOpen == 1:
                backageOpen()
            else:
                keyDown(Key.SHIFT) 
                keyDown(Key.ALT) 
                type("c")

#等待遊戲打贏或打輸
    while 1:
        print("waiting")
        if screen1.exists(Pattern("1641192829642-2.png").similar(0.60),1):
            screen1.hover(Pattern("1641192829642-2.png").similar(0.60))
            screen1.mouseDown(Button.LEFT)
            wait(1)
            screen1.mouseUp(Button.LEFT)
            print("WIN")
            break

        if screen1.exists("1641193970814-2.png",1):
            screen1.hover("1641193970814-2.png")
            print("LOSE")
            break

#當回合節結束時判斷有無MAX等級英雄並給予參數和結束緊急任務視窗
    while not screen1.exists("1641187770939.png",1):
        getNewFriend()
        if screen1.exists("1641187669242.png",1):
            #checkQuantity = 1
            #max1 = CheckHero(heroMaxRegion1,checkQuantity)

            #checkQuantity = 2
            #max2 = CheckHero(heroMaxRegion2,checkQuantity)

            #checkQuantity = 3
            #max3 = CheckHero(heroMaxRegion3,checkQuantity)
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

#重新開始
    if screen1.exists("1641187770939.png",5):
        screen1.hover(Pattern("1641187770939.png").targetOffset(2,-1))
        wait(1)
        screen1.mouseDown(Button.LEFT)
        wait(1)
        screen1.mouseUp(Button.LEFT)
        wait(1)
        print("FindRepeat")
        print(x)

    










