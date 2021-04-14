import numpy as np

def funkcja(n):
    wynik = np.arange(n*n)
    i = 2
    for liczba in wynik:
        wynik[liczba] = i
        i *= 2
    return wynik

print(funkcja(3))
