import pyautogui
import time

def mage_frost_main():
    data = []
    with open("data.txt", "r",encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip('\n')  # 去掉列表中每一个元素的换行符
            data.append(line)

     # 用户自定义参数
    move_speed = float(data[0])
    belt_space = int(data[1])
    load_time = float(data[2])
    times = int(data[3])



    # 脚本参数
    HP_space = belt_space / 2
    MP_space = belt_space / 2
    belt_remaining=[HP_space,MP_space]
    drinking=[0,0]

    # 分辨率与初始化
    x, y = pyautogui.size()
    # time.sleep(2)


    def drinkHP_fromBelt():
        if belt_remaining[0] > HP_space / 2:
            pyautogui.press('2')
            belt_remaining[0]-=1
            drinking[0]=12
        else:
            pyautogui.press('1')
            belt_remaining[0] -= 1
            drinking[0] = 1


    def drinkMP_fromBelt():
        if (belt_remaining[1] > MP_space / 2):
            pyautogui.press('4')
            belt_remaining[1] -= 1
            drinking[1] = 1
        else:
            pyautogui.press('3')
            belt_remaining[1] -= 1
            drinking[1] = 1

    def start():
        time.sleep(5)

        #血蓝检查
        img = pyautogui.screenshot()
        colorHP = img.getpixel((0.25 * x, 0.92 * y))
        colorMP = img.getpixel((0.75 * x, 0.92 * y))
        if (colorHP[0] < 50 and drinking[0] == 0): drinkHP_fromBelt()
        time.sleep(0.3)
        if (colorMP[2] < 20 and drinking[1] == 0): drinkMP_fromBelt()
        time.sleep(0.3)

        # 走向小站
        pyautogui.moveTo(0.35 * x, 0.7 * y, duration=0.2)
        pyautogui.mouseDown()
        time.sleep(3.5/move_speed)
        pyautogui.mouseUp()
        time.sleep(1.5)

        # 点击小站，点击冰冻高地
        pyautogui.moveTo(0.5 * x, 0.51 * y, duration=0.2)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(0.2 * x, 0.3 * y, duration=0.2)
        pyautogui.click()
        time.sleep(load_time/2)

        # 去有怪的地方
        pyautogui.moveTo(0.5 * x, 0.1 * y, duration=0.2)
        pyautogui.mouseDown()
        time.sleep(3.3)
        pyautogui.mouseUp()

        # 一发暴风雪
        pyautogui.click(0.5 * x, 0.1 * y, button='right')

        # 走位
        pyautogui.moveTo(0.4 * x, 0.45 * y, duration=0.2)
        pyautogui.mouseDown()
        pyautogui.keyDown('ctrl')

        time.sleep(0.2)
        pyautogui.moveTo(0.6 * x, 0.45 * y, duration=0.2)
        time.sleep(0.2)
        pyautogui.moveTo(0.4 * x, 0.45 * y, duration=0.2)
        time.sleep(0.2)
        pyautogui.moveTo(0.6 * x, 0.45 * y, duration=0.2)
        time.sleep(0.2)

        # 一发暴风雪
        pyautogui.click(0.5 * x, 0.55 * y, button='right')

        # 走位
        time.sleep(0.5)
        pyautogui.moveTo(0.6 * x, 0.45 * y, duration=0.2)
        time.sleep(0.3)
        pyautogui.moveTo(0.4 * x, 0.45 * y, duration=0.2)
        time.sleep(0.3)
        pyautogui.moveTo(0.6 * x, 0.55 * y, duration=0.2)
        time.sleep(0.3)
        pyautogui.moveTo(0.6 * x, 0.55 * y, duration=0.2)
        time.sleep(0.3)
        pyautogui.moveTo(0.4 * x, 0.45 * y, duration=0.2)
        time.sleep(0.3)
        pyautogui.moveTo(0.6 * x, 0.45 * y, duration=0.2)
        time.sleep(0.3)

        # 一发暴风雪
        pyautogui.click(0.5 * x, 0.55 * y, button='right')

        time.sleep(0.5)
        pyautogui.moveTo(0.6 * x, 0.45 * y, duration=0.2)
        time.sleep(0.3)
        pyautogui.moveTo(0.4 * x, 0.45 * y, duration=0.2)
        time.sleep(0.3)
        pyautogui.moveTo(0.6 * x, 0.55 * y, duration=0.2)
        time.sleep(0.3)
        pyautogui.moveTo(0.6 * x, 0.55 * y, duration=0.2)
        time.sleep(0.3)
        pyautogui.moveTo(0.4 * x, 0.45 * y, duration=0.2)
        time.sleep(0.3)
        pyautogui.moveTo(0.6 * x, 0.45 * y, duration=0.2)
        time.sleep(0.3)
        pyautogui.mouseUp()
        pyautogui.keyUp('ctrl')
        time.sleep(0.1)



        # 等怪死完同时注意血量
        # for i in range(10):
        #     img = pyautogui.screenshot()
        #     colorHP = img.getpixel((0.25*x,0.92*y))
        #     colorMP = img.getpixel((0.75*x,0.96*y))
        #     if (colorHP[0] < 50 and drinking[0]==0): drinkHP_fromBelt()
        #     time.sleep(0.3)
        #     if (colorMP[2] < 20 and drinking[1]==0): drinkMP_fromBelt()
        #     time.sleep(0.3)

        #回主菜单,初始化喝血药状态，再打开噩梦难度
        pyautogui.press('esc')
        time.sleep(0.5)
        pyautogui.click(0.5 * x, 0.43 * y, button='left')
        time.sleep(1)
        drinking[0]=0
        drinking[1]=0
        time.sleep(load_time)
        pyautogui.click(0.42*x,0.9*y, button='left')
        time.sleep(0.5)
        pyautogui.click(0.5*x,0.48*y, button='left')


    print("脚本开始运行")
    for i in range(times):
        print("正在进行第",i,"次...")
        start()
        if(belt_remaining[0]==0):
            pyautogui.alert(text='血瓶不足，中止', title='', button='OK')
            print("血瓶不足，中止")
            break
        if (belt_remaining[1] == 0):
            pyautogui.alert(text='蓝瓶不足，中止', title='', button='OK')
            print("蓝瓶不足，中止")
            break
