import json
from flask import Flask, jsonify, request
from flask_restful import  Resource, Api
from tratajson import jsonPrepare
import os


#alteraçao para rodar em cloud
port = int(os.getenv('PORT', 8000))
app = Flask(__name__, static_url_path='')
api = Api(app)


#tratamento de erro funcao para payload
class erroRequest(Exception):
    def __init__(self, mensagem, code=422, payload=None):
        self.mensagem = mensagem
        self.code = code
        self.payload = payload

#captura de erro
@app.errorhandler(erroRequest)
def handle_bad_request(error):
    payload = dict(error.payload or ())
    payload['code'] = error.code
    payload['mensagem'] = error.mensagem
    return jsonify(payload), 422



class freelancer(Resource):
    #tratamento para GET nao implementado
    def get(self):
        try:
            mensagem = "GET nao foi desenvolvido para esta API. Favor executar POST com arquivo no formato JSON"
        except Exception:
            mensagem = "Erro no parametro GET. Procure o desenvolvedor"
        response = mensagem
        return response

    def post(self):
        try:
            data = json.loads(request.data)
            response = jsonPrepare(data)
        except Exception:
            raise erroRequest('Erro ao carregar JSON', 422)
        return response

api.add_resource(freelancer, '/freelancer')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)