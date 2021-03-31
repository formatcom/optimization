# REF: https://en.wikipedia.org/wiki/Test_functions_for_optimization
from cso import CSO


def beale_function(x, *args, **kwargs):
    return ( 1.5 - x[0] + x[0] * x[1]) ** 2 + \
            (2.25 - x[0] + ((x[0] * x[1]) ** 2)) ** 2 + \
            (2.625 - x[0] + ((x[0]) * x[1])**3) ** 2

o = CSO(beale_function,
        lb=[-4.5, -4.5], ub=[4.5, 4.5], n_cats=100, smp=10, maxiter=100, cdc=0.5, mr=0.5, omega=0.5)

best = o.run()

print(best)
