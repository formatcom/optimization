# REF: https://en.wikipedia.org/wiki/Test_functions_for_optimization
import os

os.environ['OMP_NUM_THREADS'] = '1'
from cso import CSO

def matyas_function(x, *args, **kwargs):
    return 0.26 * ( x[0] ** 2 + x[1] ** 2 ) - 0.48 * x[0] * x[1]


o = CSO(matyas_function, lb=[-10, -10], ub=[10, 10],
            workers=1, threads=1, maxiter=200,
            cats=500, mr=0.5, smp=10, cdc=1, srd=0.1, spc=False, omega=0.5)

best = o.run()

print(best)
