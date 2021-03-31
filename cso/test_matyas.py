# REF: https://en.wikipedia.org/wiki/Test_functions_for_optimization
from cso import CSO

def matyas_function(x, *args, **kwargs):
    return 0.26 * ( x[0] ** 2 + x[1] ** 2 ) - 0.48 * x[0] * x[1]

o = CSO(matyas_function, lb=[-10, -10], ub=[10, 10],
        n_cats=500, smp=10, maxiter=200, cdc=1, mr=0.5)

best = o.run()

print(best)
