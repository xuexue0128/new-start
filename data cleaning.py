# 去重：把重复的密码删掉（比如 admin 和 123456 只保留一个）
# 过滤空值：把空字符串（比如两个逗号中间的空值 ,, 和末尾的空值）过滤掉
# 长度限制：密码长度必须 大于等于 4 位（因为实际爆破中，长度小于4的密码几乎没有意义）。提示：用 len(x)
raw_data = "admin,123456,,password,admin,root,123456,root,teer,abc,,password,123,admin"
new_list = raw_data.split(",")
clean_list = []
for num in new_list:
    if num not in clean_list and raw_data != "" and  len(num) >= 4 :
        clean_list.append(num)
print(clean_list)