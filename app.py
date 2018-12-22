from flask import Flask,jsonify,request
from flask_restful import  Resource,Api,reqparse
from flask_jwt import  JWT,jwt_required
from Security import  authenticate,identity

app = Flask(__name__)
app.secret_key='satej@)((!!!klnvlknsdfiasdasdmnnjan$$%'

api=Api(app)
jwt=JWT(app,authenticate,identity)

##demo in maemory data

items=[

]

class Items(Resource):
    parse = reqparse.RequestParser()
    parse.add_argument('price',
                       type=float,
                       required=True,
                       help="this fild is Required"
                       )
    @jwt_required()
    def get(self,name):
        # for iteam in items:
        #     if(iteam['name']==name):
        #         return  iteam
        #using filter
        iteam=next(filter(lambda x:x['name']==name,items),None)##one item for that next onely one iteam so None for avoid error
        return {'iteam':iteam},200 if iteam else 404 #not found Status


    def post(self,name):
        if(next(filter(lambda x:x['name']==name,items),None)) is not None:
            return {"message":"An Iteam with name '{}' already exist ".format(name)} , 400

        else:
            data = Items.parse.parse_args() # if header is not specified
            # also can be used as silent=True

            item = {'name': name, "price": data['price']}
            items.append(item)
            return item, 201

         #creating status
    def delete(self,name):
        global items
        items=list(filter(lambda x:x['name']!=name,items))
        return {'message':'item deleted'}

    def put(self,name):

        data=Items.parse.parse_args()
        item=next(filter(lambda x:x['name']==name,items),None)
        if item is None:
            item={"name":name,"price":data['price']}
        else:
            item.update(data)
        return item

class IteamList(Resource):
    def get(self):
        return {"iteams":items}

#Route
api.add_resource(Items,'/iteam/<string:name>')
api.add_resource(IteamList,'/iteams')
if __name__ == '__main__':
    app.run(port=8000)
