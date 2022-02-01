import matplotlib.pyplot as plt
import numpy as np
import math


X = [i for i in range(100, 1901, 100)]

 
# Assign variables to the y axis part of the curve
y = []
z = []
  

with open("serial.txt", "r+") as rfile:
	data = rfile.readlines()
	for i in data:
		y.append(float(i))

with open("parallel.txt", "r+") as rfile:
	data = rfile.readlines()
	for i in data:
		z.append(float(i))

# Plotting both the curves simultaneously
plt.plot(X, y, color='r', label='SERIAL')
plt.plot(X, z, color='g', label='PARALLEL')
  
# Naming the x-axis, y-axis and the whole graph
plt.xlabel("TESTCASE")
plt.ylabel("TIME")
plt.title("TESTCASE / TIME")
  
# Adding legend, which helps us recognize the curve according to it's color
plt.legend()
  
# To load the display window
plt.show()
