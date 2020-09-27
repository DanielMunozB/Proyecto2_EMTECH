# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 17:24:09 2020

@author: Daniel
"""
import csv 
df=[]
with open (r"C:\Users\Daniel\Documents\EMTECH\Proyecto 2\data-science-proyecto2-master\synergy_logistics_database.csv", "r") as archivo_csv:
    lector=csv.reader(archivo_csv)
    for linea in lector: 
        df.append(linea)

##print(df)
def direction (direccion):
###Generar rutas de exportacion

    contador=0
    rutas_contadas=[]
    
    conteo_rutas=[]
    
    
    for ruta in df: 
        if ruta[1]==direccion:
            ruta_actual = [ruta[2], ruta[3]]
            if ruta_actual not in rutas_contadas: 
                for movimiento in df:
                    if movimiento[1]==direccion:
                        if ruta_actual==[movimiento[2], movimiento[3]]:
                            contador+=1
                rutas_contadas.append(ruta_actual)
                
            
                conteo_rutas.append([ruta[2], ruta[3], contador])
                contador=0
                
    conteo_rutas.sort(reverse=True, key=lambda x:x[2])
    
    return(conteo_rutas)
    
#direction('Exports')


###Lo mismo para importaciones 

#direction('Imports')


####Similar pero para sacar la suma de valores por ruta

def valores (direccion):
###Generar rutas de exportacion

    contador=0
    rutas_contadas=[]
    
    conteo_rutas=[]
    
    
    for ruta in df: 
        if ruta[1]==direccion:
            ruta_actual = [ruta[2], ruta[3]]
            if ruta_actual not in rutas_contadas: 
                for movimiento in df:
                    if movimiento[1]==direccion:
                        if ruta_actual==[movimiento[2], movimiento[3]]:
                            contador+=int(movimiento[9])
                rutas_contadas.append(ruta_actual)
                
            
                conteo_rutas.append([ruta[2], ruta[3], contador])
                contador=0
                
    conteo_rutas.sort(reverse=True, key=lambda x:x[2])
    
    return(conteo_rutas)
resultado=valores('Exports')

#print(resultado)


valor_exportaciones=0


for n in resultado: 
    valor_exportaciones+=n[2]
    
#print(valor_exportaciones)=160163298000. Es el valor total de las exportaciones

##Ahora veamos el de las importaciones 

resultado=valores('Imports')

#print(resultado)


valor_importaciones=0


for n in resultado: 
    valor_importaciones+=n[2]

#print(valor_importaciones)=55528000000. Es el valor total de las importaciones

##El valor total de las operaciones es print(55528000000+160163298000)=215691298000





#####Rutas de exportacion. Valor por orgien

def valor_exp (direccion):
###Generar rutas de exportacion

    contador=0
    rutas_contadas=[]
    
    valor_rutas=[]
    
    if direccion=='Exports':
        for ruta in df: 
            if ruta[1]==direccion:
                ruta_actual = ruta[2]
                if ruta_actual not in rutas_contadas: 
                    for movimiento in df:
                        if movimiento[1]==direccion:
                            if ruta_actual==movimiento[2]:
                                contador+=int(movimiento[9])
                    rutas_contadas.append(ruta_actual)
                    
                
                    valor_rutas.append([ruta[2], contador])
                    contador=0
                    
        valor_rutas.sort(reverse=True, key=lambda x:x[1])
        
        return(valor_rutas)
    
    
    
    
    
    
pais_exp=valor_exp('Exports')

#print(pais_exp)

def valor_imp (direccion):
###Generar rutas de exportacion

    contador=0
    rutas_contadas2=[]
    
    valor_rutas2=[]
    
    if direccion=='Imports':
        for ruta in df: 
            if ruta[1]==direccion:
                ruta_actual2 = ruta[3]
                if ruta_actual2 not in rutas_contadas2: 
                    for movimiento in df:
                        if movimiento[1]==direccion:
                            if ruta_actual2==movimiento[3]:
                                contador+=int(movimiento[9])
                    rutas_contadas2.append(ruta_actual2)
                    
                
                    valor_rutas2.append([ruta[3], contador])
                    contador=0
                    
        valor_rutas2.sort(reverse=True, key=lambda x:x[1])
        
        return(valor_rutas2)
    
    
    
    
    
    
pais_imp=valor_imp('Imports')

#print(pais_imp)

##Añadiendo el porcentaje de operaciones totales. 215691298000
pais_imp_por=[]
for n in range (0,10):
    pais_imp_por.append([pais_imp[n][0], pais_imp[n][1], pais_imp[n][1]/215691298000 ])
    
    
#print(pais_imp_por)


#print(len(pais_exp))
pais_exp_por=[]
for n in range(0,19):
    pais_exp_por.append([pais_exp[n][0], pais_exp[n][1], pais_exp[n][1]/215691298000 ])
    
#print(pais_exp_por)



#sacar el 80% de las operaciones 
porcentajes=pais_exp_por
for n in range(0,10):
    porcentajes.append(pais_imp_por[n])
    

porcentajes.sort(reverse=True, key=lambda x:x[2])

#print(len(porcentajes))

#Sumar porcentajes y que pare cuando llegueal 80%
lista_final=[]
suma_porcentaje=0
for n in range (0,28):
    if suma_porcentaje<80:
        suma_porcentaje+=porcentajes[n][2]*100
        lista_final.append([porcentajes[n][0], porcentajes[n][1], porcentajes[n][2], suma_porcentaje])

#print(lista_final) 
###Tailandia es importaciones, Mexico, Emiratos y segundo Japón
###China, Francia, USA, Corea del Sur, Tailandia, Rusia, Japón, Alemania, Canadá, México, Emiratos
##Japón, Italia

import pandas as pd 

df1=pd.read_csv(r"C:\Users\Daniel\Documents\EMTECH\Proyecto 2\data-science-proyecto2-master\synergy_logistics_database.csv")

#print(df1.groupby(['transport_mode','origin']).sum().sort_values('total_value', ascending=False).head(15))
###Sea, Rail and air son las 3 con mayor valor. Pueden reducir road




#direction('Exports')

### Las 10 rutas de exportacion con más demanda son: 1 Corea Sur-Vietnam, 2 Holanda-Bélgica
### 3 USA-Holanda, 4 China-México, 5 Japón-Brasil, 6 Alemania-Francia, 7 Corea del Sur-Japón
### 8 Australia-Singapur, 9 Canadá-México, 10 China-España



##Valor de rutas de exportaciones
#resultado=valores('Exports')

#print(resultado)
#1 China-México, 2 Canadá-México, 3Corea del Sur-Vietnam, 4 Francia-Bélgica, 5 Francia-UK
#6 China-Corea del Sur, 7 USA-México, 8 Corea del Sur-Japón, 9 Alemania-Italia, 10 China Alemania

#Si usas las 10 con más demanda pierdes la 4, 5,6, 7, 9, 10 con más valor 





#direction('Imports')

###Las 10 rutas de importacion con más demanda son 1 Singapore-Thailandia, 2 Alemania-China
##3 China-Japon, ###4 Japón-México, 5 China-Thailandia, 6 Malasia-Thailandia, 7 España-Alemania
##8 Méxco-USA, 9 China-Emiratos Arabes Unidos, 10 Brasil-China

##Valor de rutas de importaciones
#resultado=valores('Imports')

#print(resultado)
#1 Singapur-Tailandia, 2 Japón-México, 3 China-Tailandia, 4 Malasia-Tailandia, 5 China-Emiratos
#6 China Japón, 7 México USA, 8 Japón-Emiratos, 9 España-ALemania, 10 Alemania-México

##Si usas las 10 con más demanda pierdes la 10 y la 8 en valor

elegir=input("Elige una opción (Exportaciones/Importaciones/Medios/Opcion 3): ")

if elegir=='Exportaciones':
    print("Las 10 rutas más demandadas de exportaciones son: ")
    print("[Origen, Destino, Repeticiones")
    resultado=direction ('Exports')
    for n in range(0,9): 
        print(resultado[n])

elif elegir=='Importaciones':
    print("Las 10 rutas más demandadas de importaciones son: ")
    print("[Origen, Destino, Repeticiones]")
    resultado=direction ('Imports')
    for n in range(0,9): 
        print(resultado[n])
elif elegir=='Medios':
    print(df1.groupby(['transport_mode']).sum().sort_values('total_value', ascending=False).head(15))

elif elegir=='Opcion 3':
    print("Los países que generan el 80% de las operaciones son: ")
    print(["País, Porcentaje, Porcentaje Acumulado"])
    formato=[]
    for line in lista_final:
        formato.append([line[0], line[2], line[3]])
    for repe in formato:
        print(repe)
else:
    print("Error en entrada: Intente de nuevo por favor")

    

