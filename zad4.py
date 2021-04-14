import numpy as np

def funkcja(n, m):
    wynik = np.logspace(1, m, num=m, base=n)
    return wynik

print(funkcja(2, 4))
