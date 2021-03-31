from cso import CSO


def test_function(x, *args, **kwargs):
    return 20 * x[0] - 2 * (x[0] ** 2)

o = CSO(test_function, maximize=True,
        lb=[-10], ub=[10], n_cats=100, smp=10, maxiter=100, cdc=1, mr=0.5)

best = o.run()

print(best)
