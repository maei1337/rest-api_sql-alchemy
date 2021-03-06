from flask import Flask
from flask_jwt import JWT
from security import authenticate, identity
from flask_restful import Api

from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = False

### ACHTUNG
app.secret_key = 'matthias' # Das sollte nich öffentlich einsehbar sein
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

### ACHTUNG
jwt = JWT(app, authenticate, identity) #/auth

api.add_resource(ItemList, '/items')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

#### IMPORT VON DB
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
