from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3


class Items(Resource):
    parse = reqparse.RequestParser()
    parse.add_argument('price',
                       type=float,
                       required=True,
                       help="this fild is Required"
                       )

    @jwt_required()
    def get(self, name):
        # for iteam in items:
        #     if(iteam['name']==name):
        #         return  iteam
        # using filter
        # iteam=next(filter(lambda x:x['name']==name,items),None)##one item for that next onely one iteam so None for avoid error
        # return {'iteam':iteam},200 if iteam else 404 #not found Status
        item = self.find_item_name(name)
        if item:
            return item
        return {"messange": "item not Found"}

    @classmethod
    def find_item_name(cls, name):
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

    def post(self, name):
        if Items.find_item_name(name):
            return {"message": "An Iteam with name '{}' already exist ".format(name)}, 400

        else:
            data = Items.parse.parse_args()  # if header is not specified
            # also can be used as silent=True

            item = {'name': name, "price": data['price']}

            try:
                self.insertion(item)
            except:
                return {"messange": "error ocurred while Inserting "}, 500
            return item, 201

        # creating status

    @classmethod
    def insertion(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        qurry = 'insert into items values (?,?)'
        cursor.execute(qurry, (item['name'], item['price']))
        connection.commit()
        connection.close()

    def delete(self, name):
        # global items
        # items=list(filter(lambda x:x['name']!=name,items))

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        qurry = 'delete from items where name=?'
        cursor.execute(qurry, (name,))
        connection.commit()
        connection.close()

        return {'message': 'item deleted'}

    def put(self, name):

        data = Items.parse.parse_args()
        # item=next(filter(lambda x:x['name']==name,items),None)
        item = self.find_item_name(name)
        updated_item = {"name": name, "price": data['price']}

        if item is None:
            try:
                self.insertion(updated_item)
            # item={"name":name,"price":data['price']}
            except:
                return {"message": "insertion fail"}
        else:
            try:
                self.update(updated_item)
            except:
                return {"message": "update item fail"}
        return updated_item

    @classmethod
    def update(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        qurry = 'update  items set price=? where name=?'
        cursor.execute(qurry, (item['price'], item['name']))
        connection.commit()
        connection.close()


class IteamList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        qurry = 'select * from items'
        result=cursor.execute(qurry)
        items=[]
        for row in result:
            items.append({"name":row[0],"price":row[1]})
        connection.commit()
        connection.close()
        return {"items":items}