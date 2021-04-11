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
- maximize : bool
    Por defecto es False, se utiliza para indicar si se busca max o min
    la func_test.

- cats : int
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
- maximize : bool
    Por defecto es False, se utiliza para indicar si se busca max o min
    la func_test.

- dimension : int
    Numero de dimensiones.

- cats : int
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
$ python3 -m venv env
$ source env/bin/activate
$
$ pip install -r requirements.txt
$
$ cd cso
$ time python test_himmelblaus.py
~~~

### Resultados
~~~
Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz

Cores:      2
Threads:    2
GFLOPS:  86.4
~~~

#### CSO  | test_sphere.py | dimension 3
| n  | workers | threads | maxiter | cats | mr | smp | cdc | srd | spc | omega | time | result |
|--|--|--|--|--|--|--|--|--|--|--|--|--|
|  1  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 21.50s | [-0.01727896,  0.01340078,  0.01545751]| 
|  2  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 20.74s | [-0.00655391, -0.01099599, -0.00916707]| 
|  3  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 21.81s | [-0.01008625,  0.0043805 ,  0.00350937]| 
|  4  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 21.23s | [0.00489058, 0.01195485, 0.01197201]| 
~~~
~~~
| n  | workers | threads | maxiter | cats | mr | smp | cdc | srd | spc | omega | time | result |
|--|--|--|--|--|--|--|--|--|--|--|--|--|
|  1  | 3 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 34.16s |[-0.0037651545586679493, -0.0980244535660562, -0.039365020574868306] | 
|  2  | 3 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 32.52s |[-0.10029394465162955, -0.1069079281528893, 0.03301591599169547] | 
|  3  | 3 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 33.86s |[-0.034710058467875005, -0.02787973747516491, -0.030165981242425314]| 
|  4  | 3 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 33.23s |[-0.07637763697216123, -0.033123010180368485, -0.2403497711396711]| 
~~~
~~~
| n  | workers | threads | maxiter | cats | mr | smp | cdc | srd | spc | omega | time | result |
|--|--|--|--|--|--|--|--|--|--|--|--|--|
|  1  | 1 | 2 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 36.38s |[ 0.01158723, -0.00072514,  0.01012487]| 
|  2  | 1 | 2 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 36.17s |[-0.00458861,  0.00882006, -0.00258965]| 
|  3 | 1 | 2 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 35.77s |[-0.00374484, -0.0026737 , -0.01068693]| 
|  4 | 1 | 2 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 35.38s |[0.00505702, 0.00904414, 0.00739504]| 
~~~
~~~
| n  | workers | threads | maxiter | cats | mr | smp | cdc | srd | spc | omega | time | result |
|--|--|--|--|--|--|--|--|--|--|--|--|--|
|  1  | 3 | 2 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 51.98s |[-0.08379533035074181, -0.06389297258342667, -0.06388296120706652]| 
|  2  | 3 | 2 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 53.38s |[0.07298986318120004, 0.07497126941811505, 0.04351470646237898]| 
|  3  | 3 | 2 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 52.31s |[-0.07032199530452798, 0.17858643752770753, 0.09637068232979784]| 
|  4  | 3 | 2 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 52.40s |[0.05096983778438524, -0.06686564511500748, -0.041256651459480986]| 

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
~~~
