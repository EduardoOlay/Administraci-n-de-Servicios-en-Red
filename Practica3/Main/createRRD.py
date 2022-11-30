import rrdtool

# por cada atributo de monitorización crear su Data Source correspondiente
atributos_monitorizacion = [
    'carga_CPU',
    'uso_RAM',
    'trafico_Red_Entrada',
    'trafico_Red_Salida'
]

#guarda un dia en resolucion de un minuto
def crear_rrd(nombre_agente):
    datasources = []
    for atributo in atributos_monitorizacion:
        datasources.append("DS:{}:GAUGE:60:0:900000000".format(atributo))
    ret = rrdtool.create("/home/eduardo/Documentos/Redes 3/Practica3/RRD/trend.rrd",
                             "--start", 'N',
                             "--step", '60',#acepta info cada 60 segundos
                             datasources,
                             "RRA:AVERAGE:0.5:1:24")

    if ret:
        print(rrdtool.error())
    #rrdtool.dump("/home/eduardo/Documentos/Redes 3/Practica3/RRD/trend_{}.rrd".format(nombre_agente))