from flask_restful import Resource
from flask import jsonify
from models.CBOModel import CBOEntidade

class CBOResource(Resource):
    # GET all (Postgres)
    def get(self):
        entidades = CBOEntidade.query.all()
        return jsonify([
            {
                "id": c.id,
                "codigo": c.codigo,
                "titulo": c.titulo
            }
            for c in entidades
        ])

class CBODetailResource(Resource):

    def get(self, id):
        entidade = CBOEntidade.query.get(id)
        if entidade:
            return jsonify({
                "id": entidade.id,
                "codigo": entidade.codigo,
                "titulo": entidade.titulo
            })
        return {"message": "CBO não encontrado"}, 404
