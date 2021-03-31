# REF: https://en.wikipedia.org/wiki/Test_functions_for_optimization
from cso import CSO

def himmelblaus_function(x, *args, **kwargs):
    return (((x[0] ** 2) + x[1] - 11) ** 2 ) + ((x[0] + (x[1] ** 2) - 7) ** 2 )

o = CSO(himmelblaus_function, lb=[-5, -5], ub=[5, 5],
        n_cats=500, smp=10, maxiter=200, cdc=1, mr=0.5)

best = o.run()

print(best)
