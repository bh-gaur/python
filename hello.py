# This will print Hello, world!

# print("Hello, world!")

# print("test".__dir__())

import time
import numpy as np

arr = np.arange(1000000)
print(arr * 2)   # No loop needed


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)   # [5 7 9]
print(a * b)   # [ 4 10 18]


m = np.array([[1, 2], [3, 4]])
print(m)
