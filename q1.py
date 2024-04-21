import numpy as np

#linespace
x = np.linspace(0,100,11)
print(x)

#arrange
y = np.arange(0,101,10)
print(y)

#rearange the first 10 elements of y into a 5x2 array
y =y[:-1]
z = y.reshape(5,2)
print(z)
