import numpy as geek

# 2x2 matrix with 1's on main diagonal
b = geek.eye(2, dtype=float)
print("Matrix b : \n", b)

# matrix with R=4 C=5 and 1 on diagonal
# below main diagonal
a = geek.eye(4, 4, k=0)
print("\nMatrix a : \n", a)
