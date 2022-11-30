import sys
import rrdtool
import time
import datetime
from Notify import send_alert_attached
from getSNMP import consultaSNMP
import time

rrdpath = '/home/eduardo/Documentos/Redes 3/Practica3/RRD/'
imgpath = '/home/eduardo/Documentos/Redes 3/Practica3/IMG/'


def generarGraficaCPU(ultima_lectura):
    nombre_agente = consultaSNMP('comunidadSNMP', 'localhost', '1.3.6.1.2.1.1.5.0')
    tiempo_final = int(ultima_lectura)
    tiempo_inicial = tiempo_final - 1800
    ret = rrdtool.graphv(imgpath + "deteccionCPU.png",
                         "--start", str(tiempo_inicial),
                         "--end", str(tiempo_final),
                         "--vertical-label=Carga de CPU %",
                         '--lower-limit', '0',
                         '--upper-limit', '100',
                         "--title= Monitorización del uso del CPU \nde {}".format(
                             nombre_agente),
                         "DEF:cargaCPU=" + rrdpath + "trend.rrd:carga_CPU:AVERAGE",
                         "VDEF:cargaMAX=cargaCPU,MAXIMUM",
                         "VDEF:cargaMIN=cargaCPU,MINIMUM",
                         "VDEF:cargaSTDEV=cargaCPU,STDEV",
                         "VDEF:cargaLAST=cargaCPU,LAST",
                         "CDEF:umbralOperativo=cargaCPU,20,LT,0,cargaCPU,IF",
                         "CDEF:umbralSobrecarga=cargaCPU,60,LT,0,cargaCPU,IF",
                         "CDEF:umbralCargaExcesiva=cargaCPU,85,LT,0,cargaCPU,IF",
                         "AREA:cargaCPU#4E0482:Carga del CPU",
                         "AREA:umbralOperativo#000:Carga CPU normal 20% - 60%",
                         "AREA:umbralSobrecarga#f4ee2a:Carga CPU sobrecarga 60% -85%",
                         "AREA:umbralCargaExcesiva#ca230f:Carga CPU  excesiva +85%",
                         "HRULE:20#000:Umbral 20%",
                         "HRULE:60#EF6C00:Umbral 60%",
                         "HRULE:85#D84315:Umbral 85%",
                         "PRINT:cargaLAST:%6.2lf",
                         "GPRINT:cargaMIN:%6.2lf %SMIN",
                         "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                         "GPRINT:cargaLAST:%6.2lf %SLAST")


def generarGraficaRAM(ultima_lectura):
    nombre_agente = consultaSNMP('comunidadSNMP', 'localhost', '1.3.6.1.2.1.1.5.0')
    tiempo_final = int(ultima_lectura)
    tiempo_inicial = tiempo_final - 1800
    ret = rrdtool.graphv(imgpath + "deteccionRAM.png",
                         "--start", str(tiempo_inicial),
                         "--end", str(tiempo_final),
                         "--vertical-label=RAM (GB)",
                         '--lower-limit', '0',
                         '--upper-limit', '10',
                         "--title= Monitorización de uso de la RAM {}".format(
                             nombre_agente),
                         "DEF:cargaRAM=" + rrdpath + "trend.rrd:uso_RAM:AVERAGE",
                         "VDEF:cargaMAX=cargaRAM,MAXIMUM",
                         "VDEF:cargaMIN=cargaRAM,MINIMUM",
                         "VDEF:cargaSTDEV=cargaRAM,STDEV",
                         "VDEF:cargaLAST=cargaRAM,LAST",
                         "CDEF:umbralOperativo=cargaRAM,2.5,LT,0,cargaRAM,IF",
                         "CDEF:umbralSobrecarga=cargaRAM,5,LT,0,cargaRAM,IF",
                         "CDEF:umbralCargaExcesiva=cargaRAM,6.5,LT,0,cargaRAM,IF",
                         "AREA:cargaRAM#0fca80:Carga de RAM",
                         "AREA:umbralOperativo#1cb43c:Carga RAM normal (40% - 60%)",
                         "AREA:umbralSobrecarga#f4ee2a:Carga Ram sobrecarga (60% -85%)",
                         "AREA:umbralCargaExcesiva#ca230f:Carga CPU  excesiva (+85%)",
                         "HRULE:2.5#FF8F00:Umbral 40%",
                         "HRULE:5#EF6C00:Umbral 60%",
                         "HRULE:6.5#D84315:Umbral 85%",
                         "PRINT:cargaLAST:%6.2lf",
                         "GPRINT:cargaMIN:%6.2lf %SMIN",
                         "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                         "GPRINT:cargaLAST:%6.2lf %SLAST")


def generarGraficaRED(ultima_lectura):
    nombre_agente = consultaSNMP('comunidadSNMP', 'localhost', '1.3.6.1.2.1.1.5.0')
    tiempo_final = int(ultima_lectura)
    tiempo_inicial = tiempo_final - 1800
    ret = rrdtool.graphv(imgpath + "deteccionRED.png",
                         "--start", str(tiempo_inicial),
                         "--end", str(tiempo_final),
                         "--vertical-label=Octetos",
                         '--lower-limit', '0',
                         '--upper-limit', '100',
                         "--title= Monitorización de carga octetos de entrada y salida en \n Red {}".format(
                             nombre_agente),
                         "DEF:cargaRED=" + rrdpath + "trend.rrd:trafico_Red_Entrada:AVERAGE",
                         "DEF:cargaRED_2=" + rrdpath + "trend.rrd:trafico_Red_Salida:AVERAGE",
                         "VDEF:cargaMAX=cargaRED,MAXIMUM",
                         "VDEF:cargaMIN=cargaRED,MINIMUM",
                         "VDEF:cargaSTDEV=cargaRED,STDEV",
                         "VDEF:cargaLAST=cargaRED,LAST",
                         "VDEF:cargaMAX_2=cargaRED_2,MAXIMUM",
                         "VDEF:cargaMIN_2=cargaRED_2,MINIMUM",
                         "VDEF:cargaSTDEV_2=cargaRED_2,STDEV",
                         "VDEF:cargaLAST_2=cargaRED_2,LAST",
                         "CDEF:umbralOperativoIn=cargaRED,20,LT,0,cargaRED,IF",
                         "CDEF:umbralSobrecargaIn=cargaRED,50,LT,0,cargaRED,IF",
                         "CDEF:umbralCargaExcesivaIn=cargaRED,90,LT,0,cargaRED,IF",
                         "CDEF:umbralOperativoOut=cargaRED_2,20,LT,0,cargaRED_2,IF",
                         "CDEF:umbralSobrecargaOut=cargaRED_2,50,LT,0,cargaRED_2,IF",
                         "CDEF:umbralCargaExcesivaOut=cargaRED_2,90,LT,0,cargaRED_2,IF",
                         "LINE:cargaRED#ca0fca:Octetos de entrada",
                         "LINE:umbralOperativoIn#1cb43c:Octetos de entrada (20 - 50)",
                         "LINE:umbralSobrecargaIn#f4ee2a:Octetos de entrada (50 -90)",
                         "LINE:umbralCargaExcesivaIn#ca230f:Octetos de entrada (+90)",
                         "LINE:cargaRED_2#ca5b0f:Octetos de salida",
                         "LINE:umbralOperativoOut#09901c:Octetos de salida (20 - 50)",
                         "LINE:umbralSobrecargaOut#cccc15:Octetos de salida (50 - 90)",
                         "LINE:umbralCargaExcesivaOut#b41515:Octetos de salida (+90)",
                         "HRULE:20#FF8F00:Umbral 20%",
                         "HRULE:50#EF6C00:Umbral 50%",
                         "HRULE:90#D84315:Umbral 90%",
                         "PRINT:cargaLAST:%6.2lf",
                         "GPRINT:cargaMIN:%6.2lf %SMIN",
                         "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                         "GPRINT:cargaLAST:%6.2lf %SLAST")



while (1):
    ultima_actualizacion = rrdtool.lastupdate(rrdpath + "trend.rrd")
    timestamp = ultima_actualizacion['date'].timestamp()
    datoCPU = ultima_actualizacion['ds']["carga_CPU"]
    datoRAM = ultima_actualizacion['ds']["uso_RAM"]
    datoOctetosEntrada = ultima_actualizacion['ds']["trafico_Red_Entrada"]
    datoOctetosSalida = ultima_actualizacion['ds']["trafico_Red_Salida"]

    print('N:' + str(datoCPU) + ':' + str(datoRAM) + ':' + str(datoOctetosEntrada) + ':' + str(datoOctetosSalida))

    elementos_sobrecargados = ['CPU', 'RAM', 'RED']
    if 20 < datoCPU < 60 or 2.5 < datoRAM < 5 or 20 < datoOctetosSalida < 50 or 20 < datoOctetosEntrada < 50:
        cadena = "Sobrepasa el umbral operativo"
        generarGraficaCPU(int(timestamp))
        generarGraficaRAM(int(timestamp))
        generarGraficaRED(int(timestamp))
        send_alert_attached(cadena, elementos_sobrecargados)
        print(cadena)

    if 60 < datoCPU < 85 or 5 < datoRAM < 6.5 or 50 < datoOctetosSalida < 90 or 50 < datoOctetosEntrada < 90:
        cadena = "Sobrepasa umbral de sobrecarga "
        generarGraficaCPU(int(timestamp))
        generarGraficaRAM(int(timestamp))
        generarGraficaRED(int(timestamp))
        send_alert_attached(cadena, elementos_sobrecargados)
        print(cadena)

    if datoCPU > 65 or datoRAM > 6.5 or datoOctetosSalida > 90 or datoOctetosEntrada > 90:
        cadena = "Sobrepasa umbral excesivo, se recomienda accion inmediata"
        generarGraficaCPU(int(timestamp))
        generarGraficaRAM(int(timestamp))
        generarGraficaRED(int(timestamp))
        send_alert_attached(cadena, elementos_sobrecargados)
        print(cadena)


    time.sleep(20)