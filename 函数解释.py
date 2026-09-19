import math

def menu():
    print("="*40)
    print("您好，欢迎使用物理公式计算世界，请选择你要使用的功能")
    print("1. 计算物体的运动（匀变速、自由落体）")
    print("2. 计算力与牛顿定律")
    print("3. 曲线运动、万有引力")
    print("4. 功、能量、动量")
    print("5. 电场计算")
    print("6. 恒定电流电路")
    print("7. 磁场、洛伦兹粒子圆周运动")
    print("0. 离开")
    print("="*40)

# 1 运动模块
def func_move():
    print("\n-----【物体运动计算】-----")
    print("1.匀变速位移 x = v0*t + 0.5*a*t*t")
    print("2.自由落体 h = 0.5*g*t*t")
    op = int(input("请选择子功能："))
    if op == 1:
        v0 = float(input("初速度v0："))
        a = float(input("加速度a："))
        t = float(input("时间t："))
        x = v0 * t + 0.5 * a * t ** 2
        print(f"位移 x = {x:.4f}")
    elif op == 2:
        t = float(input("下落时间t："))
        g = 9.8
        h = 0.5 * g * t * t
        print(f"下落高度 h = {h:.4f}")
    print("\n谢谢你的使用")

# 2 牛顿力学
def func_force():
    print("\n-----【力与牛顿定律】-----")
    print("1.合力 F合 = m*a")
    op = int(input("子功能选择："))
    if op ==1:
        m = float(input("质量m："))
        a = float(input("加速度a："))
        f = m * a
        print(f"合力 F合 = {f:.4f}")
    print("\n谢谢你的使用")

#3 曲线&万有引力
def func_orbit():
    print("\n-----【曲线运动、万有引力】-----")
    print("1.粒子圆周向心力 F = m*v*v/r")
    op = int(input("子功能选择："))
    if op ==1:
        m=float(input("质量m："))
        v=float(input("线速度v："))
        r=float(input("半径r："))
        f = m*v**2 / r
        print(f"向心力 = {f:.4f}")
    print("\n谢谢你的使用")

#4 功和动量
def func_energy():
    print("\n-----【功、能量动量】-----")
    print("1.动能 Ek = 1/2mv²")
    op = int(input("子功能选择："))
    if op ==1:
        m = float(input("质量m："))
        v = float(input("速度v："))
        ek = 0.5 * m * v**2
        print(f"动能 Ek = {ek:.4f}")
    print("\n谢谢你的使用")

#5电场
def func_electric():
    print("\n-----【电场计算】-----")
    print("1.匀强电场 U = E*d")
    op = int(input("子功能选择："))
    if op == 1:
        E = float(input("场强E："))
        d = float(input("距离d："))
        U = E * d
        print(f"电势差 U = {U:.4f}")
    print("\n谢谢你的使用")

#6电路
def func_circuit():
    print("\n-----【恒定电流电路】-----")
    print("1.欧姆定律 I = U/R")
    op = int(input("子功能选择："))
    if op ==1:
        U = float(input("电压U："))
        R = float(input("电阻R："))
        I = U / R
        print(f"电流 I = {I:.4f}")
    print("\n谢谢你的使用")

#7磁场（你的粒子周期公式！）
def func_magnetic():
    print("\n-----【磁场、带电粒子圆周运动】-----")
    print("1.粒子周期 T = 2πm/(B*q)")
    op = int(input("子功能选择："))
    if op == 1:
        B = float(input("磁场B："))
        q = float(input("电荷量q："))
        m = float(input("粒子质量m："))
        T = 2 * math.pi * m / (B * q)
        print(f"运动周期 T = {T:.4e}")
    print("\n谢谢你的使用")


#主循环
def main():
    while True:
        menu()
        choice = int(input("\n请输入功能序号："))
        if choice == 0:
            print("程序结束，再见！")
            break
        elif choice == 1:
            func_move()
        elif choice == 2:
            func_force()
        elif choice ==3:
            func_orbit()
        elif choice ==4:
            func_energy()
        elif choice ==5:
            func_electric()
        elif choice ==6:
            func_circuit()
        elif choice ==7:
            func_magnetic()
        else:
            print("输入无效，请输入0‑7之间数字！")
            print("\n谢谢你的使用")
        
        input("\n按下回车键，返回主菜单......")

if __name__ == "__main__":
    main()