import csv
from setcover import Greedy

FILEPATH = '../dataset/scp/set_cover_5.txt'
DEBUG = True

dataraw = []
with open(FILEPATH) as f:
    dataraw = [[int(x) for x in v] for v in list(csv.reader(f, delimiter=' '))]

n_group = dataraw[0][0]
n_elem = dataraw[0][1]

dataraw = dataraw[1:]

cost = [c[0] for c in dataraw]    # Costos
dataset = [s[1:] for s in dataraw]      # lista con todos los conjuntos


o = Greedy(n_group, n_elem, cost, dataset, debug=True)

r = o.run()

print()
print(r)
