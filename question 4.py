#Find the approximate (eye ball it) location of "n_0" . Do this by zooming in on your plot and indicating on the plot where n_0 is and why you picked this value. Hint: I should see data that does not follow the trend of the polynomial you determined in #2.

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
times = nump.zeros_like(n1, dtype=float)

# Measures the duration of the function for each given value of n
for i, n in enumerate(n1):
    starting_time = time.time()
    f(n)
    times[i] = time.time() - starting_time

# Plot the data
p.plot(n1, times, 'o', markersize=4, label='Time taken to execute')
p.xlabel('n')
p.ylabel('Time (t)')
p.title('Execution Time Taken vs. n')

# Polynomial curve
coefficients = nump.polyfit(n1, times, 2)
curve_fit = nump.polyval(coefficients, n1)

p.plot(n1, curve_fit, 'r-', linewidth=2, label='Polynomial Curve')

# Zoom in on the plot (adjust xlim and ylim based on your observations)
p.xlim(0, 75)
p.ylim(0, 0.005)

# Mark the approximate location of n_0
n_0 = 10
p.annotate(f'$n_0 = {n_0}$', xy=(n_0, curve_fit[n_0]), xytext=(n_0, curve_fit[n_0] + 0.001), arrowprops=dict(facecolor='black', shrink=0.05),)

# Display the plot
p.legend()
p.show()
