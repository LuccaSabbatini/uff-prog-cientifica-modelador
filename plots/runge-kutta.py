import matplotlib.pyplot as plt

a = 0
b = 4
n = 4
h = (b - a) / n
alpha = 2

x = []
y = []
yc = []
yc.append(alpha)
yrk = []
yrk.append(alpha)


def func_1(x):
    return x * x + 2


def func_2(x):
    return 2 * x


for i in range(n + 1):
    xi = i * h
    x.append(xi)
    y.append(func_1(xi))

for i in range(n):
    yi = yc[i] + h * func_2(x[i])
    yc.append(yi)

a1 = 0.5
a2 = 0.5
p1 = 1
q11 = 1

for i in range(n):
    k1 = func_2(x[i])
    yr = yrk[i] + q11 * k1 * h
    k2 = func_2(x[i] + p1 * h)
    yrk.append(yrk[i] + h * (a1 * k1 + a2 * k2))

plt.plot(x, y, x, yc, x, yrk)
plt.show()
