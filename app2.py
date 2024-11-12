class elementos:  
    def __init__(self, fecha, agente, clientes, error):
        self.agente = agente #reportadoPor
        self.clientes = clientes #usuAfectados
        self.error = error #tipoerror
        self.fecha = fecha #fecha

class Fecha:
    def __init__(self, fecha, frec):
        self.fecha = fecha
        self.frec = frec    

class Correo_Fecha:
    def __init__(self, correo, fecha, num_rep):
        self.fecha = fecha
        self.correo = correo
        self.num_rep = num_rep

import re 
from xml.dom import minidom
import xml.etree.ElementTree as ET

def btnReset():
    if len(listainfo)>0:
       listainfo.clear()

listainfo = []



def datosRecibidos(info):
    listainfo = info
    print("Datos Recibidos, comenzando Parseo")

    #Mostrando datos de parseo en consola

    for l in listainfo:
        # imprimirfecha = re.findall('Guatemala.([0-2][0-9]|3[0-1])(\/|-)(0[1-9]|1[0-2])\2(\d{4})', l)
        fecha = re.findall('[0-9]+/[0-9]+/[0-9]+',l)
        print('Fecha:     ', fecha)

        # email = re.findall('([a-zA-z0-9])+@(ing|gmail|hotmail)?(\.usac\.edu)?(\.gt|\.com)', l)
        email = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', l)
        print('Reportado por:  ', email[0] )

        agente = email[0]
        email.pop(0)
        print('Afectados:            ', email)

        error = re.findall('Error.+\S', l)
        errores = error[0].replace('Error:','')
        print('Error:       ',errores)

        listainfo.append(elementos(fecha,agente,email,errores))

#@app
def format(info):
    salida = ET.tostring(info).decode()
    reescribe = minidom.parseString(salida)
    return reescribe.toprettyxml(indent="")

#@app
def XML():
    res = request.json
    text = res['archivo_xml']
    myfile = open('xmltemp.xml', 'w') 
    myfile.write(text)
    read_xml()
    return res


eventos = []
fecha = ''
agente =''
clientes = ''
error = ''

val = 0

def texto(info):
    global fecha, agente, clientes, error
    
    #Fecha
    if re.findall('^guatemala', info.lower()):
        print('fecha')
        fecha = info
    #Agente 
    elif re.findall('^reportado por: ', info.lower()):
        print('reportado por')
        agente = info
    #Clientes Afectados 
    elif re.findall('^usuarios afectados', info.lower()) or re.findall('@ing.usac.edu.gt$', info.lower()) :
        print('usuarios afectados')
        clientes += info
    #Errores
    elif re.findall('^error', info.lower()) or re.findall('.$', info.lower()):
        print('error')
        error+= cadena
        
    else:
        print('No hay correos que coincidan con el patron solicitado')




def salidaXML():
    global clientes, errores
    salida = minidom.parse('C:\Users\karen\Documents\-IPC2_Proyecto3_201900603\prueba.xml') #lo saca de otro archivo ya parseado
    evento = salida.getElementsByTagName('EVENTO')
    for w in range(len(evento)):
        aux =  open('estadisticas.xml','w')
        aux.write(evento[w].firstChild.data)
        aux.close()
        clientes = ''
        errores = ''
        lectura = open('estadisticas.txt','r')
        for archivo in lectura.readlines():
            linea = archivo.split()
            if len(linea) == 0:
                continue
            else:
                pasar_cadena(archivo.strip(' '))
        l=elementos(fecha,agente,clientes,error)
        eventos.append(l)
        lectura.close()         

vectfecha=[]
auxfecha=[]
auxfecha2=[]
def fechas():
    for d in eventos:
        j=d.fecha.split(',')
        j[1].strip('\n')
        auxfecha.append(j[1].strip(''))
        auxfecha2.append(j[1].strip(''))

    print('tama',len(auxfecha))
    aux = 0
    for d in range(len(auxfecha))
        print(d,'l',len(auxfecha))

        if len(auxfecha) == 0:
            break
        temp = auxfecha[0]

        for c in range(len(auxfecha2)):
            temporal = auxfecha2[c]
            if temp == temporal:
                print(d,'',aux,'fecha->',temp)
                aux +=1
                auxfecha.remove(temp)
        nofechas = Fecha(temp,aux)
        vectfecha.append(nofechas)        
        aux = 0
    for d in vectfecha:
        print(d.fecha,d.frec)



salidaXML()
fechas()                