import sympy as sp
f_input = input("Enter function in terms of x: ")
comp_x = float(input("Enter x of evaluation: "))
h = 0.001
x = sp.symbols('x')
f = sp.sympify(f_input)
f_num = sp.lambdify(x, f)
f_dx = ((f_num(comp_x + h) - f_num(comp_x - h))/(2*h))
print("The estimate d/dx",f_input,"of",comp_x,"at", h , "is",f_dx)