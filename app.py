from helpers.application import app, api
from helpers.database.database import db
from flask_migrate import Migrate
from flask_cors import CORS

from resources.CBOResource import CBOResource, CBODetailResource
from resources.CBOSearchResource import CBOSearchResource

# CORS
CORS(app)

# Migrate
migrate = Migrate(app, db)

# Rotas
api.add_resource(CBOResource, "/CBOEntidades")
api.add_resource(CBODetailResource, "/CBOEntidades/<int:id>")
api.add_resource(CBOSearchResource, "/CBOEntidades/buscar")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
