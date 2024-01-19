import numpy as np
b = np.zeros(2, dtype=int)
print("Matrix b: \n", b)

b = np.zeros([2, 2], dtype=int)
print("Matrix b: \n", b)

b = np.zeros((2,), dtype=[('x', 'float'), ('y', 'int')])
