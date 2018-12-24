from flask_restful import Resource,reqparse
from flask_jwt import  jwt_required
import  sqlite3
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
        # iteam=next(filter(lambda x:x['name']==name,items),None)##one item for that next onely one iteam so None for avoid error
        # return {'iteam':iteam},200 if iteam else 404 #not found Status
        item=self.find_item_name(name)
        if item:
            return item
        return{"messange":"item not Found"}
    @classmethod
    def find_item_name(cls,name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        qurry = 'SELECT * FROM items where name=?'
        result = cursor.execute(qurry, (name,))
        row = result.fetchone()
        connection.close()
        if row:
            return {
                'item': {'name': row[0], 'price': row[1]}
            }
    def post(self,name):
        if Items.find_item_name(name):
            return {"message":"An Iteam with name '{}' already exist ".format(name)} , 400

        else:
            data = Items.parse.parse_args() # if header is not specified
            # also can be used as silent=True

            item = {'name': name, "price": data['price']}
            connection=sqlite3.connect('data.db')
            cursor=connection.cursor()
            qurry='insert into items values (?,?)'
            cursor.execute(qurry,(item['name'],item['price']))
            connection.commit()
            connection.close()
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