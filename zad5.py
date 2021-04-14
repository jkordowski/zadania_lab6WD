import numpy as np

def funkcja(n):
    wektor = np.diag([i for i in range(n, 0, -1)],2)
    print(wektor)


funkcja(5)