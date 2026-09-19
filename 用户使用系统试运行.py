# 初始默认账号
user_name_ed = "1"
key_code_ed = "1"

while True:
    print("""
         欢迎使用本产品，需要确认您是否已有登录
                 1.是(新用户注册)，2.不是(老用户登录)
        """)
    answer = int(input("您好，请问你是否是第一次使用本产品?（填1/2即可）"))
    match answer:
        case 1:
            word_user_name = input("请输入您要使用的用户名：")
            word_user_key = input("请输入你的密码：")

            word_user_name_2 = input("请再次确认用户名：")
            word_user_key_2 = input("请再次确认密码：")
            if word_user_key == word_user_key_2 and word_user_name == word_user_name_2:
               
                user_name_ed = word_user_name
                key_code_ed = word_user_key
                print("恭喜您注册登录成功！")
                break
            else:
                print("抱歉，两次输入不一致！请重新输入！")

        case 2:
            print("欢迎您再次使用，需要您的账号和密码")
            word_user_name = input("请输入您要使用的用户名：")
            word_user_key = input("请输入你的密码：")

            if word_user_name == user_name_ed and word_user_key == key_code_ed:
                print("恭喜您登录成功!")
                break
            else:
                print("您的输入密码有误或者用户名不对应，请再次输入")
        case _:
            print("您的填写方式有误，请重新填写！")