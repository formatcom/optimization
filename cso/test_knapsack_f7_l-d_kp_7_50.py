# REF: https://en.wikipedia.org/wiki/Knapsack_problem

import csv
import numpy as np

from cso import BCSO

FILEPATH = '../dataset/kp/low-dimensional/f7_l-d_kp_7_50'

W = 0      # pesos
U = 0      # utilidades
N = 0      # numero de objetos
M = 0      # peso maximo

with open(FILEPATH, 'r') as f:
    data = np.array(list(csv.reader(f, delimiter=' ')), dtype=float)

    N = int(data[0][0])
    M = data[0][1]

    data = data[1:]

    U = data[:, 0]
    W = data[:, 1]


print()
print(FILEPATH)
print()
print('N', N)
print('W', W)
print('U', U)
print('W Max', M)
print()

def test_function(x, *args, **kwargs):

    # se calcula el costo
    c = 0
    for i, _ in enumerate(x):
        c = c + (x[i] * U[i])

    w = 0
    for i, _ in enumerate(x):
        w = w + (x[i] * W[i])

    # penalizo sobrepasar el peso maximo
    return c if w <= M else 0


o = BCSO(test_function, dimension=N, maxiter=150, maximize=True,
                workers=1, threads=1, cats=500, mr=0.5, smp=20, cdc=0.7,
                pmo=0.7, spc=False, omega=0.5, weight=1)

best = o.run()


print(best[BCSO.BEST_FUNC_TEST_VALUE])

decode = []

for i, x in enumerate(best[BCSO.BEST_CAT_POSITION]):
    if x:
        decode.append(i + 1)

print(decode)
