import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from scipy import constants
from decimal import Decimal as dec
from math import cos

# Объявление переменных и занесение их значений
M = 285000 # стартовая масса ракеты
M0 = 4600 # конечная масса на орбите
T = 910 # суммарное время работы ступеней
Fi = 3268861.02 # среднее значение силы тяги
g = constants.g # ускорение свободного падения
Cf = 0.34 # коэффицент сопротивления
S = constants.pi * ((10.3) / 2) ** 2 # площадь основания ракеты-носителя
p0 = 101325 # нормальное атмосферное давление
L = -0.0065 # среднее значение вертикальной компоненты градиента температуры 
T0 = 288.15 # стандартная температура воздуха
Mv = 0.0289644 # молярная масса воздуха
R = 8.31447 # универсальная газовая постоянная
Pi = constants.pi # число Пи

# Объявление функций
def A(t):
    return Fi / (M - ((M - M0) / T) * t)

def B(t):
    return g / cos(Pi * t / (2 * T))

def C(t, v):
    ro = (1 + (L * v**2 * cos(Pi * t / T)) / (2 * T0 * g))**(- g * Mv / R / L)
    temp = T0 + (L * v**2 * cos(Pi * t / T)) / (2 * g)
    return (Cf * S  * v**2 * p0 * ro * Mv) / (2 * R * temp * (M - ((M - M0) / T) * t) * cos(Pi * t / (2 * T)))

def dv_dt(t, v):
    return + A(t) - B(t) - C(t, v)

v0 = 0
t = np.linspace(0, 34, 1080) 
solve = integrate.solve_ivp(dv_dt, t_span = (0, max(t)), y0 = [v0], t_eval = t)
x = solve.t
y = solve.y[0]

plt.figure(figsize=(7, 6))
plt.plot(x, y, '-r', label="first")
plt.plot(x, y, '-r', label="v(t)")
plt.legend()
plt.grid(True)
plt.show() 