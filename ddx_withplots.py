import sympy as sp
import matplotlib.pyplot as plt
h_vals = []
deriv_vals = []
f_input = input("Enter function in terms of x: ")
comp_x = float(input("Enter x of evaluation: "))
n = int(input("Enter number of h values: "))
h = [10**(-i) for i in range(n)]
x = sp.symbols('x')
f = sp.sympify(f_input)
f_num = sp.lambdify(x, f)
f_exact = sp.diff(f, x)
true_val = float(f_exact.subs(x, comp_x))
zero_h = None
for i in h:
    f_dx = ((f_num(comp_x + i) - f_num(comp_x - i))/(2*i))
    print("The estimate d/dx",f_input,"of",comp_x,"at", i , "is",f_dx)
    h_vals.append(i)
    deriv_vals.append(f_dx)
    if abs(f_dx) < 1e-12 and zero_h is None:
        zero_h = i
    plt.plot(h_vals, deriv_vals, marker='o')
plt.xlabel("h (step size)")
plt.ylabel("Estimated derivative")
plt.title("Derivative Approximation at each Step")
plt.xscale('log')
plt.gca().invert_xaxis()
plt.plot(h_vals, deriv_vals, marker='o', label="Numerical")
plt.axhline(y=true_val, linestyle='--', label="Exact")
if zero_h is not None:
    plt.axvline(x=zero_h, color='red', linestyle='--', label="Numerical = 0")
plt.xlabel("h (step size)")
plt.ylabel("Estimated derivative")
plt.title("Derivative Approximation vs Step Size")
plt.legend()
plt.show()