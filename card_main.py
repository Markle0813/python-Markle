
# -*- coding: utf-8 -*-
import card_tools

while True:

    # TODO 显示功能菜单
    card_tools.show_menu()
    action_str = input('请输入希望执行的操作：')

    if action_str in ['1', '2', '3']:
        # 新增名片
        if action_str == '1':
            card_tools.new_card()
        # 显示全部
        if action_str == '2':

            card_tools.show_all()
        # 查询名片
        if action_str == '3':
            card_tools.search_card()
    elif action_str == '0':
        print('欢迎再次使用本系统')
        break
    else:
        print('您输入的内容有误，请重新选择')
