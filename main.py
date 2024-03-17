import sympy as sp

# 创建符号变量
a, b, c, d, e, f, g, m = sp.symbols('a b c d e f g m')
#CO2,H2O,CO,H2,N2,HCl,SO2,O2,OH,NO,H,Cl,Al2O3

Nc = 11.2738
Nh = 40.8672
No = 25.8632
Nn = 5.7692
Ncl = 5.7692

Kp = 6.811
Kp1h2o = 0.006037
Kp2h2o = 0.004625
Kph2 = 0.0006284
Kphcl = 0.4472 * (10**(-3))
Kpno = 0.003391

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
    ]

    # 解方程组
    solutions = sp.solve(equations, (a, b, c, d, e, f, g, m))

    for i1 in solutions:
        if not any(num < 0 for num in i1):
            global ng
            a, b, c, d, e, f, g, m = i1
            if temp == 0:
                ng = sum(i1) - m
                temp = 1
            else:
                ng = sum(i1) - m + ng
            print(a, b, c, d, e, f, g, h, i, j, k, l, m)
            h, i, j, k, l = sp.symbols('h i j k l')

def equations1():
    global a, b, c, d, e, f, g, m, h, i, j, k, l, ng
    p_ng = 70.92 / ng
    equations1 = [
        sp.Eq(h, (b/d)**2 * (Kp1h2o**2) * (p_ng**(-1))),
        sp.Eq(i, (b/(d**0.5)) * Kp2h2o * (p_ng**(-0.5))),
        sp.Eq(k, (d*Kph2)**0.5 * (p_ng**(-0.5))),
        sp.Eq(l, (f/k) * Kphcl * (p_ng**(-1))),
        sp.Eq(j, (e*h*Kpno)**0.5),
    ]

    solutions1 = sp.solve(equations1, (h, i, j, k, l))
    for i2 in solutions1:
        if not any(num < 0 for num in i2):
            h, i, j, k, l = i2
            ng = sum(i2)
            a, b, c, d, e, f, g, m = sp.symbols('a b c d e f g m')
equations()
print('第一次')
equations1()
equations()
print('第二次')
equations1()
equations()
print('第三次')
equations1()
equations()
print('第四次')
equations1()
equations()
