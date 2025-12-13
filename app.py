from helpers.database import app, db
from flask_restful import Api
from flask_migrate import Migrate
from flask_cors import CORS


CORS(app)


from resources.CBOResource import CBOResource, CBODetailResource

api = Api(app)
migrate = Migrate(app, db)

# Rotas da API

api.add_resource(CBOResource, "/CBOEntidades")
api.add_resource(CBODetailResource, "/cartorios/<int:codigo>")

if __name__ == "__main__":
    app.run(debug=True)
