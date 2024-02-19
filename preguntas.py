"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    import csv
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        suma=0
        for row in reader:
            l = row[0].split('\t')
            suma = suma + int(l[1])
    return suma


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    import csv
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        resp=[]
        sumaA=0
        sumaB=0
        sumaC=0
        sumaD=0
        sumaE=0
        for row in reader:
            l = row[0].split('\t')
            if l[0] == 'A':
                sumaA+=1
            elif l[0] == 'B':
                sumaB+=1
            elif l[0] == 'C':
                sumaC+=1
            elif l[0] == 'D':
                sumaD+=1
            elif l[0] == 'E':
                sumaE+=1
        resp.append(("A", sumaA))
        resp.append(("B", sumaB))
        resp.append(("C", sumaC))
        resp.append(("D", sumaD))
        resp.append(("E", sumaE))
    return resp


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    import csv
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        resp=[]
        sumaA=0
        sumaB=0
        sumaC=0
        sumaD=0
        sumaE=0
        for row in reader:
            l = row[0].split('\t')
            if l[0] == 'A':
                sumaA+=int(l[1])
            elif l[0] == 'B':
                sumaB+=int(l[1])
            elif l[0] == 'C':
                sumaC+=int(l[1])
            elif l[0] == 'D':
                sumaD+=int(l[1])
            elif l[0] == 'E':
                sumaE+=int(l[1])
        resp.append(("A", sumaA))
        resp.append(("B", sumaB))
        resp.append(("C", sumaC))
        resp.append(("D", sumaD))
        resp.append(("E", sumaE))
    return resp
#print(pregunta_03())

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    import csv
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        meses=[]
        resp=[]
        for row in reader:
            l = row[0].split('\t')
            l2 = l[2].split('-')
            meses.append(l2[1])
        ocurrencias=sorted(list(set(meses)))
        for i in ocurrencias:
            N = [x for x in meses if x==i]
            resp.append((i, len(N)))
    return resp
#print(pregunta_04())

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    import csv
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        suma=0
        lista=[]
        letras=[]
        resp=[]
        for row in reader:
            l = row[0].split('\t')
            if l[0] not in letras:
                letras.append(l[0])
            lista.append((l[0],l[1]))
        letras=sorted(letras)
        for i in letras:
            N = [int(x[1]) for x in lista if x[0]==i]
            resp.append((i, max(N), min(N)))
        #resp.append((i, len(N)))
    return resp
#print(pregunta_05())

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    
    import re
    x = open("data.csv", "r").readlines()
    chars=[]
    letras=[]
    for row in x:
        row = row.replace('\n', '')
        l = row.split('\t')
        #l[4] = l[4].replace(':', ',')
        entrada = l[4].split(',')
        pattern = "[a-j]{3}"
        prog = re.compile(pattern)
        for i in entrada:
            aux = i.split(':')
            chars.append(aux)
            if prog.match(aux[0]) and (aux[0] not in letras):
                    #print(i)
                letras.append(aux[0])
    #for x in chars:
    resp=[]
    letras=sorted(letras)
    for i in letras:
        N = [int(x[1]) for x in chars if x[0]==i]
        resp.append((i, min(N), max(N)))

    return resp
#print(pregunta_06())

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    x = open("data.csv", "r").readlines()
    l = [int(z[2]) for z in x]     
    letras = list(set(l))
    l2 = [(z[0], int(z[2])) for z in x]
    l2 = [list(i) for i in l2]
    resp = []
    letras = sorted(letras)
    for i in letras: 
        N = [x[0] for x in l2 if x[1]==i]
        resp.append((i, N))
    return resp
#print(pregunta_07())

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    x = open("data.csv", "r").readlines()
    l = [int(z[2]) for z in x]     
    letras = list(set(l))
    l2 = [(z[0], int(z[2])) for z in x]
    l2 = [list(i) for i in l2]
    resp = []
    letras = sorted(letras)
    for i in letras:
        N = [x[0] for x in l2 if x[1]==i]
        N = list(set(N))
        resp.append((i, sorted(N)))
    return resp
#print(pregunta_08())

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    import re
    x = open("data.csv", "r").readlines()
    chars=[]
    letras=[]
    for row in x:
        row = row.replace('\n', '')
        l = row.split('\t')
        #l[4] = l[4].replace(':', ',')
        entrada = l[4].split(',')
        pattern = "[a-j]{3}"
        prog = re.compile(pattern)
        for i in entrada:
            aux = i.split(':')
            chars.append(aux)
            if prog.match(aux[0]) and (aux[0] not in letras):
                    #print(i)
                letras.append(aux[0])
    #for x in chars:
    resp=[]
    aux1=[]
    aux2=[]
    letras=sorted(letras)
    for i in letras:
        N = [int(x[1]) for x in chars if x[0]==i]
        #resp.append((i, len(N)))
        aux1.append(i) 
        aux2.append(len(N))   
    resp = dict(zip(aux1, aux2))

    return resp
#print(pregunta_09())

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    L = open("data.csv", "r").readlines()
    M = [i.replace("\t", " ") for i in L]
    M = [j.replace("\n", "") for j in L]    

    resp = [(i[0], i.count(',') - i.count(':') + 2, i.count(':')) for i in M]

    return  resp
#print(pregunta_10())

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    
    x = open("data.csv", "r").readlines()
    x = [z.replace("\t", " ") for z in x]
    x = [z.replace("\n", "") for z in x] 
    x=[z.split() for z in x]  
    x=[(int(z[1]), z[3].split(',')) for z in x]
    print(x)
    lista=[]"""
    ############
    import re
    x = open("data.csv", "r").readlines()
    chars=[]
    
    for row in x:
        row = row.replace('\n', '')
        l = row.split('\t')
        numero = int(l[1])
        entrada = l[3].split(',')
        chars.append((numero,entrada))
    letras = []
    l2 = []
    for i in chars:
        l2 += i[1]
    letras = list(set(l2))
    letras = sorted(letras)
    suma = []

    for j in letras:
        N = [n[0] for n in chars if j in n[1] ]
        suma.append(sum(N))
    resp = dict(zip(letras, suma))
    
    return resp
#print(pregunta_11())

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    import re
    x = open("data.csv", "r").readlines()
    chars=[]
    
    for row in x:
        row = row.replace('\n', '')
        l = row.split('\t')
        numero = l[0]
        entrada = l[4].split(',')
        chars.append((numero,entrada))
    a=[]
    b=[]
    for i in chars:
        a.append(i[0])
    for i in chars:
        b.append(i[1])
    l=[]
    for j in b: 
        N = [(re.findall('\d{1,2}', x)) for x in j] 
        l.append(N)

    l2=[]
    for k in l:
        l2.append(sum([int(d[0]) for d in k]))

    resp = list(set(a))
    resp = sorted(resp)
    d = [[l2[i], a[i]] for i in range(len(a))]

    X=[]
    Y=[]
    for n in resp: 
        g = [x[0] for x in d if x[1] == n]
        X.append(n)
        Y.append(sum(g))
    dicc= dict(zip(X, Y))

    return dicc

#print(pregunta_12())
