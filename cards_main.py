#  #！ python解释器
import cards_tools
import ImageStringGet


while True:
    #  显示功能菜单
    cards_tools.show_menu()

    action_str = input("请选择希望执行的操作： ")
    print("您选择的操作是【%s】" % action_str)

    if action_str in ["1", "2", "3","4"]:
        if action_str == "1":
            cards_tools.new_card()
        if action_str == "2":
            cards_tools.show_all()
        if action_str == "3":
            cards_tools.search_card()
        if action_str == "4":
            a,b,c= ImageStringGet.ChineseGet('card2.png')
            print(a,b,c)
            cards_tools.addCard(a, b, c)
        pass
    elif action_str == "0":
        print("欢迎再次使用【名片管理系统】")
        break
    # pass
    else:
        print("您输入的不正确，请重新选择")
