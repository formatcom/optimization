# REF: https://en.wikipedia.org/wiki/Knapsack_problem

import csv
import numpy as np

FILEPATH = '../dataset/kp/knapsack_wiki.csv'

W = 0      # pesos
U = 0      # utilidades
N = 0      # numero de objetos
M = 0      # peso maximo

with open(FILEPATH, 'r') as f:
    data = np.array(list(csv.reader(f, delimiter=' ')), dtype=int)

    N = data[0][0]
    M = data[0][1]

    data = data[1:]

    U = data[:, 0]
    W = data[:, 1]

# buffer (N+1) x (M+1)
R = [[0 for m in range(M+1)] for i in range(N+1)]

"""
R[x] <- x es el numero de objetos que ha introducido en orden

ej:
    - R[0] ningun objeto, todos los pesos a 0
    - R[1] se analiza el primer objeto de la lista,

        se introduce a la lista si se cumple que el peso (m) es
        mayor al peso del primer objeto en la lista y ademas este
        objeto tiene mas utilidad que el objeto que ya esta guardado
        en esta posición.

        NOTA: el valor guardado es la utilidad del objeto mas la utilidad
        del peso restante guardado anteriormente. U[i-1] + R[i-1][m-W[i-1]].

    - R[N] todos los objetos de la lista analizados.


R[x][y] <- y almacena la utilidad por peso, deacuerdo a el valor de x

 esto quiere decir que en R[N][M] tenemos la mejor solución, pero podemos
ver otras alternativas como R[N][5] para todos los objetos con peso max 5
"""

for i in range(1, N+1):
    for m in range(1, M+1):

        if W[i-1] <= m and U[i-1] + R[i-1][m-W[i-1]] > R[i-1][m]:
            R[i][m] = U[i-1] + R[i-1][m-W[i-1]]
        else:
            R[i][m] = R[i-1][m]

objs = []
m = M
for i in reversed(range(N)):
    if R[i][m] != R[i-1][m] and R[i][m] == U[i-1] + R[i-1][m-W[i-1]]:
        objs.append(i)
        m -= W[i-1]

print()
print(FILEPATH)
print()
print('W', W)
print('U', U)
print('W Max', M)
print('U Max', R[N][M])
print('O', objs)
print()
