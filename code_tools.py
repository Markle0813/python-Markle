
# 展示菜单
print("欢迎游玩游戏")
# 提示玩家输入操作
while True:

    # TODO 显示功能菜单
    player = input('请输入希望执行的操作：')
    if player in ['1', '2', '3']:
        # 操作1
        if player == '1':
            print("你好1")
        # 操作2
        if player == '2':
            print("你好2")
        # 操作3
        if player == '3':
            print("你好3")
    elif player == '0':
        print("欢迎再次游玩")
        break
    else:
        print("你输入的操作有误")
    #     二次
    




