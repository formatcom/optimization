# REF: https://en.wikipedia.org/wiki/Test_functions_for_optimization
from cso import CSO

dimension = 3

def sphere_function(x, *args, **kwargs):
    return sum([a**2 for a in x])

o = CSO(sphere_function, lb=[-10] * dimension, ub=[10] * dimension,
            workers=1, threads=1, chunksize=500, maxiter=200,
            n_cats=500, mr=0.5, smp=10, cdc=1, srd=0.1, spc=False, omega=0.5)

best = o.run()

print(best)
