# raw_ips = "192.168.1.1, 192.168.1.2, 192.168.1.1 , 10.0.0.1, 192.168.1.2,  , 10.0.0.1"
# one_ips = raw_ips.split(",")
# clean_list = []
# for item in one_ips:
#     clean_item = item.strip()
#     if clean_item != "":
#         clean_list.append(clean_item)
#
# result = list(set(clean_list))
# print(result)
#
#


# users = ["admin", "root", "test"]
# passwords = ["123456", "password", "admin"]
# login_list = []
# for user in users:
#     for password in passwords:
#         login_list.append({"user": user, "password": password})
# for login in login_list:
#     print(login)



def count_danger_ports(servers , danger_ports):
    """用于统计指定高危端口在每台服务器上出现的次数
    servers:嵌套列表，每台服务器的端口列表
    danger_ports:高危端口列表
    return:key为端口，value为次数
    """
    result = {}
    for port in danger_ports:
        count = 0
        for server in servers:
            if port in server:
                count += 1
        result[port]= count
    return result

servers = [
    [22, 80, 443, 3389],
    [80, 443, 22],
    [22, 80, 8080],
    [443, 3389],
    [22, 80, 443, 8080, 3389]
]
danger_ports = [22, 80, 443, 3389]
list = count_danger_ports(servers, danger_ports)
print(list)