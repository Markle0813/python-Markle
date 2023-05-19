import pyautogui as pg

pg.PAUSE = 0.01

import pyautogui as pg
#print(pg.position())
pg.PAUSE = 0.01
for i in range(50000):
    if i and pg.position() != (1568, 771):
        print('break')
        break
    #     鼠标坐标
    pg.click(1568, 771)
    print(i)











