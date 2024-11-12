from flask import Flask, jsonify, request
from flask_cors import CORS
import app2

app = Flask(__name__)
CORS(app)

#info =listadatos

XML = []
@app.route('/inicio')    #peticion
def inicio():
    return jsonify({'mensaje': 'Ejecutando el servidor'})

#Mandar datos y editarlos para el textarea
@app.route('/recibirXML', methods=['POST'])
def recibirXML():
    global XML
    datosXML = request.json['datos']

    print(request.json['datos'])

    eventos = datosXML.split("</EVENTO>")
    eventos.pop(len(eventos)-1)

    app2.datosRecibidos(eventos)
    return jsonify({'mensaje':'Recibido en Backend' })

#Resetear el Frontend
@app.route('/reset', methods=['GET'])
def reset():
    print('Datos Borrados')
    app2.btnReset()
    return jsonify({'mensaje': 'Reiniciando, espere un momento'})


if __name__=='__main__':
    app.run( debug=True, port=5000)  #5000



#Primero se ejecuta Flask y luego se corre el server de Django


    # for h in datos1:
    #     h = h.replace('<EVENTO>','')
    #     h = h.replace('\n', '')
    #     h = h.replace('\t', '')
    #     h = h.replace('>', '')
    #     XML.append(h)
    # XML.pop(len(datos1) - 1)

    # #Mandando al Frontend
    # app2.datosRecibidos(XML)
    # XML.clear()     
    # return jsonify({'Recibido en Backend': request.json['datos']})

# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Hello, Flask!"