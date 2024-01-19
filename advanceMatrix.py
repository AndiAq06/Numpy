import numpy as np

# membuat matrix dengan data tertentu
a = np.array(([1, 2, 3], [3, 4, 5]), dtype=float)
print(a)

# membuat array dengan menggunaka function


def kuadrat(baris, kolom):
    return kolom**2


def jumlah(baris, kolom):
    return (kolom + baris)


b = np.fromfunction(kuadrat, (1, 10), dtype=int)
print(b)
c = np.fromfunction(jumlah, (4, 4), dtype=int)
print(c)
