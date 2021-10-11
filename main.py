import PySimpleGUI as sg
import os
import pyautogui
import time
import assassin_trap
import mage_frost

pyautogui.FAILSAFE = True


def save(values):
    str = values[0] + "\n" + values[1] + '\n' + values[2] + '\n' + values[3] + '\n' + values[4][0]
    print(str)
    with open("data.txt", "w", encoding='utf-8') as f:
        f.write(str)


content = ['冰冻高原-陷阱刺', '冰冻高原-冰法']
document = ['assassin_trap', 'mage_frost']
data = []

with open("data.txt", "r", encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip('\n')  # 去掉列表中每一个元素的换行符
        data.append(line)

print(data)
content = ['冰冻高原-陷阱刺', '冰冻高原-冰法']
layout = [
          [sg.Text('鼠标移到屏幕左上角以强制终止程序', text_color='#c3c3c3')],
          [sg.Text('走路速度：'), sg.Text('初始走路速度的倍数', text_color='#c3c3c3'), sg.InputText(size=12, default_text=data[0])],
          [sg.Text('背包大小：'), sg.Text('腰带的格数', text_color='#c3c3c3'), sg.InputText(size=12, default_text=data[1])],
          [sg.Text('加载速度：'), sg.Text('加载入地图最慢的速度(秒数)，建议大一点以防bug', text_color='#c3c3c3'),
           sg.InputText(size=12, default_text=data[2])],
          [sg.Text('循环次数：'), sg.Text('循环刷的次数', text_color='#c3c3c3'), sg.InputText(size=12, default_text=data[3])],
          [sg.Listbox(values=content, size=(20, 6), enable_events=True, default_values=['冰冻高原-陷阱刺']),
           sg.Button('RUN'), sg.Button('CLOSE'), sg.Button('INSTRUCTION')]
          ]

# 创造窗口
window = sg.Window('Window Title', layout)

# 事件循环并获取输入值

while True:
    event, values = window.read()
    if event in (None, 'CLOSE'):
        break

    if event in (None, 'RUN'):
        print('Running', values[4][0])
        save(values)
        print(values, "saved")
        if (values[4][0] == '冰冻高原-陷阱刺'): assassin_trap.assassin_trap_main()
        if (values[4][0] == '冰冻高原-冰法'): mage_frost.mage_frost_main()
    if event in (None, 'INSTRUCTION'):
        os.system("data.txt")
        pyautogui.PAUSE = 1000
    print('You entered ', values)

window.close()
