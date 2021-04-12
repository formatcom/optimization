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

### CSO  | test_sphere.py | dimension 3

> Global minimum
>
> ![sphere](markdown/sphere.svg)


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

### CSO  | test_matyas.py | dimension 2

> Global minimum
>
> ![matyas](markdown/matyas.svg)

| n  | workers | threads | maxiter | cats | mr | smp | cdc | srd | spc | omega | time | result |
|--|--|--|--|--|--|--|--|--|--|--|--|--|
|  1  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 21.70s | [-0.00219794, -0.00220389]| 
|  2  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 20.33s | [-0.00072755, -0.00084696]| 
|  3  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 20.36s | [-0.01181477, -0.01387464]| 
|  4  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 20.64s | [-0.00191806, -0.00043771]|
|  5  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 22.11s | [0.00341738, 0.00284375]|
|  6  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 20.57s | [-0.00542174, -0.00507472]|
|  7  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 20.88s | [-0.00160638, -0.0009822 ]|
|  8  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 20.48s | [0.0019583 , 0.00202374]|
|  9  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 21.34s | [0.00495406, 0.0041392 ]|
|  10  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 21.05s | [0.00926299, 0.00963383]|

### CSO  | test_beale.py | dimension 2

> Global minimum
>
> ![beale](markdown/beale.svg)

| n  | workers | threads | maxiter | cats | mr | smp | cdc | srd | spc | omega | time | result |
|--|--|--|--|--|--|--|--|--|--|--|--|--|
|  1  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 25.25s |[2.48073003, 0.22802043]| 
|  2  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 25.17s |[2.48186641, 0.228083  ]| 
|  3  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 25.19s |[2.48136496, 0.22847218]|
|  4  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 24.18s |[2.48085428, 0.22798683]| 
|  5  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 26.30s |[[2.48304593, 0.22873487]|
|  6  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 25.38s |[2.48374288, 0.229162  ]| 
|  7  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 25.27s |[2.48357631, 0.22865276]|
|  8  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 24.97s |[2.48230566, 0.22850661]|
|  9  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 24.02s |[2.48122373, 0.22839413]| 
|  10  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 24.89s |[2.47971806, 0.22798356]| 

### CSO  | test_booth.py | dimension 2

> Global minimum
>
> ![booth](markdown/booth.svg)

| n  | workers | threads | maxiter | cats | mr | smp | cdc | srd | spc | omega | time | result |
|--|--|--|--|--|--|--|--|--|--|--|--|--|
|  1  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 24.30s |[[1.00040217, 3.00210714]| 
|  2  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 23.35s |[1.0012424 , 2.99974706]| 
|  3  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 23.65s |[0.9997878 , 2.99946154]| 
|  4  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 23.22s |[[1.00035112, 3.00089043]| 
|  5  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 23.44s |[1.00036068, 3.00119816]|
|  6  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 23.10s |[1.00245263, 2.99791777]|
|  7  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 23.06s |[0.99943678, 3.00039696]|
|  8  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 24.73s |[0.99995004, 2.99909456]|
|  9  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 23.26s |[0.9994608 , 3.00350465]|
|  10  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 23.35s |[1.0014833 , 2.99804731]|

### CSO  | test_himmelblaus.py | dimension 2

> Global minimum
>
> ![himmelblaus](markdown/himmelblaus_1.svg)
>
> ![himmelblaus](markdown/himmelblaus_2.svg)
>
> ![himmelblaus](markdown/himmelblaus_3.svg)
>
> ![himmelblaus](markdown/himmelblaus_4.svg)

| n  | workers | threads | maxiter | cats | mr | smp | cdc | srd | spc | omega | time | result |
|--|--|--|--|--|--|--|--|--|--|--|--|--|
|  1  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 21.03s |[3.00125341, 1.99843419]|
|  2  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 22.75s |[-3.78007255, -3.28286918]|
|  3  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 21.56s |[ 3.58508285, -1.84841575]| 
|  4  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 21.92s |[3.00015874, 1.99900615]|
|  5  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 23.32s |[-3.77939371, -3.28467525]|
|  6  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 22.13s |[ 3.58466987, -1.84967224]|
|  7  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 21.92s |[-3.77704171, -3.28315489]|
|  8  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 23.54s |[ 3.58476494, -1.84803254]|
|  9  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 23.09s |[2.9992986, 1.9991622]| 
|  10  | 1 | 1 | 200 | 500 | 0.5 | 10 | 1 | 0.1 | False | 0.5 | 22.33s |[-2.8052767 ,  3.12988145]| 

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
