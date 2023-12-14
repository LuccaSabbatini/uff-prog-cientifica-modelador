import matplotlib.pyplot as plt

a = 0
b = 4
n = 100
h = (b - a) / n
alpha = 2

x = []
y = []
yc = []
yc.append(alpha)


def func_1(x):
    return x * x + 2


for i in range(n + 1):
    xi = i * h
    x.append(xi)
    y.append(func_1(xi))


def func_2(x):
    return 2 * x


for i in range(n):
    yi = yc[i] + h * func_2(x[i])
    yc.append(yi)

plt.plot(x, y, x, yc)
plt.show()
