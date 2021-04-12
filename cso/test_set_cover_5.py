# REF: https://es.wikipedia.org/wiki/Problema_del_conjunto_de_cobertura

import os

os.environ['OMP_NUM_THREADS'] = '1'
import csv
import numpy as np

from cso import BCSO

FILEPATH = '../dataset/scp/set_cover_5.txt'

dataraw = []
with open(FILEPATH) as f:
    dataraw = [[int(x) for x in v] for v in list(csv.reader(f, delimiter=' '))]

n_group = dataraw[0][0]
n_elem = dataraw[0][1]

dataraw = dataraw[1:]

cost = [c[0] for c in dataraw]    # Costos
dataset = [s[1:] for s in dataraw]      # lista con todos los conjuntos

matrix = np.zeros(shape=(n_elem, n_group), dtype=np.int)

for j, group in enumerate(dataset):
    for i in group:
        if i:
            matrix[i-1][j] = 1

print("#" * 40)
print("dataset")
print()
for i, group in enumerate(dataset):
    print("[{:04d}] {}".format(i+1, group))
print("#" * 40)
print("cost")
print()
print(cost)
print("#" * 40)
print("matrix")
print()
print(matrix)
print()

def test_function(x, *args, **kwargs):

    # se calcula el costo
    c = 0
    for j, _ in enumerate(x):
        c = c + (x[j] * cost[j])

    # penalizo no cubrir algun elemento
    for i, _ in enumerate(matrix):

        n = 0
        for j, _ in enumerate(x):
            n = n + ( matrix[i][j] * x[j] )

        if n == 0:
            c = c + 1000

    return c


o = BCSO(test_function, dimension=n_group, maxiter=300,
                workers=1, threads=1, cats=150, mr=0.5, smp=20, cdc=0.7,
                pmo=0.1, spc=False, omega=0.5, weight=1)

best = o.run()

print(best[BCSO.BEST_FUNC_TEST_VALUE])

decode_covering = []

for i, x in enumerate(best[BCSO.BEST_CAT_POSITION]):
    if x:
        decode_covering.append(i + 1)

print(decode_covering)
