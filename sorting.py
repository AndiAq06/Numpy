import numpy as np
a = np.floor(np.random.randn(1, 6)*10)

print(a)

print('nilai max dari a = ', a.max())
print('posisi max dari a = ', a.argmax())
print('nilai min dari a = ', a.max())
print('posisi min dari a = ', a.argmax())

print('mengurutkan nilai a')
print(np.sort(a))

# array 2 dimensi
a = np.floor(np.random.randn(2, 2)*10)

print(a)

print('nilai max dari a = ', a.max())
print('posisi max dari a = ', a.argmax())
print('nilai min dari a = ', a.max())
print('posisi min dari a = ', a.argmax())

print('mengurutkan nilai a')
print(np.sort(a))

# multitype
dtipe = [('nama', 'S10'), ('tinggi', int)]
data = [
    ('Ucup', 170),
    ('Otong', 150),
    ('Mario', 160)
]

a = np.array(data, dtype=dtipe)
print(a)

print(np.sort(a, order='tinggi'))
print(np.sort(a, order='nama'))
