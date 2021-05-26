# Assignment one: Given a certain altitude, output the appropriate values for the temp, pressure and density
# Author: Nikolaus Ricker

"""Libraries"""
import math

# ---------------------------------------------------------------------------------------------
"""Constants"""
g = 9.80665
R = 287.0
t0 = 288.15
p = 101325
a = [-0.0065, 0, 0.001, 0.0028, 0, -0.0028, -0.002]
h = [0, 11000, 20000, 32000, 47000, 51000, 71000, 86000]
# ---------------------------------------------------------------------------------------------
"""Functions"""


def get_p(a_, p_, dif):
    if a_ != 0:
        p_ = p_ * pow((t / t0), (-g / (a_ * R)))
    else:
        p_ = p_ * math.exp(-g * dif / (R * t))
    return p_


def new_temp():
    print("Do you want to define a new sea level temperature? (y/n)")
    ans_ = input()
    return ans_


def get_temp(h_, h_max, h0_, t_, a_):
    if h_ > h_max:
        t_ = t_ + a_ * (h_max - h0_)
    else:
        t_ = t_ + a_ * (h_ - h0_)
    return t_


# ---------------------------------------------------------------------------------------------
"""Variables"""
error = True
h1 = 0
# ---------------------------------------------------------------------------------------------
"""Program Start"""
# ---------------------------------------------------------------------------------------------
print("Hi, this is an ISA calculator. in what units do you want to calculate it?\n1. Meters\n2. Feet\n3. FL")
n = int(input('Give me a number: '))

while (n != 1) & (n != 2) & (n != 3):  # Checks for valid number
    n = int(input('Give me a valid number: '))
# ---------------------------------------------------------------------------------------------
"""Temperature"""
ans = new_temp()
while (ans != 'y') & (ans != 'n'):
    ans = new_temp()

if ans == 'y':
    t0 = float(input("What temperature in Kelvin?"))
    if t0 < 0:  # Checks for valid temperature
        t0 = float(input("Give a valid temperature"))
# ---------------------------------------------------------------------------------------------
"""Altitude"""
print("Give me the altitude in correct units")

while error:
    h1 = float(input("Give a valid height: "))
    # Conversion of units
    if n == 2:
        h1 = 0.3048 * h1
    elif n == 3:
        h1 = h1 * 100 * 0.3048

    error = False
    if (h1 < 0) | (h1 > 86000):
        error = True
# ---------------------------------------------------------------------------------------------
"""Troposphere"""  # Obtaining p and t for the applicable sections
t = get_temp(h1, h[1], h[0], t0, a[0])
p = get_p(a[0], p, 0)
t0 = t
"""Tropopause"""
if h1 > 11000:
    if h1 < 20000:
        p = get_p(a[1], p, h1-11000)
    else:
        p = get_p(a[1], p, 9000)
t0 = t
"""Stratosphere 1"""
if h1 > 20000:
    t = get_temp(h1, h[3], h[2], t, a[2])
    p = get_p(a[2], p, 0)
t0 = t
"""Stratosphere 2"""
if h1 > 32000:
    t = get_temp(h1, h[4], h[3], t, a[3])
    p = get_p(a[3], p, 0)
t0 = t
"""Stratopause"""
if h1 > 47000:
    if h1 < 51000:
        p = get_p(a[4], p, h1-47000)
    else:
        p = get_p(a[4], p, 4000)
t0 = t
"""Mesosphere"""
if h1 > 51000:
    t = get_temp(h1, h[6], h[5], t, a[5])
    p = get_p(a[5], p, 0)
t0 = t
if h1 > 71000:
    t = t + a[6] * (h1 - h[6])
    p = get_p(a[6], p, 0)
# ---------------------------------------------------------------------------------------------
"""Get rho"""
rho = p / (R * t)
# ---------------------------------------------------------------------------------------------
"""Return to original unit"""
if n == 2:
    h1 = h1 / 0.3048
elif n == 3:
    h1 = h1 / (1000 * 0.3048)
# ---------------------------------------------------------------------------------------------
"""Give results"""
print("At an altitude ", h1, ", the values given by the ISA are:\nPressure-", round(p, 3), "\nDensity-", round(rho, 7),
      "\nTemperature-", round(t, 1))
# ---------------------------------------------------------------------------------------------
dummy = input('Press enter to leave the ISA calculator')
print("Trial")
