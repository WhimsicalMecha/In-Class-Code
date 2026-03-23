import sympy as sp 
import numpy as np
x = sp.symbols('x')
f_input = x**2 -1
a = float(0)
b = float(10)
n = int(1000000)
f = sp.sympify(f_input) 
print("You entered:", f)
f_num = sp.lambdify(x, f)
#x_i = np.random.uniform(a, b, n) #random list values
#AVG_L = ((sum(f_num(x_i)))/n)/2
#AVG_W = sum(x_i)/n
#A = (AVG_L/AVG_W)
x_i = np.random.uniform(a, b, n)   # random 
A = (b - a) * np.mean(f_num(x_i))      
print("monte calro sum :",A)
print("sp.integrate    :",sp.integrate(f, (x, a, b)))