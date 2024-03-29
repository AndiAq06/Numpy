import numpy as np

A = np.array(([2, 3], [1, 2]))
Y = np.array([23, 14])
print(Y)

A_inv = np.linalg.inv(A)

# Menyelesaikan persamaan kuadrat
X1 = np.dot(A_inv, Y)
print(X1)

# cara lain
X2 = np.linalg.solve(A, Y)
print(X2)
