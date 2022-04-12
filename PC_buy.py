def cpu_cost():
    print("1 : intel i7, 2 : intel i5, 3 : AMD Ryzen7, 4 : AMD Ryzen5")
    while True:
        cpu = int(input("CPU 선택(1~4) : "))
        if cpu == 1:
            return 406400
        elif cpu == 2:
            return 180400
        elif cpu == 3:
            return 373200
        elif cpu == 4:
            return 171300

def mainboard_cost():
    print("1 : ASUS PRIME B365M-A, 2 : MSI H310M PRO-VD PLUSE, 3 : GIGABYTE B365M DS3H")
    while True:
        mainboard = int(input("메인모드 선택(1~3) : "))
        if mainboard == 1:
            return 91000
        elif mainboard == 2:
            return 63900
        elif mainboard == 3:
            return 83400

def memory_cost():
    print("1 : 16G, 2 : 8G")
    while True:
        memory = int(input("메모리 종류 선택(1~2) : "))
        if memory == 1:
            return 59000
        elif memory == 2:
            return 28700

def harddisk_cost():
    print("1 : 4TB, 2 : 2TB, 3 : 1TB")
    while True:
        harddisk = int(input("하드디스크 종류 선택(1~3) : "))
        if harddisk == 1:
            return 108900
        elif harddisk == 2:
            return 62900
        elif harddisk == 3:
            return 46400

def monitor_cost():
    print("1 : Samsung 28 inch, 2 : Samsung 24 inch, 3 : LG 28 inch, 4 : LG 24 inch")
    while True:
        monitor = int(input("모니터 종류 선택(1~4) : "))
        if monitor == 1:
            return 350000
        elif monitor == 2:
            return 200000
        elif monitor == 3:
            return 340000
        elif monitor == 4:
            return 210000

overall_cost = 0 # 전체 가격 초기화
overall_cost = cpu_cost() + mainboard_cost() + memory_cost() + \
    harddisk_cost() + monitor_cost()

print("총", overall_cost, '원') # 전체 가격 출력