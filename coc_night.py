#图片匹配
import aircv as ac
from time import sleep
#截屏
import win32gui, win32ui, win32con, win32api
#截图
import cv2
#自动化鼠标
import pyautogui

list1 = [68,122,1450,1733,162,217,1450,1733,256,300,1546,1736]
list2 = [158,200,137,286,209,249,137,286,263,306,137,286]

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

def click1(name,number):
        coordinate = match_img("screenshot.jpg",name +".jpg")
        if(coordinate is not None):
            click_img(coordinate,number)
            print(name + " is success!")
            return 0
        else:
            print(name + " is fail!")
            return 1
def click(name,number=1):
    button = click1(name,number)
    i=0
    while(button and i<10):
        button = click1(name,number)
        i = i+1
        
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


axis_click(163,924)#attack
sleep(1)
times=0
while(times<15):
    axis_click(1241,468)#find
    sleep(10)
    #调整画面
    pyautogui.keyDown("ctrl")
    pyautogui.scroll(-1000)
    pyautogui.keyUp("ctrl")
    sleep(10)
    pyautogui.moveTo(944,754)
    pyautogui.dragRel(0,-500,duration=0.5)
    axis_click(330,940)#第一个
    pyautogui.press(['q','e'])
    sleep(1)
    pyautogui.press(['u','m'])
    sleep(1)
    pyautogui.press(['z','c'])
    sleep(1)
    pyautogui.press(['a','d'])
    sleep(1)
    pyautogui.press(['w','j'])
    sleep(1)
    pyautogui.press(['s','d'])
    #axis_click(600,940)#第三个
    wait = 0
    window_capture("screenshot.jpg")
    while(click1("Okay",1)and wait<12):
        sleep(15)
        window_capture("screenshot.jpg")
        wait = wait + 1
    sleep(226-wait*15)
    axis_click(1388,752)#okay
    sleep(1)
    times = times+1









