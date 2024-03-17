import sympy as sp

# 创建符号变量
a, b, c, d, e, f, g, m = sp.symbols('a b c d e f g m')
#CO2,H2O,CO,H2,N2,HCl,SO2,O2,OH,NO,H,Cl,Al2O3

Nc = 11.2738
Nh = 40.8672
No = 25.8632
Nn = 5.7692
Ncl = 5.7692

Kp = 7.008
Kp1h2o = 0.02233
Kp2h2o = 0.02091
Kph2 = 0.006649
Kphcl = 4.5983 * (10**(-3))
Kpno = 0.008786

h, i, j, k, l = (0,) * 5
temp = 0

def equations():
    global a, b, c, d, e, f, g, m, h, i, j, k, l, temp

# 定义方程组
    equations = [
        sp.Eq(g, 2.4177),
        sp.Eq(m, 0.9266),
        sp.Eq(a + c, Nc),
        sp.Eq(2*b +2*d, Nh - f - i - k),
        sp.Eq(2*a + b + c,No - 2*g - 3*m - 2*h - i - j),
        sp.Eq((c*b)/(a*d), Kp),
        sp.Eq(2*e, Nn - j),
        sp.Eq(f, Ncl - l),
        # sp.Eq(h, 0),
        # sp.Eq(i, 0),
        # sp.Eq(j, 0),
        # sp.Eq(k, 0),
        # sp.Eq(l, 0),
    ]

    # 解方程组
    solutions = sp.solve(equations, (a, b, c, d, e, f, g, m))

    # 打印解
    print("解为:", solutions)
    for i1 in solutions:
        if not any(num < 0 for num in i1):
            print(i1)
            global ng
            a, b, c, d, e, f, g, m = i1
            if temp == 0:
                ng = sum(i1) - m
                temp = 1
            else:
                ng = sum(i1) - m + ng
            print(ng)
            print(a, b, c, d, e, f, g, h, i, j, k, l, m)
            h, i, j, k, l = sp.symbols('h i j k l')
            return ng

ngg = equations()

h, i, j, k, l = sp.symbols('h i j k l')
def equations1():
    global a, b, c, d, e, f, g, m, h, i, j, k, l, ng
    p_ng = 70 / ng
    equations1 = [
        sp.Eq(h, (b/d)**2 * (Kp1h2o**2) * (p_ng**(-1))),
        sp.Eq(i, (b/(d**0.5)) * Kp2h2o * (p_ng**(-0.5))),
        sp.Eq(k, (d*Kph2)**0.5 * (p_ng**(-0.5))),
        sp.Eq(l, (f/k) * Kphcl * (p_ng**(-1))),
        sp.Eq(j, (e*h*Kpno)**0.5),
    ]

    solutions1 = sp.solve(equations1, (h, i, j, k, l))
    print("解为:", solutions1)
    for i2 in solutions1:
        if not any(num < 0 for num in i2):
            print(i2)
            h, i, j, k, l = i2
            ng = sum(i2)
            print(ng)
            a, b, c, d, e, f, g, m = sp.symbols('a b c d e f g m')

equations1()
# while 1:
#     ngg1 = equations()
#     equations1()
#     if abs(ngg1-ngg)/ngg1 < 0.0001:
#         print(ngg1)
#         break
#     ngg = ngg1


equations()
equations1()
equations()
equations1()
equations()
equations1()
equations()
