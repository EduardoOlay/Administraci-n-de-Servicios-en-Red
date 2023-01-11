import os
import shlex
import subprocess
import sys
import getpass
import telnetlib
from ftplib import FTP
from getSNMP import consultaSNMP

user="rcp"
password="rcp"
resp="Y"

def imprimirInfo():
    name= str(consultaSNMP("comunidadSNMP","localhost",'1.3.6.1.2.1.1.1.0'))
    if name == 'Hardware:':
        name = "Windows"
        _OID = '1.3.6.1.2.1.2.2.1.8.3'  # OID para la interfaz
    else:  # Cuando name == Linux
        _OID = '1.3.6.1.2.1.2.2.1.8.3'  # En caso de Linux como es nuestra compu es wlan0

    OperStatus=consultaSNMP("comunidadSNMP","localhost",_OID)

    if OperStatus == '1':
        status = 'up'
    elif OperStatus == '2':
        status = 'down'
    elif OperStatus == '3':
        status = 'testing'


    num_puertos= consultaSNMP("comunidadSNMP","localhost",'1.3.6.1.2.1.2.1.0')
    print("<Dispositivo: "+name+">   <Estatus del monitoreo: "+status+">    <No. puertos disponibles: "+num_puertos+">")


while resp != 'N':
    #Se imprime el menú

    print("******************** PRÁCTICA 4 ********************")
    print("**** Módulo de Administración de configuración *****\n")

    imprimirInfo()

    print("    1.- Generar archivo")
    print("    2.- Extraer archivo")
    print("    3.- Mandar archivo\n")

    opcion=int(input("Opcion elegida: "))

    if opcion==1:
        print("\n******************************************************\n")
        print("\n******************** Generar archivo *****************\n")
        print("\n******************************************************\n")

        ipTelnet = input("Ingrese la ip del dispositivo que quiere que se genere ell archivo: ")
        # ipTelnet = "192.168.0.1"

        tn = telnetlib.Telnet(ipTelnet)  # Se inicia  el Telnet

        tn.read_until(b"User: ")
        tn.write(user.encode('ascii') + b"\n")  # Se ingresa el usuario
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")  # Se ingresa el psw

        # Se comienzan a escribir los comandos para la creacion del archivo
        tn.write(b"enable\n")
        tn.write(b"config\n")
        tn.write(b"hostname Gen\n")  # Le cambiamos el hostname para verificaciones posteriores
        tn.write(b"exit\n")
        tn.write(
            b"copy running-config startup-config\n")  # Comando para la creación del archivo startup-config
        tn.write(b"exit\n")  # Se cierra conexión

        print(tn.read_all().decode('ascii'))  # Se muestran los comandos escritos

        print("\nSe ha creado el archivo ""startup-config\n")

    if opcion == 2:
        print("\n*********************************************************\n")
        print("\n******************** Extraer archivo ********************\n")
        print("\n*********************************************************\n")

        print("Se va a extraera el archivo startup-config del dispositivo que seleccione\n")

        ipFTP = input("Ingrese la ip del dispositivo: ")
        # ipFTP = "192.168.0.1"

        ftp = FTP(ipFTP, user, password)  # Iniciamos conexión con el servidor FTP
        print(
            "\n" + ftp.getwelcome())  # imprime el mensaje de bienvenida enviado por el servidor en respuesta a la conexión inicial

        print(ftp.retrbinary('RETR startup-config',
                             open('startup-config', 'wb').write))  # copiamos el archivo en la carpeta local
        print("\n")
        ftp.close()  # Cerramos conexión

        print("\nExtracción del archivo exitosa...")

    if opcion == 3:
        print("\n*********************************************************\n")
        print("\n******************** Mandar archivo ********************\n")
        print("\n*********************************************************\n")

        print("Se va a mandar el archivo statup-config a la direccion establecida\n")

        ipFTP = input("Ingrese la ip del dispositivo: ")
        # ipFTP = "192.168.0.1"

        ftp = FTP(ipFTP, user, password)

        fichero_origen = '/home/eduardo/Documentos/Redes 3/Practica4/Practica4/startup-config'
        ftp_raiz = '/'

        f = open(fichero_origen, 'rb')  # abrimos el fichero que tenemos en nuestra carpeta local
        ftp.cwd(ftp_raiz)  # nos posicionamos en raiz
        ftp.storbinary('STOR startup-config', f)  # copiamos el archivo
        f.close()  # cerramos fichero
        ftp.quit()  # cerramos conexion

        print("\nEnvio del archivo exitoso\n")

    resp = str(input("\n ¿Desea volver al menú? [S/N] "))
    resp = resp.upper()

print("\nHata luego =D")
