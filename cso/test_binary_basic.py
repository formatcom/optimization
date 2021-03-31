from cso import BCSO

dataset = [10, -10, 20, 1, 3, 25, -100, 20]

def test_function(x, *args, **kwargs):

    c = 0
    for i, f in enumerate(x):
        if f == 1:
            c = c + dataset[i]

    return c

omin = BCSO(test_function,
        dimension=len(dataset), maximize=False, n_cats=100, smp=10, maxiter=100, cdc=1, mr=0.5)
omax = BCSO(test_function,
        dimension=len(dataset), maximize=True, n_cats=100, smp=10, maxiter=100, cdc=1, mr=0.5)

best_min = omin.run()
best_max = omax.run()

print(dataset)
print()
print('min', best_min)
print()
print('max', best_max)
