# resources/CartorioResource.py
from flask_restful import Resource, reqparse
from flask import jsonify
from models import CBOEntidade
from helpers.database import db

# Parser para POST e PUT
cartorio_parser = reqparse.RequestParser()
cartorio_parser.add_argument("codigo", type=int, required=False)
cartorio_parser.add_argument("titulo", type=str, required=False)


class CBOResource(Resource):
    # GET all
    def get(self):
        entidade = CBOEntidade.query.all()
        return jsonify([
            {"id": c.id, "codigo": c.codigo, "titulo": c.titulo} 
            for c in entidade
        ])
    
class CBODetailResource(Resource):
    # GET by id
    def get(self, id):
        entidade = CBOEntidade.query.get(id)
        if entidade:
            return jsonify({"id": entidade.id, "codigo": entidade.codigo, "titulo": entidade.titulo})
        return {"message": "Cartório não encontrado"}, 404
        
    
    
    
    
    
    
    
    
    # # POST
    # def post(self):
    #     args = entidade_parser.parse_args()
    #     novo_cartorio = CBOEntidade(
    #         nome=args["nome"],
    #         email=args.get("email"),
    #         cnpj=args.get("cnpj")
    #     )
    #     db.session.add(novo_cartorio)
    #     db.session.commit()
    #     return {"message": "Cartório criado com sucesso", "id": novo_cartorio.id}, 201


    # # PUT
    # def put(self, id):
    #     cartorio = CBOEntidade.query.get(id)
    #     if not cartorio:
    #         return {"message": "Cartório não encontrado"}, 404
        
    #     args = cartorio_parser.parse_args()
    #     cartorio.nome = args["nome"]
    #     cartorio.email = args.get("email")
    #     cartorio.cnpj = args.get("cnpj")
    #     db.session.commit()
    #     return {"message": "Cartório atualizado com sucesso"}
    
    # # DELETE
    # def delete(self, id):
    #     cartorio = CBOEntidade.query.get(id)
    #     if not cartorio:
    #         return {"message": "Cartório não encontrado"}, 404
        
    #     db.session.delete(cartorio)
    #     db.session.commit()
    #     return {"message": "Cartório deletado com sucesso"}
