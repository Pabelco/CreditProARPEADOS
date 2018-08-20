
import numpy as np
import pandas as pd

def funcion1(dataFrameJT): #funcion que va a analizar el dataframe de Joel Torres
    numeroFilas=dataFrameJT.shape[1]  # variable que me va a dar el numero de filas
    puntaje=0 #puntaje que al inicio obviamente es 0
    for i in range(0,numeroFilas+1): # recorro las filas n veces, comenzando por el indice 0 hasta el indice n
        contador=0 # un contador que comienza en 0
        primeraFila=dataFrameJT.ix[i:i+1] # comienza la lectura de la primera fila, luego segunda, luego tercera, etc etc...
        listaDeListaFilas=primeraFila.values #esta variable me lanza una lista con otra lista donde esta la n fila
        listaDeFila=listaDeListaFilas[0] # me devuelve la n fila en una sola lista
        identificacion=listaDeFila[0] # sacando parametros
        formaPago = listaDeFila[8]
        casado = listaDeFila[9]
        trabajaConDependencia = listaDeFila[10]
        negocioPropio = listaDeFila[11]
        ingresos = listaDeFila[12]
        edad = listaDeFila[13]
        sexo = listaDeFila[14]
        vehiculoPropio = listaDeFila[15]
        casaPropia = listaDeFila[16]
        if identificacion=="C" : # Comienzo a poner mis condiciones
            contador= contador+5
        if identificacion=="R":
            contador= contador +10
        if formaPago == "TARJETA":
            contador= contador+10
        if formaPago == "BANCO" :
            contador= contador + 10
        if formaPago == "COOPERATIVA":
            contador= contador+ 5
        if casado=="S":
            contador= contador +10
        if casado== "N":
            contador= contador+5
        if negocioPropio== "S":
            contador= contador +10
        if negocioPropio == "N":
            contador = contador+5
        if ingresos >=374 and ingresos<=500:
            contador = contador+5
        if ingresos>501 and ingresos<=700:
            contador= contador + 7
        if ingresos>701 and ingresos<=900:
            contador= contador +9
        if ingresos>=901:
            contador= contador+10
        if sexo=="M":
            contador= contador+5
        if sexo== "F":
            contador=contador+10
        if vehiculoPropio=="S":
            contador= contador+10
        if vehiculoPropio=="N":
            contador=contador+5
        if casaPropia=="S":
            contador= contador +10
        if casaPropia =="N":
            contador= contador+5
        if edad>=18 and edad<=25:
            contador=contador+4
        if edad>=26 and edad<=30:
            contador=contador+5
        if edad>=31 and edad<=35:
            contador=contador+7
        if edad>=36 and edad<=40:
            contador=contador+9
        if edad>=41:
            contador=contador+10
        if trabajaConDependencia== "S":
            contador=contador+10
        if trabajaConDependencia== "N":
            contador=contador+5
        if identificacion=="P":
            contador=contador+0

        puntaje= contador # hago que el puntaje se actualize al valor del puntaje que analizamos (del 0 al 100)
    dataFrameJT["PUNTAJE"]=puntaje # creo una nueva columna en el dataFrame con los puntajes respectiva
    return(dataFrameJT) # devuelvo el dataframe con una columna extra donde va a estar los puntajes







