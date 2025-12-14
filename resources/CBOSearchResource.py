from flask_restful import Resource
from flask import request, jsonify
from helpers.solr import solr

class CBOSearchResource(Resource):
    def get(self):
        q = request.args.get("q", "*:*")

        resultados = solr.search(
            q,
            **{
                "defType": "edismax",
                "qf": "titulo",
                "rows": 20
            }
        )

        return jsonify([
            {
                "id": r["id"],
                "codigo": r["codigo"],
                "titulo": r["titulo"]
            }
            for r in resultados
        ])
