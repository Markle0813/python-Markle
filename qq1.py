def say_hello():

    print("hi 1")
    print("hi 2")
    print("hi 3")
    print('*' * 50)
    print('功能：显示全部')
    print('*' * 50)
    print('功能：搜索名片')
    # 提示登陆
    password = 8336797
    password = input("请输入密码")
    if password == 8336797:
        print("登陆成功")
    else:
        print("登陆失败，请重新登录")
        # 提示登陆
        password = 8336797
        password = input("请输入密码")
        if password == 8336797:
            print("登陆成功")
        else:
            print("登陆失败，请重新登录")
