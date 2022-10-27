from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

import pymongo
import certifi

app=Flask(__name__)
cors = CORS(app)
#importar controladores
from Controladores.ControladorCandidato import ControladorCandidato
controllerCandidato=ControladorCandidato()

#Accesos
@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Servidor en ejecución ..."
    return jsonify(json)

#Micro Servicio de Listado de Estudiantes
@app.route("/candidatos",methods=['GET'])
def getCandidatos():
    print("Micro Servicio Listando los candidatos...")
    json=controllerCandidato.index()
    return jsonify(json)

#Micro Servicio de Creacion de Candidatos
@app.route("/candidatos",methods=['POST'])
def crearCandidato():
    print("Micro Servicio Creando candidato....")
    data = request.get_json()
    json=controllerCandidato.create(data)
    return jsonify(json)

#Consultar candidato
@app.route("/candidatos/<string:id>",methods=['GET'])
def getCandidato(id):
    print("Micro Servicio de Consultar el candidato con id: " + id)
    json=controllerCandidato.show(id)
    return jsonify(json)

#Actualizar Candidato
@app.route("/candidatos/<string:id>",methods=['PUT'])
def modificarCandidato(id):
    print("Micro Servicio Actualizando candidato: " + id)
    data = request.get_json()
    json=controllerCandidato.update(id,data)
    return jsonify(json)

#Eliminar Candidato
@app.route("/candidatos/<string:id>",methods=['DELETE'])
def eliminarCandidato(id):
    print("Micro Servicio Se eliminara el candidato con id: " + id)
    json=controllerCandidato.delete(id)
    return jsonify(json)

def loadFileConfig():
    with open('config.json') as file:
        data = json.load(file)
    return data

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

if __name__=='__main__':
    print_hi('Ciclo 4 Mision TIC 2022 TDVJ')
    dataConfig = loadFileConfig()
    print("Server ejecutandose : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])

""" 
ca = certifi.where()

client = pymongo.MongoClient("mongodb+srv://usuario-votaciones:Pruebas2022@cluster0.b1xs3bm.mongodb.net/bd-registro-votaciones?retryWrites=true&w=majority",tlsCAFile=ca)
db = client.test
print(db)

baseDatos = client["bd-registro-votaciones"]
print(baseDatos.list_collection_names())
"""
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
