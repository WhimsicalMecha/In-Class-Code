import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
x = sp.symbols('x')
f_input = input("Enter function in terms of x: ")
a = float(input("Enter the lower bound: "))
b = float(input("Enter the upper bound: "))
n = 1000
f = sp.sympify(f_input)
f_num = sp.lambdify(x, f, "numpy")
print("You entered:", f)
below = []
above = []

# Find critical points
df = sp.diff(f, x)
critical = sp.solve(df, x)
test_points = [a, b]
for c in critical:
    try:
        c_val = float(c)
        if a <= c_val <= b:
            test_points.append(c_val)
    except:
        pass
# Evaluate endpoints and critical points
values = []
for p in test_points:
    try:
        values.append(float(f.subs(x, p)))
    except:
        pass

# Rectangle bounds
xmin = a
xmax = b
ymin = min(values)
ymax = max(values)
# If function is flat
if ymin == ymax:
    ymin -= 1
    ymax += 1
A = (xmax - xmin) * (ymax - ymin)

# Generate random points in rectangle
x_points = np.random.uniform(xmin, xmax, n)
y_points = np.random.uniform(ymin, ymax, n)
# Sort random
for px, py in zip(x_points, y_points):
    fy = f_num(px)
    if np.isfinite(fy):
        if py <= fy:
            below.append((px, py))
        else:
            above.append((px, py))

# Monte Carlo estimate
hits = len(below)
mc_estimate = A * (hits / n)
exact_integral = sp.integrate(f, (x, a, b)).evalf()
print("\nTotal below:", len(below))
print("Total above:", len(above))
print("Monte Carlo H/M estimate:", mc_estimate)
print("sp.integrate:", exact_integral)

#PLOT
x_plot = np.linspace(xmin, xmax, 1000)
y_plot = f_num(x_plot)
width = xmax - xmin
height = ymax - ymin
base_size = 8
scale = base_size / max(width, height)
fig_w = max(4, width * scale)
fig_h = max(4, height * scale)
plt.figure(figsize=(fig_w, fig_h))

# Plot function
plt.plot(x_plot, y_plot, label="f(x)")

# Plot random points
if below:
    below_x, below_y = zip(*below)
    plt.scatter(below_x, below_y, s=20, label="Below curve")
if above:
    above_x, above_y = zip(*above)
    plt.scatter(above_x, above_y, s=20, label="Above curve")

# Plot rectangle bounds
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)

# Make plot scale match rectangle scale
plt.gca().set_aspect('equal', adjustable='box')

plt.xlabel("x")
plt.ylabel("y")
plt.title("Monte Carlo Integration Visualization")
plt.grid(True)

# Only show legend if labeled items exist
handles, labels = plt.gca().get_legend_handles_labels()
if handles:
    plt.legend()
plt.show()