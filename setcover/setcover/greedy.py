### Greedy Algorithm
### Creado por Vinicio Valbuena
### REF: https://doc.lagout.org/science/0_Computer%20Science/2_Algorithms/Approximation%20Algorithms%20%5BVazirani%202010-12-01%5D.pdf#page=31

import math

class Greedy:

    INDEX = 0
    SET = 1

    def __init__(self, n_group, n_elem, cost, dataset, debug=False):

        self.n_group = n_group
        self.n_elem = n_elem
        self.cost = cost
        self.debug = debug

        self.dataset = []

        for i, g in enumerate(dataset):
            self.dataset.append((i, g))

        if self.debug:

            print("#####################################")
            print("number sets     {:05d}".format(self.n_group))
            print("number elements {:05d}".format(self.n_elem))
            print()
            print("#####################################")
            print("cost | set ")
            print()

            for i, c in enumerate(self.cost):
                print("{cost:04d} | {set}".format(**{
                    'cost': c,
                    'set': self.dataset[i],
                }))

            print()
            print("#####################################")
            print()

    def run(self):

        # Lista de elementos sin cubrir
        uncovered_elements = set()

        for s in self.dataset:
            uncovered_elements = uncovered_elements.union(s[self.SET])

        # Lista de conjuntos sin cubrir
        uncovered_groups = self.dataset.copy()

        # Lista de conjuntos cubiertos
        covered_groups = []
        covered_elements = set()

        # Costo total
        cost = 0

        # Trabajmos con una copia de los costos
        _cost = self.cost.copy()

        while uncovered_elements:

            # selecciona el mejor conjunto
            _select_group = -1
            _min_cost = math.inf

            if self.debug:
                print()

            for i, group in enumerate(uncovered_groups):

                '''
                rentabilidad = c / ( g - s )

                donde:
                    c = costo del conjunto
                    g = elementos del conjunto
                    s = elementos cubiertos actualmente

                    ( g - s ) = numero de elementos no cubiertos en g
                '''

                # Rentabilidad inf por defecto
                r = math.inf

                # (g - s)
                n_elements = len(set(group[self.SET]) - covered_elements)

                if self.debug:
                    print("[{i:04d}] | {cost:04d} | {set}".format(**{
                        'i': i,
                        'cost': _cost[i],
                        'set': group,
                    }))

                # Verificamos que seleccionamos algun elemento
                if n_elements:

                    c = _cost[i]

                    r = c / n_elements

                # Actualizamos el mejor costo
                if r < _min_cost:

                    _min_cost = r
                    _index_select = i

            if self.debug:
                print(" " * 100,  end = '')
                print("                                select -> [{:04d}]".format(_index_select))

            # Acumulamos el costo total
            cost = cost + _cost[_index_select]

            # Agregamos el conjunto a cubrir
            covered_groups.append(uncovered_groups[_index_select])

            # Agregamos los elementos a cubrir
            covered_elements = covered_elements.union(uncovered_groups[_index_select][self.SET])

            # Eliminamos los elementos cubiertos
            uncovered_elements = uncovered_elements - set(uncovered_groups[_index_select][self.SET])

            # Eliminamos el conjunto cubierto
            del uncovered_groups[_index_select]
            del _cost[_index_select]

        return covered_groups, cost




