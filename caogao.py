# import random
# print("欢迎游玩")
# player = eval(input("请输入 点数 1 点数 2 点数 3 点数 4"))
# computer = random.randint(1,4)
# print("你输入的为 %d 电脑输入为 %d" %(player,computer))
# if ((player == 2 and computer == 1 )
#         or (player == 3 and computer == 1)
#         or (player == 3 and computer == 2)
#         or (player == 4 and computer == 1)
#         or (player == 4 and computer == 3)
#         or (player == 4 and computer == 2)):
#
#
#
#     print("恭喜获胜")
# elif(player == computer):
#
#     print("平手")
# else:
#
#     i = 1
#     while i <= 5:
#         print("电脑都打不过")
#         i += 1
#     print("数字 %d" % i)


































import pyautogui as pg

pg.PAUSE = 0.01

import pyautogui as pg
#print(pg.position())
pg.PAUSE = 0.001
for i in range(111):
    if i and pg.position() != (1568, 771):
        print('break')
        break
    pg.click(1568, 771)
    print(i)

























# import random
# player = eval(input("请输入数字"))
# computer = random.randint(1,5)
# print("你输入的数字为 %d 电脑输入的数字为 %d" %(player,computer))
# if((player==1 and computer==2)
#     or(player== 1 and computer== 3)
#     or(player==1 and computer==4)
#     or(player==2 and computer==3)
#     or(player==3 and computer==4)):
#
#
#
#         print("你赢了")
# elif(player==computer):
#     print("平局")
# else:
#     print("你输了")
#     def print_long(char,times):
#         print(char*times)
#     print_long("SB ",10)

































import random
oklook =random.randint(1,4)
computer =random.randint(1,4)
print("您的中奖号码为%d 中奖号码为 %d" %(oklook,computer))
if((oklook==1 and computer==2)
        or (oklook==2 and computer == 3)
        or (oklook == 3 and computer == 4)):
        print("你没有中将")
elif(oklook==computer):
    print("恭喜中奖")
else:
    print("你没有中将")




















