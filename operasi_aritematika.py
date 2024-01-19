import numpy as np
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

anp = np.array([1, 2, 3, 4, 5])
bnp = np.array([6, 7, 8, 9, 10])

# Penjumlahan
penjumlahan = anp + bnp

# pengurangan
pengurangan = anp - bnp

# perkalian
perkalian = anp * bnp

# pembagian
pembagian = anp / bnp

# kuadrat
kuadrat = anp**2

# multidimensi array
c = np.array([(1, 2, 3), (4, 5, 6)])
d = np.array([(7, 8, 9), [-1, -2, -3]])
hasil = c + d
hasil = c - d
hasil = c * d
print(hasil)
