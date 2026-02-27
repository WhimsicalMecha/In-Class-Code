import numpy as np
import matplotlib.pyplot as plt
import random

#Function
def f(x):
    return x**2 + 2*x - 15

#User Input
x0 = float(input("Enter initial x value: "))
MAX_ITER = int(input("Enter number of iterations: "))

#SEARCH PHASE: find second point using scaled random steps, biger exponent bigger random
print("\n--- SEARCH PHASE ---")
a = x0 #first = user
fa = f(a)
attempt = 1

while True:
    # Random step scaled by magnitude of f(a)
    scale = max(1.0, abs(fa))  #at least 1 to avoid tiny steps
    step = random.uniform(-scale, scale) #random scale based on range
    
    b = a + step
    fb = f(b)
    
    print(f"Attempt {attempt}: checking {b:.6f} (f={fb:.6e})")
    
    if fa * fb < 0:
        print(f"Sign change found between {a:.6f} (f={fa:.6e}) and {b:.6f} (f={fb:.6e})")
        break
    attempt += 1

#BISECTION ITERATIONS
print("\n--- BISECTION ITERATIONS ---")
errors = []
iterations = []

for itr in range(1, MAX_ITER + 1):
    #method
    midpoint = (a + b) / 2
    fmid = f(midpoint)
    
    iterations.append(itr)
    errors.append(abs(fmid))
    
    #Logging
    print(f"\nIteration {itr}")
    print(f"Current interval: [{a:.10f}, {b:.10f}]")
    print(f"Midpoint = {midpoint:.10f}")
    print(f"f(midpoint) = {fmid:.10e}")
    #logic
    if fa * fmid < 0:
        print("Sign change between a and midpoint → replacing b with midpoint")
        b = midpoint
        fb = fmid
    else:
        print("Sign change between midpoint and b → replacing a with midpoint")
        a = midpoint
        fa = fmid

root = (a + b) / 2
print(f"\nFinal approximation after {MAX_ITER} iterations: {root}")

plt.semilogy(iterations, errors, marker='o', linestyle='-', color='purple', label='Bisection (Dynamic Random Search)')
plt.xlabel("Iteration Number (n)")
plt.ylabel("Absolute Error |f(x_n)|")
plt.title("Bisection Method Convergence (Semi-Log Plot with Points)")
plt.grid(True)
plt.legend()
plt.show()