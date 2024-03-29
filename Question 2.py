
import time
import numpy as nump
import matplotlib.pyplot as p

def f(n):
    x = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            x = x + 1
    return x

# range of n values
n1 = nump.arange(1, 150)

# Allocate memory in advance for storing execution times
time1 = nump.zeros_like(n1, dtype=float)

# Measures the duration of the function for each given value of n
for i, n in enumerate(n1):
    starting_time = time.time()
    f(n)
    time1[i] = time.time() - starting_time


p.plot(n1, time1, 'o', markersize=4, label='Time taken to execute')
p.xlabel('n')
p.ylabel('Time (t)')
p.title('Execution Time Taken vs. n')

# polynomial curve 
coefficients = nump.polyfit(n1, time1, 2)
curve_fit = nump.polyval(coefficients, n1)

p.plot(n1, curve_fit, 'r-', linewidth=2, label='Polynomial Curve')
p.legend()
p.show()
