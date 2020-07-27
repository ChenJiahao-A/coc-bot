#图片匹配
import aircv as ac
from time import sleep
#截屏
import win32gui, win32ui, win32con, win32api
#截图
import cv2
#自动化鼠标
import pyautogui
#百度需要
from aip import AipOcr
import re
#移动文件
from shutil import move
#退出
import sys
#改变工作目录
from os import getcwd
from os import chdir

list1 = [68,122,1450,1733,162,217,1450,1733,256,300,1546,1736]
list2 = [158,200,137,286,209,249,137,286,263,306,137,286]

#百度账号信息
APP_ID =''
API_KEY = ''
SECRET_KEY = ''
client = AipOcr(APP_ID,API_KEY,SECRET_KEY)



def match_img(imgsrc,imgobj,confidencevalue=0.7):#imgsrc=原始图像，imgobj=待查找的图片
    x_co = None
    y_co = None
    imsrc = ac.imread(imgsrc)
    imobj = ac.imread(imgobj)

    match_result = ac.find_template(imsrc,imobj,confidencevalue)
    return (match_result)

def click_img(match_result,number):
    x_co = (match_result['rectangle'][0][0] + match_result['rectangle'][2][0])/2
    y_co = (match_result['rectangle'][0][1] + match_result['rectangle'][1][1])/2
    pyautogui.moveTo(x_co,y_co,duration=0.25,tween=pyautogui.linear)
    pyautogui.click(clicks=number,interval=0.2)

def click(name,number=1):
        coordinate = match_img("screenshot.jpg",name +".jpg")
        confidence = 0.65
        while(coordinate is None and confidence >0.49):
            print(name + " is fail!")
            window_capture("screenshot.jpg")
            coordinate = match_img("screenshot.jpg",name +".jpg",confidence)
            confidence = confidence - 0.05
            print("confidence is " , confidence)
            
        if(confidence >0.49):
            click_img(coordinate,number)
            return 0
        else:
            return 1
        
def axis_click(x,y):
    pyautogui.moveTo(x,y)
    pyautogui.click()

    
def window_capture(filename):
    hwnd = 0  # 窗口的编号，0号表示当前活跃窗口
    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建bigmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 获取监控器信息
    MoniterDev = win32api.EnumDisplayMonitors(None, None)
    w = MoniterDev[0][2][2]
    h = MoniterDev[0][2][3]
    # print w,h　　　#图片大小
    # 为bitmap开辟空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 截取从左上角（0，0）长宽为（w，h）的图片
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)

def count(list1):
    black_number = 0
    elixir_number = 0
    gold_number = 0
    #截屏
    #judge_cloud()函数已截图
    #截图
    img=cv2.imread("screenshot.jpg")
    cv2.imwrite("gold_number.jpg",img[list1[0]:list1[1],list1[2]:list1[3]])
    cv2.imwrite("elixir_number.jpg",img[list1[4]:list1[5],list1[6]:list1[7]])
    cv2.imwrite("black_number.jpg",img[list1[8]:list1[9],list1[10]:list1[11]])
    
    #统计资源
    gold_number_img = open("gold_number.jpg","rb").read()
    elixir_number_img = open("elixir_number.jpg","rb").read()
    black_number_img = open("black_number.jpg","rb").read()
    
    gold_img_message = client.basicAccurate(gold_number_img)
    elixir_img_message = client.basicAccurate(elixir_number_img)
    black_img_message = client.numbers(black_number_img)

    try:
        gold_number = int(gold_img_message.get("words_result")[0].get("words"))
        elixir_number = int(elixir_img_message.get("words_result")[0].get("words"))
        black_number = int(black_img_message.get("words_result")[0].get("words"))
        print(black_number)

        #临时任务
        move('Gold_number.jpg','base\\'+str(gold_number)+'.jpg')
        move("elixir_number.jpg",'base\\'+str(elixir_number)+'.jpg')
        move("black_number.jpg",'base\\'+str(black_number)+'.jpg')
    except:
        print('next1')

    return (gold_number,elixir_number,black_number)

def place(a,b,c,x,y,z):
    #胖子
    click("Attack_gia")
    sleep(1)
    pyautogui.press([a,b,c],interval=0.1)
    #野蛮人
    click("Attack_bar")
    sleep(1)
    pyautogui.press([x,y,z],presses=4,interval=0.1)
    #弓箭手
    click("Attack_arc")
    sleep(1)
    pyautogui.press([x,y,z],presses=5,interval=0.1)
    sleep(0.5)
    pyautogui.press([a,b,c],presses=5,interval=0.1)

def judge_sucess(name,time=60):
    sleep(time)
    window_capture("screenshot.jpg")
    p=0
    standard = match_img("screenshot.jpg",name+".jpg")
    while((standard is None ) and p<8):
        sleep(time)
        window_capture("screenshot.jpg")
        standard = match_img("screenshot.jpg",name+".jpg")
        axis_click(960,579)
        p=p+1
    if(p>8):
        print("Recognition of "+ name + ".jpg is overtime!")
        sys.exit("exit！")
        

def attack():
    print("Attack!")
    #进攻
    axis_click(154,914)#icon of attack
    axis_click(1422,660)#icon of find

    #判断是否进攻
    judge_sucess("Attack_cup",5)
    
    (g_number,e_number,b_number) = count(list2)
    
    while(g_number<170000 or e_number<170000):
        axis_click(1700,753)
        judge_sucess("Attack_cup",5)
        (g_number,e_number,b_number) = count(list2)
        total = g_number+e_number+b_number
    #调整画面
    pyautogui.moveTo(1920/2,1080/2)
    pyautogui.dragRel(0,200,duration=0.3)
    pyautogui.scroll(500)
    sleep(3)
    pyautogui.dragRel(-300,0,duration=0.25)
    sleep(2)

    #下兵
    window_capture("screenshot.jpg")
    '''
    click('Attack_lig')
    pyautogui.moveTo(1920/2,1080/2)
    pyautogui.click(clicks=3,interval=0.2)
    '''
    click('Attack_clan')
    pyautogui.press('x')
    place('z','x','c','v','b','n')
    place('a','s','d','f','g','h')
    click('Attack_queen')
    #click('Attack_king')
    pyautogui.press('s')

    #调整画面
    pyautogui.moveTo(1920/2,1080/2)
    pyautogui.dragRel(0,-200,duration=0.3)
    pyautogui.scroll(-500)
    #下兵
    place('q','w','e','r','t','y')
    place('u','j','m','i','k','o')
    click('Attack_queen')
    #click('Attack_king')

    sleep(45)
    judge_sucess("return_home",15)
    axis_click(941,926)
    print("Return home!")


def train():
    print("Train!")
    #训练兵种
    axis_click(121,756)#icon of army
    sleep(1)
    axis_click(567,95)#icon of train troops
    window_capture("screenshot.jpg")
    click("Giant",12)
    #number = int(input("Barbarian's number："))
    click("Barbarian",48)
    #number = int(input("Archer's number："))
    click("Archer",112)
    '''
    click('brew')
    window_capture("screenshot.jpg")
    click('healing',2)
    click('lightning',3)
    '''
    axis_click(1728,86)#icon of exit
    
def reinforcement():
    print("Ask reinforcement!")
    window_capture("screenshot.jpg")
    click('clan')
    window_capture("screenshot.jpg")
    click('request')
    window_capture("screenshot.jpg")
    click('send')
    


def complete():
    #打开coc
    #截屏
    window_capture("screenshot.jpg")
    '''
    #统计资源
    (g_number0,e_number0,b_number0) = count(list1)
    print(g_number0,e_number0,b_number)
    '''
    #先收集资源
    click("Gold")
    click("Elixir")
    click("Dark_elixir")


    sleep(3)
    times=0
    while(times < 2):
        attack()#进攻
        sleep(30)
        pyautogui.keyDown("ctrl")
        pyautogui.scroll(-1000)
        pyautogui.keyUp("ctrl")
        train()#训练
        sleep(1)
        if(times%5 == 0):
            print(1)
            reinforcement()#援兵
        times = times+1
        sleep(10)


wd = getcwd()
chdir(wd+'\\picture')

launch = 0
while(launch < 14):
    window_capture("screenshot.jpg")
    click("simulator",2)
    
    judge_sucess("coc_icon")
    
    axis_click(1076,276)#coc_icon
    sleep(3)
    axis_click(1703,67)#放大

    ###axis_click(960,923)#okay
    
    judge_sucess("Dark_elixir")

    
    complete()

    axis_click(1860,16)#关闭
    axis_click(1093,596)#退出
    launch = launch+1
    minute = 60*50
    sleep(minute)
    print(launch,"*************************************************")
    
    
    
    
print("Done!")


