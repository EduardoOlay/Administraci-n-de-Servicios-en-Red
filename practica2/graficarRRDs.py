import sys
import rrdtool
import time

strings_contabilidad = {
    'paquetes_multicast': 'Paquetes multicast que ha enviado la interfaz \nde la interfaz de red de un agente',
    'paquetes_ip': 'Paquetes IP que los protocolos locales (incluyendo ICMP)\n suministraron a IP en las solicitudes de transmisión.',
    'mensajes_icmp': 'Mensajes ICMP \nque ha recibido el agente',
    'segmentos_tcp': 'Número de segmentos TCP transmitidos que contienen\n uno o más octetos transmitidos previamente',
    'datagramas': 'Datagramas enviados por el dispositivo',
}


def generar_graficas_rrd(inicio, fin, nombre):

    rrdtool.dump("contabilidad_{}.rrd".format(nombre), "contabilidad_{}.xml".format(nombre))

    #separar cada datasorce para hacer su propia grafica
    for datasource, titulo in strings_contabilidad.items():
        ret = rrdtool.graphv( "{}_{}.png".format(nombre, datasource),
                             "--start",inicio,
                             "--end",fin,
                             "--vertical-label=Cantidad",
                             "--title={}".format(titulo),
                             "DEF:traficods=contabilidad_{}.rrd:{}:AVERAGE".format(nombre, datasource),
                             "LINE1:traficods#00ffb9:{}".format(datasource),#paquetes_multicast
                             )

"""
"DEF:traficoPaquetesIP=contabilidad.rrd:paquetes_ip:AVERAGE",
                         "LINE1:traficoPaquetesIP#f0932b:paq_ip",#paquetes IP
                         "DEF:traficoMensajesICMP=contabilidad.rrd:mensajes_icmp:AVERAGE",
                         "LINE1:traficoMensajesICMP#eb4d4b:men_icmp",#mensajes ICMP
                         "DEF:traficoSegmentosTCP=contabilidad.rrd:segmentos_tcp:AVERAGE",
                         "LINE1:traficoSegmentosTCP#6ab04c:seg_tcp",#segmentos TCP
                         "DEF:traficoDatagramas=contabilidad.rrd:datagramas:AVERAGE",
                         "LINE1:traficoDatagramas#0000FF:datagramas",#Datagramas
"""