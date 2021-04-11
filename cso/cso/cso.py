# Creado por Vinicio Valbuena
#
# REF: https://www.researchgate.net/publication/221419703_Cat_Swarm_Optimization
# REF: https://downloads.hindawi.com/journals/cin/2020/4854895.pdf
# REF: https://www.researchgate.net/publication/258510186_Discrete_binary_cat_swarm_optimization_algorithm
# REF: https://www.researchgate.net/publication/282307581_A_Binary_Cat_Swarm_Optimization_Algorithm_for_the_Non-Unicost_Set_Covering_Problem
# REF: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6393876/
# REF: http://opac.pucv.cl/pucv_txt/txt-6500/UCD6603_01.pdf

from multiprocessing import Process, Queue
from concurrent.futures import ThreadPoolExecutor
from functools import partial

import numpy as np
from numpy.random import default_rng, SeedSequence

class _CSO:

    MODE_TRACING = 0 # Gato buscando y cazando
    MODE_SEEKING = 1 # Gato descansando, mirando alrededor y buscando la siguiente posicion a moverse

    CAT_POSITION = 0
    CAT_VELOCITY = 1
    CAT_FLAG = 2

    BEST_PROCESS_ID = 0
    BEST_CAT_INDEX = 1
    BEST_CAT_POSITION = 2
    BEST_FUNC_TEST_VALUE = 3

    def valid_args_limit(self):
        pass

    def init_positions(self, cats):
        pass

    def init_velocity(self, cats):
        pass

    def apply_mutation(self, cats):
        pass

    # Gato buscando / cazando
    def mode_tracing(self, mask, cats, best):
        pass

    # Gato descansando, mirando alrededor y buscando la siguiente posicion para moverse
    def mode_seeking(self, mask, i, cats, best):

        ### 1.- Se crean SMP copias de el gato (posición)
        copycat = np.array([cats[self.CAT_POSITION][mask][i].copy()] * self.smp)

        ### 2.- Aplicar la formula de mutación
        self.apply_mutation(copycat)

        if self.spc:
            copycat = np.append(copycat, [cats[self.CAT_POSITION][mask][i].copy()], axis=0)

        ### 3.- Evaluar FS (Función fitness) para todos los candidatos

        # Si todos los elementos son iguales la propabilidad para todos es 1
        fs = np.array(list(self.threads.map(
                                self.func_test,
                                copycat, chunksize=self.chunksize)))

        if (fs == fs[0]).all():
            p = np.array([1] * len(copycat))

        else:
            fsmin = np.min(fs)
            fsmax = np.max(fs)
            fsb = fsmax

            p = abs(fs - fsb) / ( fsmax - fsmin )

        ### 4.- Seleccionamos la nueva posición

        # selector de gatos con numpy mask
        _cats = cats[self.CAT_POSITION][mask]

        _cats[i] = copycat[p.argmax()]

        cats[self.CAT_POSITION][mask] = _cats

    def __worker__(self, pid, random, maxiter, queue):

        self.random = random # random con soporte a multiprocess

        ### 1.- Especificar limites maximos y minimos
        self.valid_args_limit()

        # Mascara de mutación, utilizada en el modo seeking
        self.n_mutations = int(self.cdc * self.dimension)
        self.maskm = ( [True] * self.n_mutations  ) + \
                        ( [False] * (self.dimension - self.n_mutations) )


        ### 2.- Generar N gatos aleatorios y posicionar en el espacio dimensional M
        cats = [[]] * 3

        self.init_positions(cats)

        ### 2.1.- Inicializar velocidad
        self.init_velocity(cats)

        ### 3.- Clasificar aleatoriamente a los gatos segun el mr
        cats[self.CAT_FLAG] = ( [self.MODE_TRACING] * int(self.n_cats * self.mr) ) + \
                              ( [self.MODE_SEEKING] * int(self.n_cats * (1 - self.mr)))

        cats[self.CAT_FLAG] = self.random.permutation(cats[self.CAT_FLAG])


        ### 4.- Evaluar la función fitness para todos los gatos
        best = [[]] * 4

        best[self.BEST_PROCESS_ID] = pid
        best[self.BEST_CAT_INDEX] = -1
        best[self.BEST_CAT_POSITION] = list()
        best[self.BEST_FUNC_TEST_VALUE] = np.inf


        # variable de ayuda, valor inf en fitness
        fs = np.ones(self.n_cats)*np.inf

        it = 0
        while True:

            newfs = np.array(list(self.threads.map(
                                    self.func_test,
                                    cats[self.CAT_POSITION],
                                    chunksize=self.chunksize)))

            ### 4.1 Guardar la mejor posición en memoria
            _update = newfs < fs

            fs[_update] = newfs[_update]

            _index_min = np.argmin(fs)

            if fs[_index_min] < best[self.BEST_FUNC_TEST_VALUE]:
                best[self.BEST_CAT_INDEX] = _index_min
                best[self.BEST_FUNC_TEST_VALUE] = fs[_index_min]
                best[self.BEST_CAT_POSITION] = cats[self.CAT_POSITION][_index_min].copy()

            if it == maxiter:
                break

            ### 5.- Aplicar comportamientos
            mask_tracing = cats[self.CAT_FLAG] == self.MODE_TRACING
            mask_seeking = ~mask_tracing

            # Gato en estado alerta, cazando su presa
            self.mode_tracing(mask_tracing, cats, best)

            # Gato en descanso, pero siempre alerta
            for i, _ in enumerate(cats[self.CAT_FLAG][mask_seeking]):
                self.mode_seeking(mask_seeking, i, cats, best)

            # Clasificar aleatoriamente a los gatos segun el mr
            cats[self.CAT_FLAG] = self.random.permutation(cats[self.CAT_FLAG])

            it += 1

        if self.workers == 1:
            return best

        queue.put(best)

    def run(self):

        split = int(np.ceil(self.maxiter / self.workers))
        seq = SeedSequence()
        random = seq.spawn(self.workers)

        if self.debug:
            print()
            print('maxiter {} split {} workers {} threads {} chunksize {} cats {}'.format(
                    self.maxiter, split,
                    self.workers, self.n_threads, self.chunksize, self.n_cats))

        best = None

        if self.workers == 1:
            best = self.__worker__(0, default_rng(random[0]), self.maxiter, None)
        else:

            queue_best = Queue()

            best = [[]] * 4
            best[self.BEST_FUNC_TEST_VALUE] = np.inf

            for pid in range(self.workers):
                Process(target=self.__worker__, args=(
                                    pid,
                                    default_rng(random[pid]),
                                    split,
                                    queue_best)).start()

            for _ in range(self.workers):
                _best = queue_best.get()
                if self.debug:
                    print(_best)

                if _best[self.BEST_FUNC_TEST_VALUE] < best[self.BEST_FUNC_TEST_VALUE]:
                    best = _best

        # Se parchea la salida si se esta maximizando para optener el valor real: -f(x)
        if self.maximize:
            best[self.BEST_FUNC_TEST_VALUE] = -best[self.BEST_FUNC_TEST_VALUE]

        if self.debug:
            print()

        return best

    def __init__(self, func_test, debug=True,
            maximize=False, n_cats=100, maxiter=100,
            workers=1, threads=1, chunksize=1,
            *args, **kwargs):

        # Validaciones iniciales
        assert hasattr(func_test, '__call__'), 'Invalid function handle'

        _func_test = partial(func_test, *args, **kwargs)

        # Para maximizar la función la invierto: -f(x)
        self.func_test = _func_test if not maximize else lambda x: -_func_test(x)

        self.debug = debug
        self.n_cats = n_cats
        self.maxiter = maxiter
        self.maximize = maximize
        self.chunksize = chunksize
        self.workers = workers
        self.n_threads = threads

        self.threads = ThreadPoolExecutor(max_workers=threads)

        self.omega = kwargs.get('omega')
        self.mr = kwargs.get('mr')
        self.cdc = kwargs.get('cdc')
        self.spc = kwargs.get('spc')
        self.args = args
        self.kwargs = kwargs

        smp = kwargs.get('smp')

        # Numero de copias del gato a generar en seeking mode
        self.smp = smp if not self.spc else smp - 1


# Cat Swarm Optimization
class CSO(_CSO):

    def valid_args_limit(self):
        assert len(self.lb)==len(self.ub), 'Lower- and upper-bounds must be the same length'

        self.lb = np.array(self.lb)
        self.ub = np.array(self.ub)

        assert np.all(self.ub>self.lb), 'All upper-bound values must be greater than lower-bound values'

        self.dimension = len(self.lb)

    def init_positions(self, cats):
        # se crean los gatos con valores entre [0, 1]
        cats[self.CAT_POSITION] = self.random.random((self.n_cats, self.dimension))

        # inicializar la posicion de los gatos respetando los limites
        cats[self.CAT_POSITION] = self.lb + ( cats[self.CAT_POSITION] * ( self.ub - self.lb ) )

    def init_velocity(self, cats):
        # limites de velocidad
        velocityMax = np.abs(self.ub - self.lb)
        velocityMin = -velocityMax

        cats[self.CAT_VELOCITY] = velocityMin + self.random.random((self.n_cats, self.dimension)) * \
                                (velocityMax - velocityMin)

    def apply_mutation(self, cats):
        for cat in cats:

            # Actualizamos la mascara de mutación
            self.maskm = self.random.permutation(self.maskm)

            # Se elige si se suma o se resta el valor
            operation = self.random.choice([-1, 1], self.n_mutations)

            cat[self.maskm] = cat[self.maskm] + (operation * self.srd * cat[self.maskm])


    def __init__(self, func_test, lb, ub,
                    omega=0.5, mr=0.3, smp=2, srd=0.1, cdc=0.5, spc=False,
                    *args, **kwargs):

        self.lb = lb
        self.ub = ub

        self.srd = srd

        super().__init__(func_test,
                            omega=omega, mr=mr,
                            smp=smp, cdc=cdc, spc=spc, *args, **kwargs)

    # Gato buscando / cazando
    def mode_tracing(self, mask, cats, best):

        n = len(cats[self.CAT_POSITION][mask])

        ### 1.- Actualizar Velocidad
        r = self.random.uniform(size=(n, self.dimension))
        c = self.omega

        cats[self.CAT_VELOCITY][mask] = cats[self.CAT_VELOCITY][mask] + r * c * \
                                    (best[self.BEST_CAT_POSITION] - cats[self.CAT_POSITION][mask])

        ### 2.- Actualizamos la posición
        cats[self.CAT_POSITION][mask] = cats[self.CAT_POSITION][mask] + cats[self.CAT_VELOCITY][mask]

        ### 3.- Corregir las posiciones de acuerdo a los limites establecidos
        maskl = cats[self.CAT_POSITION][mask] < self.lb
        masku = cats[self.CAT_POSITION][mask] > self.ub

        cats[self.CAT_POSITION][mask] = ( cats[self.CAT_POSITION][mask] * (~np.logical_or(maskl, masku)) ) \
                                    + ( self.lb * maskl ) + ( self.ub * masku )


# Binary Cat Swarm Optimization
class BCSO(_CSO):

    def init_positions(self, cats):
        cats[self.CAT_POSITION] = self.random.randint(2, size=(self.n_cats, self.dimension))

    # se asigna una velocidad por dimension
    # la velicidad en binario se define como
    # v[k][d][0] probabilidad de que cambie a 0
    # v[k][d][1] probabilidad de que cambie a 1
    def init_velocity(self, cats):
        cats[self.CAT_VELOCITY] = self.random.uniform(size=(self.n_cats, self.dimension, 2))

    def apply_mutation(self, cats):
        for cat in cats:

            # Actualizamos la mascara de mutación
            self.maskm = self.random.permutation(self.maskm)

            update = self.random.random(self.n_mutations) < self.pmo

            x = cat[self.maskm]

            x[update] = 1

            cat[self.maskm] = x

    # Gato buscando / cazando
    def mode_tracing(self, mask, cats, best):

        c = self.omega

        dkd = [0] * 2

        for k, cat in enumerate(cats[self.CAT_POSITION]):
            for d, _ in enumerate(cat):

                r = self.random.random()

                # 1.-
                if best[self.BEST_CAT_POSITION][d] == 1:

                    dkd[0] = -r * c
                    dkd[1] =  r * c

                else:

                    dkd[0] =  r * c
                    dkd[1] = -r * c

                # 2.-
                cats[self.CAT_VELOCITY][k][d] = self.weight * cats[self.CAT_VELOCITY][k][d] + dkd

                # 3.-
                if cat[d] == 1:
                    cats[self.CAT_VELOCITY][k][d][1] = cats[self.CAT_VELOCITY][k][d][0]

                else:
                    cats[self.CAT_VELOCITY][k][d][1] = cats[self.CAT_VELOCITY][k][d][1]

                # 4.- Probabilidad de mutación
                m = 1 / (1 + (np.e ** -cats[self.CAT_VELOCITY][k][d][1]))

                if self.random.random() > m:
                    cat[d] = best[self.BEST_CAT_POSITION][d]


    def __init__(self, func_test, dimension=1,
                    omega=0.5, weight=1, mr=0.3, smp=2, pmo=0.7, cdc=0.5, spc=False,
                    *args, **kwargs):

        self.dimension = dimension
        self.pmo = pmo
        self.weight = weight

        super().__init__(func_test,
                            omega=omega, mr=mr,
                            smp=smp, cdc=cdc, spc=spc, *args, **kwargs)

