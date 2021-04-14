# REF: https://en.wikipedia.org/wiki/Knapsack_problem

import csv
import numpy as np

from cso import BCSO

FILEPATH = '../dataset/kp/large_scale/knapPI_3_200_1000_1'

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

    return c

def help_the_cat(cat, *args, **kwargs):

    # variables de ayuda
    w = 0
    x = cat[BCSO.HELP_CAT_POSITION].copy()

    # calculamos el peso
    for i, _ in enumerate(x):
        w = w + (x[i] * W[i])

    # Si no ha superado el maximo, retornamos el gato original
    if w <= M:
        return cat

    # Ayudamos un poco a nuestro gatito ( Yue )
    clon = cat

    w = 0

    # El clon lo iniciamos con cero items
    clon[BCSO.HELP_CAT_POSITION] = np.zeros(N)

    # dimensiones organizadas de manera aleatoria
    dimension = np.random.permutation(np.array((range(N))))

    for i in dimension:

        _w = w + (x[i] * W[i])

        if _w <= M:

            w = _w
            clon[BCSO.HELP_CAT_POSITION][i] = x[i]

    # calculamos el costo
    c = test_function(clon[BCSO.HELP_CAT_POSITION], *args, **kwargs)

    # ahora si actualizamos el gato
    clon[BCSO.HELP_CAT_COST] = c

    return clon



o = BCSO(test_function, dimension=N, maxiter=150, maximize=True, help_the_cat=help_the_cat,
                workers=1, threads=1, cats=500, mr=0.5, smp=20, cdc=0.7,
                pmo=0.7, spc=True, omega=0.5, weight=1)

best = o.run()


print(best[BCSO.BEST_FUNC_TEST_VALUE])

decode = []

for i, x in enumerate(best[BCSO.BEST_CAT_POSITION]):
    if x:
        decode.append(i + 1)

print(decode)
