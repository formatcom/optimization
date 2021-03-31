### Proyecto final de optimización
Vinicio Valbuena

~~~
- Cat Swarm Optimization (Continuo)

    * Pruebas

	- Sphere function
	- Matyas function
	- Beale  function
	- Booth  function
	- Himmelblau's function

- Binary Cat Swarm Optimization (Discreto)

    * Pruebas

	- Knapsack problem
	- Set cover problem
~~~

### class CSO
~~~

Parametros
==========
- func_test : func
    La funcion a minimizar / maximizar.

- lb : array
    limites inferiores de las variable[s].

- ub : array
    limites superiores de las variable[s].

Opcionales
==========
- n_cats : int
    Numero de gatos.

- maxiter : int
    Numero maximo de iteraciones.

- mr : float
    Clasifica aleatoriamente a los gatos en búsqueda y rastreo.
    Intervalo [0, 1]. Ejemplo si el numero de gatos es 10 y el mr
    es 0.2, se eligiran 8 gatos aleatoriamente para ir al modo
    búsqueda ( seeking mode ) y los 2 restantes iran al modo de
    rastreo ( tracing mode ).

- smp : int
    Numero de posibles posiciones candidas aleatorias, ejemplo si
    se asigna a 5 cada gato generan 5 posiciones candidatas
    aleatorias para seleccionar la siguiente posicion.

- cdc : float
    Define cuantas dimenciones se van a modificar. Intervalo [0, 1].
    Ejemplo si el espacio de busqueda es de 5 dimensiones y cdc se
    asigna a 0.2, entonces para cada gato, cuatro dimensiones
    aleatorias de las cinco deben ser modificado y el otro permanece
    igual.

- srd : float
    Es la proporción de mutaciones para las dimensiones seleccionadas,
    es decir, define la cantidad de mutación y modificaciones para
    aquellas dimensiones que fueron seleccionadas por los cdc.
    Intervalo [0, 1].

- spc : bool
    Especifica si la posicion actual del gato se utiliza como posicion
    candidata.

- omega : float
    Factor para escalar la velocidad. Intervalo [0, 1].
~~~

### class BCSO
~~~

Parametros
==========
- func_test : func
    La funcion a minimizar / maximizar.

Opcionales
==========
- dimension : int
    Numero de dimensiones.

- n_cats : int
    Numero de gatos.

- maxiter : int
    Numero maximo de iteraciones.

- mr : float
    Clasifica aleatoriamente a los gatos en búsqueda y rastreo.
    Intervalo [0, 1]. Ejemplo si el numero de gatos es 10 y el mr
    es 0.2, se eligiran 8 gatos aleatoriamente para ir al modo
    búsqueda ( seeking mode ) y los 2 restantes iran al modo de
    rastreo ( tracing mode ).

- smp : int
    Numero de posibles posiciones candidas aleatorias, ejemplo si
    se asigna a 5 cada gato generan 5 posiciones candidatas
    aleatorias para seleccionar la siguiente posicion.

- cdc : float
    Define cuantas dimenciones se van a modificar. Intervalo [0, 1].
    Ejemplo si el espacio de busqueda es de 5 dimensiones y cdc se
    asigna a 0.2, entonces para cada gato, cuatro dimensiones
    aleatorias de las cinco deben ser modificado y el otro permanece
    igual.

- pmo : float
    Probabilidad de mutación. Intervalo [0, 1].

- spc : bool
    Especifica si la posicion actual del gato se utiliza como posicion
    candidata.

- omega : float
    Factor para escalar la velocidad. Intervalo [0, 1].

- weight : float
    Peso aplicado a la velocidad. Intervalo [0, 1].

~~~

### Ejecutar una prueba [Linux]
~~~
$ git clone https://github.com/formatcom/optimization
$ cd optimization
$
$ python -m venv env
$ source env/bin/activate
$
$ pip install -r requirements.txt
$
$ cd cso
$ time python test_himmelblaus.py
~~~

### Referencias
~~~
- https://www.researchgate.net/publication/221419703_Cat_Swarm_Optimization
- https://downloads.hindawi.com/journals/cin/2020/4854895.pdf
- https://www.researchgate.net/publication/258510186_Discrete_binary_cat_swarm_optimization_algorithm
- https://www.researchgate.net/publication/282307581_A_Binary_Cat_Swarm_Optimization_Algorithm_for_the_Non-Unicost_Set_Covering_Problem
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6393876/
- http://opac.pucv.cl/pucv_txt/txt-6500/UCD6603_01.pdf
- https://en.wikipedia.org/wiki/Test_functions_for_optimization
- https://es.wikipedia.org/wiki/Problema_del_conjunto_de_cobertura
- https://en.wikipedia.org/wiki/Set_cover_problem
- https://es.wikipedia.org/wiki/Problema_del_conjunto_de_cobertura
~~~
