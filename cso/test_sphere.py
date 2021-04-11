# REF: https://en.wikipedia.org/wiki/Test_functions_for_optimization
import os

os.environ['OMP_NUM_THREADS'] = '1'

from cso import CSO

dimension = 3

def sphere_function(x, *args, **kwargs):
    return sum([a**2 for a in x])

o = CSO(sphere_function, lb=[-10] * dimension, ub=[10] * dimension,
            workers=3, threads=2, maxiter=200,
            cats=500, mr=0.5, smp=10, cdc=1, srd=0.1, spc=False, omega=0.5)

best = o.run()

print(best)
