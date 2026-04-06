import sympy as sp
import matplotlib.pyplot as plt
x = sp.symbols('x')
allowed = {
    "x": x,
    "sin": sp.sin,
    "cos": sp.cos,
    "tan": sp.tan,
    "exp": sp.exp,
    "log": sp.log,
    "sqrt": sp.sqrt,
    "pi": sp.pi,
    "asin": sp.asin,
    "acos": sp.acos,
    "atan": sp.atan,
    "ln": sp.log,
    "e": sp.E
}

f_input = input("Enter function in terms of x: ")
comp_x = float(input("Enter x of evaluation: "))
h = [1, 0.1, 0.05, 0.01, 0.005, 0.001]
f = sp.sympify(f_input, locals=allowed)
f_num = sp.lambdify(x, f)
f_exact = sp.diff(f, x)
true_val = float(f_exact.subs(x, comp_x))

h_vals = []
f_eval = []
b_eval = []
c_eval = []
f_error = []
b_error = []
c_error = []

#loop1 eval
for i in h:
    f_f_dx = (f_num(comp_x + i) - f_num(comp_x)) / i
    b_f_dx = (f_num(comp_x) - f_num(comp_x - i)) / i
    c_f_dx = (f_num(comp_x + i) - f_num(comp_x - i)) / (2 * i)

    h_vals.append(i)
    f_eval.append(f_f_dx)
    b_eval.append(b_f_dx)
    c_eval.append(c_f_dx)

#loop2 error
for i in range(len(h_vals)):
    f_e = abs((f_eval[i] - true_val) / true_val) * 100
    b_e = abs((b_eval[i] - true_val) / true_val) * 100
    c_e = abs((c_eval[i] - true_val) / true_val) * 100

    f_error.append(f_e)
    b_error.append(b_e)
    c_error.append(c_e)

min_f = min(f_error)
min_f_pos = f_error.index(min_f)
min_b = min(b_error)
min_b_pos = b_error.index(min_b)
min_c = min(c_error)
min_c_pos = c_error.index(min_c)


plt.figure()
plt.plot(h_vals, c_eval, marker='o', label="Central Difference")
plt.plot(h_vals, f_eval, marker='o', label="Forward Difference")
plt.plot(h_vals, b_eval, marker='o', label="Backward Difference")
plt.axhline(y=true_val, linestyle='--', label="Exact Derivative")
plt.xlabel("h (step size)")
plt.ylabel("Estimated derivative")
plt.title("Derivative Approximation vs Step Size")
plt.xscale('log')
plt.yscale('log')
plt.gca().invert_xaxis()
plt.legend()
plt.show()
plt.figure()
plt.plot(h_vals, c_error, marker='o', label="Central Difference Error")
plt.plot(h_vals, f_error, marker='o', label="Forward Difference Error")
plt.plot(h_vals, b_error, marker='o', label="Backward Difference Error")
plt.xlabel("h (step size)")
plt.ylabel("Percent error")
plt.title("Percent Error vs Step Size")
plt.xscale('log')
plt.yscale('log')
plt.gca().invert_xaxis()
plt.legend()
plt.show()

print("Forward Difference lowest error =", min_f, "% at h =", h_vals[min_f_pos])
print("Backward Difference lowest error =", min_b, "% at h =", h_vals[min_b_pos])
print("Central Difference lowest error =", min_c, "% at h =", h_vals[min_c_pos])