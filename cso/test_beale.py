# REF: https://en.wikipedia.org/wiki/Test_functions_for_optimization
import os

os.environ['OMP_NUM_THREADS'] = '1'
from cso import CSO

def beale_function(x, *args, **kwargs):
    return ( 1.5 - x[0] + x[0] * x[1]) ** 2 + \
            (2.25 - x[0] + ((x[0] * x[1]) ** 2)) ** 2 + \
            (2.625 - x[0] + ((x[0]) * x[1])**3) ** 2

o = CSO(beale_function, lb=[-4.5, -4.5], ub=[4.5, 4.5],
            workers=1, threads=1, maxiter=200,
            cats=500, mr=0.5, smp=10, cdc=1, srd=0.1, spc=False, omega=0.5)

best = o.run()

print(best)
