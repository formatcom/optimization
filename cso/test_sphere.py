# REF: https://en.wikipedia.org/wiki/Test_functions_for_optimization
from cso import CSO

dimension = 3

def sphere_function(x, *args, **kwargs):
    return sum([a**2 for a in x])

o = CSO(sphere_function, lb=[-10] * dimension, ub=[10] * dimension,
        n_cats=500, smp=10, maxiter=200, cdc=1, mr=0.5)

best = o.run()

print(best)
