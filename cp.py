import numpy as np
import pandas as pd

def funcion1(matrizJT):

    contador=0
    for linea in matrizJT:
        linea[0]= "identificacion"
        linea[8]="forma de pago"
        linea[9] = "casado"
        linea[11] = "negocio propio"
        linea[10] = "trabaja con dependencia"
        linea[12] = "ingresos"
        linea[13] = "edad"
        linea[14] = "sexo"
        linea[15] = "vehiculo propio"
        linea[16] = "casa propio"

        if "identificacion"== "cedula":
            contador= contador+5
        elif "identificacion"== "RUC":
            contador= contador +10
        elif "forma de pago" == "tarjeta":
            contador= contador+10
        elif "forma de pago" == "banco" and "forma de pago" == "ahorros":
            contador= contador + 5
        elif "forma de pago" == "banco" and "forma de pago" == "corriente":
            contador= contador+ 10
        elif "forma de pago" == "cooperativa":
            contador=contador+5
        elif "casado"== True:
            contador= contador +10
        elif "casado"== False:
            contador= contador+5
        elif "negocio propio"== True:
            contador= contador +10
        elif "negocio propio"== False:
            contador = contador+5
        elif "ingresos">=374 and "ingresos"<=500:
            contador = contador+5
        elif "ingresos">501 and "ingresos"<=700:
            contador= contador + 7
        elif "ingresos">701 and "ingresos"<=900:
            contador= contador +9
        elif "ingresos">=901
            contador= contador+10
        elif "sexo"=="masculino":
            contador= contador+5
        elif "sexo"== "femenino":
            contador=contador+10
        elif "vehiculo"==True:
            contador= contador+10
        elif "vehiculo"==False:
            contador=contador+5
        elif "casa propia"==True:
            contador= contador +10
        elif "casa propia"== False:
            contador= contador+5
        elif "edad">=18 and "edad"<=25:
            contador=contador+4
        elif "edad">=26 and "edad"<=30:
            contador=contador+5
        elif "edad">=31 and "edad"<=35:
            contador=contador+7
        elif "edad">=36 and "edad"<=40:
            contador=contador+9
        elif "edad">=41:
            contador=contador+10
        elif "trabaja con dependencia"== True:
            contador=contador+10
        elif "trabaja con dependencia"== True:
            contador=contador+5

        puntajeTotal= contador
        matrizJT[17]= puntajeTotal





