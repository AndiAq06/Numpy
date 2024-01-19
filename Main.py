import numpy as np

# Membuat vector
a = np.array([1, 2, 3, 4, 5])
b = np.array([1.5, 2.5, 5, 6, 7])

# Membuat vektor dengan range
c = np.arange(1, 10, 2)

# Membuat linear space
d = np.linspace(1, 10, 4)

# array multidimensi/matrix
e = np.array([(1, 2, 3), (4, 5, 6)])

#  matrix dengan nilai 0
f = np.zeros((5, 5))

#  matrix dengan nilai satu
g = np.ones((5, 5))

# matrix identitas
h = np.identity(3)
h = np.eye(3)

# Display
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
