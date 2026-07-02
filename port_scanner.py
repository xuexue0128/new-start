import socket

def scan_port(ip, port):
    """检查单个窗口是否开放
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except Exception:
        return False

def scan_ports(ip,start_port,end_port):
    """扫描指定IP的端口范围
    return: 开放端口列表
    """
    open_ports = []
    print(f"正在扫描{ip}的端口{start_port}——{end_port}")
    for port in range(start_port,end_port+1):
        if scan_port(ip,port):
            open_ports.append(port)
            print(f"Port {port} is open")
    return open_ports
def main():
    print("="*40)
    print("简易端口扫描器")
    print("="*40)

    target_ip   = input("请输入目标IP地址")
    start       = int(input("请输入起始端口"))
    end         = int(input("请输入结束端口"))

    print(f"\n目标：{target_ip}")
    print(f"端口范围{start}-{end}")
    print("-"*40)

    open_ports = scan_ports(target_ip,start,end)

    print("-"*40)
    if open_ports:
        print(f"find {len(open_ports)} open ports")
        for port in open_ports:
            print(f"{port} ")
    else:

        print("not find any open ports")

    print("=" * 40)

if __name__ == "__main__":
    main()
