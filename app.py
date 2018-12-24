from flask import Flask
from flask_restful import  Api
from flask_jwt import  JWT
from Security import  authenticate,identity
from user import  UserResgister
from item import Items , IteamList
app = Flask(__name__)
app.secret_key='satej@)((!!!klnvlknsdfiasdasdmnnjan$$%'

api=Api(app)
jwt=JWT(app,authenticate,identity)

##demo in maemory data
#Route
api.add_resource(Items,'/iteam/<string:name>')
api.add_resource(IteamList,'/iteams')
api.add_resource(UserResgister,'/register')
if __name__ == '__main__':
    app.run(port=8000)
