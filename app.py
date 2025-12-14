from helpers.database import app, db
from flask_restful import Api
from flask_migrate import Migrate
from flask_cors import CORS

from resources.CBOResource import CBOResource, CBODetailResource
from resources.CBOSearchResource import CBOSearchResource

CORS(app)

api = Api(app)
migrate = Migrate(app, db)

# Rotas
api.add_resource(CBOResource, "/CBOEntidades")
api.add_resource(CBODetailResource, "/CBOEntidades/<int:id>")
api.add_resource(CBOSearchResource, "/CBOEntidades/buscar")

if __name__ == "__main__":
    app.run(debug=True)
