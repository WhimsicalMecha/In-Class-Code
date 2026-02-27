import numpy as np
import matplotlib.pyplot as plt

x = float(input("Enter initial value of x : "))
n = float(input("Enter max number of iteration : "))

#funtion being run = x^2 - x
def f(x):
    return x**2 + 2*x -15
def df(x):
    return 2*x + 2

MAX_ITER = n
itr = 0 #starting iteration value
result = f(x)
#hold values for plots
iterations = []
errors = []

#loop
while itr<MAX_ITER:
    itr+=1
    
    result = f(x)
    x_old = x  
    x = x - result/df(x)    
    dx = x - x_old
    
    iterations.append(itr)
    errors.append(abs(result))    
    print("iteration", itr, "result", result, "x =", x,"jump =", dx)
print(f"\nFinal approximation after {MAX_ITER} iterations: {x}")
plt.semilogy(iterations, errors, marker='o', linestyle='-', color='blue', label='Newton-Raphson')
plt.xlabel("Iteration Number (n) linear scale")
plt.ylabel("Absolute Error |f(x_n)|log scale")
plt.title("Convergence Speed: Linear vs Quadratic")
plt.grid(True)
plt.legend()
plt.show()
