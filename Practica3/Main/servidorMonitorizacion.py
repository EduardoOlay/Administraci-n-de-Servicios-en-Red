"""
Practica 3: Monitorizar el rendimiento de un agente usando SNMP
Olay Silis Jose Eduardo
4CM13
2020630347
"""
import time
import rrdtool
from getSNMP import consultaSNMP
from createRRD import crear_rrd
rrdpath='/home/eduardo/Documentos/Redes 3/Practica3/RRD/'
#Variables globales para guardar las consultas del CPU
carga_CPU1 =0;
carga_CPU2 =0;
carga_CPU3 =0;
carga_CPU4 =0;
carga_CPU5 =0;
carga_CPU6 =0;
carga_CPU7 =0;
carga_CPU8 =0;
carga_CPU9 =0;
carga_CPU10 =0;
carga_CPU11=0;
carga_CPU12 =0;

#Variables globales para guardar las consultas de la memoria RAM
mem_RAM_Libre=0;
mem_RAM_Total=0;

#Variables globales para guardar el tráfico de Red
OctetosEntrada=0;
OctetosSalida=0;
#from grafDetection import generar_graficas_rrd

def TrendUpdate(com,ip):
    while 1:
        #Se hacen las consultas de los cores
        carga_CPU1 = int(consultaSNMP(com,ip,'1.3.6.1.2.1.25.3.3.1.2.196608'))
        carga_CPU2 = int(consultaSNMP(com, ip, '1.3.6.1.2.1.25.3.3.1.2.196609'))
        carga_CPU3 = int(consultaSNMP(com,ip ,'1.3.6.1.2.1.25.3.3.1.2.196610'))
        carga_CPU4 = int(consultaSNMP(com,ip ,'1.3.6.1.2.1.25.3.3.1.2.196611'))
        carga_CPU5 = int(consultaSNMP(com, ip ,'1.3.6.1.2.1.25.3.3.1.2.196612'))
        carga_CPU6 = int(consultaSNMP(com, ip, '1.3.6.1.2.1.25.3.3.1.2.196613'))
        carga_CPU7 = int(consultaSNMP(com, ip, '1.3.6.1.2.1.25.3.3.1.2.196614'))
        carga_CPU8 = int(consultaSNMP(com,ip, '1.3.6.1.2.1.25.3.3.1.2.196615'))
        carga_CPU9 = int(consultaSNMP(com,ip, '1.3.6.1.2.1.25.3.3.1.2.196616'))
        carga_CPU10 = int(consultaSNMP(com, ip, '1.3.6.1.2.1.25.3.3.1.2.196617'))
        carga_CPU11 = int(consultaSNMP(com,ip, '1.3.6.1.2.1.25.3.3.1.2.196618'))
        carga_CPU12 = int(consultaSNMP(com, ip, '1.3.6.1.2.1.25.3.3.1.2.196619'))

        #Se hacen las consultas para obtener la memoria RAM libre y la total
        mem_RAM_Libre = int(consultaSNMP(com, ip, '1.3.6.1.4.1.2021.4.6.0'))
        mem_RAM_Total = int(consultaSNMP(com, ip, '1.3.6.1.4.1.2021.4.5.0'))

        #Se hace la consulta para tener los octetos de entrada y salida de red
        OctetosEntrada = int(consultaSNMP(com, ip, '1.3.6.1.2.1.2.2.1.10.1')) + int(consultaSNMP(com, ip, '1.3.6.1.2.1.2.2.1.10.2'))
        OctetosSalida = int(consultaSNMP(com, ip, '1.3.6.1.2.1.2.2.1.16.1')) + int(consultaSNMP(com, ip, '1.3.6.1.2.1.2.2.1.16.1'))

        #Se calcula el promedio para hacer una medida gneral de la carga del CPU
        promedioCargaCPU = (carga_CPU1 + carga_CPU2 + carga_CPU3 + carga_CPU4 + carga_CPU5 + carga_CPU6 + carga_CPU7 + carga_CPU8 + carga_CPU9 + carga_CPU10 + carga_CPU11 + carga_CPU12) / 12

        #Se hace la conversión a GB de la memoria ram para despues hacer una resta y obtener la memoria RAm en uso
        conversionRAM_Libre=mem_RAM_Libre/100000
        conversionRAM_Total=mem_RAM_Total/1000000
        mem_RAM_uso=conversionRAM_Total - conversionRAM_Libre
        conversion_OctIn=OctetosEntrada/10000000
        conversion_OctOut=OctetosSalida/1000000

        valor= "N:"+str(promedioCargaCPU)+":"+str(mem_RAM_uso)+":"+str(conversion_OctIn)+":"+str(conversion_OctOut)
        print(valor)
        rrdtool.update(rrdpath+'trend.rrd',valor)
        time.sleep(5)
    if ret:
        print(rrdtool.error())
        time.sleep(300)
    ultima_lectura=int(rrdtool.last(rrdpath+"trend.rrd"))



print("----Practica 3: Monitorizar el rendimiento de un agente usando SNMP----")
print("\n Eduardo Olay Silis - 4CM13 - 2020630347")
comunidad = input("\n\nEscribe el nombre de la comunidad del dispositivo: ")
ip = input("Escribe la direccion ip del dispositivo: ")

crear_rrd(comunidad)
print("\nAgente agregado exitosamemte comenzando monitorizacion...")
TrendUpdate(comunidad,ip)



