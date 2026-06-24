# 开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据，
# 通过控制台菜单与用户交互。具体功能如下:
# 1.添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
# 2.修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
# 3.删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
# 4.查询购物车：将购物车中的商品信息展示出来，格式为："商品名称： xxx，商品价格： xxx，商品数量：xxx"。
# 5.退出购物车



shopping_cart = {}
print("欢迎使用购物车")
while True:
    print(" 1 添加,2 修改,3 删除,4 查询,5 退出")
    choice = input("请选择你要进行的操作")
    if choice == "1":
        name = input("商品名称")
        if name in shopping_cart:
            print("该商品已在购物车之中，操作失败")
            continue
        price = input("商品金额")
        num   = input("商品数量")
        shopping_cart[name]={"price":price,"num":num}
        print(f"已添加：{shopping_cart[name]}")
    elif choice == "2":
        name = input("商品名称")
        if name not in shopping_cart:
            print("商品不存在")
        else:
            price = input("更改后金额")
            num   = input("更改后数量")
            shopping_cart[name]={"price":price,"num":num}
            print("修改成功")
    elif choice == "3":
        name = input("要删除的商品")
        if name in shopping_cart:
            del shopping_cart[name]
            print("已删除")
        else:
            print("暂无该商品")
    elif choice == "4":
        if not shopping_cart:
            print("购物车为空")
        else:
            for name ,item_data in shopping_cart.items():
                print(f"商品名称：{name}，商品价格：{item_data['price']}，商品数量：{item_data['num']}")
    elif choice == "5":
        print("已退出")
        break
    else:
        print("输入有误，请重新输入")











