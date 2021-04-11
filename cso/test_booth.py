# REF: https://en.wikipedia.org/wiki/Test_functions_for_optimization
from cso import CSO


def booth_function(x, *args, **kwargs):
    return ( (x[0] + (2*x[1]) -7) ** 2 ) + (( (2 * x[0]) + x[1] - 5 ) ** 2 )

o = CSO(booth_function, lb=[-10, -10], ub=[10, 10],
            workers=1, theads=2, chunksize=300,
            cats=600, smp=10, maxiter=300, mr=0.5)

best = o.run()

print(best)
