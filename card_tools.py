
card_list = []
def show_menu():
    # 显示菜单
    print('*' * 50)
    print(
        '''
欢迎使用名片管理系统 V1.0

1.新增名片
2.显示全部
3.搜索名片
0.退出系统
        '''
    )
    print('*' * 50)


def new_card():
    print('*' * 50)
    print('新增名片')
    # 提示用户输入名片
    name_str = input('请输入姓名：')
    phone_str = input('请输入电话：')
    qq_str = input('请输入qq:')
    email_str = input('请输入邮箱：')
    card_dict = {'name': name_str,
                 'phone': phone_str,
                 'qq': qq_str,
                 'email': email_str}
    card_list.append(card_dict)
    print(card_dict)
    print('成功添加%s的名片' % card_dict['name'])


def show_all():
    # 显示全部
    # 2 提示用户输入密码

    print('*' * 50)
    print('功能：显示全部')

    # 判断是否有名片记录
    if len(card_list) == 0:
        print('提示：没有任何名片记录')
        return

    # 打印表头
    for name in ['姓名', '电话', 'QQ', '邮箱']:
        print(name, end='\t\t')

    print(' ')

    # 打印分割线
    print('*' * 50)
    for card_dict in card_list:
        print('%s\t\t%s\t\t%s\t\t%s\t\t' % (card_dict['name'],
                                            card_dict['phone'],
                                            card_dict['qq'],
                                            card_dict['email']))


def search_card():
    # 提示登陆






    find_name = input('请输入要搜索的姓名：')
    for card_dict in card_list:
        if card_dict['name'] == find_name:
            print('姓名\t\t\t电话\t\t\tQQ\t\t\t邮箱')
            print('*' * 40)

            print('%s\t\t\t%s\t\t\t%s\t\t\t%s' % (
                card_dict['name'],
                card_dict['phone'],
                card_dict['qq'],
                card_dict['email']
            ))
            print('*' * 40)
            deal_card(card_dict)

            break
        else:
            print('没有找到%s的名片' % find_name)


def deal_card(find_dict):

    print(find_dict)
    action_str = input('请选择要进行的操作：'
                       '1.修改 2.删除 3.返回主菜单')

    if action_str == '1':
        find_dict['name'] = input_card_info(find_dict['name'], '姓名：')
        find_dict['phone'] = input_card_info(find_dict['phone'], '电话：')
        find_dict['qq'] = input_card_info(find_dict['qq'], 'QQ：')
        find_dict['email'] = input_card_info(find_dict['email'], '邮箱：')
        print('修改名片成功')

    elif action_str == '2':
        card_list.remove(find_dict)
        print('删除名片成功')


def input_card_info(dict_value, tip_message):
    # 1.提示用户输入内容
    result_str = input(tip_message)
    # 2如果输入内容，直接返回结果
    if len(result_str) > 0:
        return result_str
    # 3.如果用户没有输入内容，返回‘字典原有值’
    else:
        return dict_value





