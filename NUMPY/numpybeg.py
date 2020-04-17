import numpy as np

# Elementwise Operations

**1. Basic Operations**

**with scalars**

a = np.array([1, 2, 3, 4]) #create an array

a + 1

a ** 2

**All arithmetic operates elementwise**

b = np.ones(4) + 1

a - b

a * b

# Matrix multiplication

c = np.diag([1, 2, 3, 4])

print(c * c)
print("*****************")
print(c.dot(c))

**comparisions**

a = np.array([1, 2, 3, 4])
b = np.array([5, 2, 2, 4])
a == b

a > b

#array-wise comparisions
a = np.array([1, 2, 3, 4])
b = np.array([5, 2, 2, 4])
c = np.array([1, 2, 3, 4])

np.array_equal(a, b)

np.array_equal(a, c)

**Logical Operations**

a = np.array([1, 1, 0, 0], dtype=bool)
b = np.array([1, 0, 1, 0], dtype=bool)

np.logical_or(a, b)

np.logical_and(a, b)

**Transcendental functions:**

a = np.arange(5)

np.sin(a)   

np.log(a)

np.exp(a)   #evaluates e^x for each element in a given input

**Shape Mismatch**

a = np.arange(4)

a + np.array([1, 2])
