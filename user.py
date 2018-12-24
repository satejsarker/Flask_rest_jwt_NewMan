import  sqlite3
from flask_restful import  Resource, reqparse

class  User:
    def __init__(self,_id,username,password):
        self.id =  _id
        self.username = username
        self.password = password
    @classmethod
    def find_by_username(cls,username):
        connection= sqlite3.connect('data.db')
        cursor=connection.cursor()
        qurry='select * from users where username=?'
        result=cursor.execute(qurry,(username,))
        row=result.fetchone()
        if row:
            #simplefy the class methord and class name
            user=cls(*row) #return the complete row
        else:
            user=None
        connection.close()
        return user

    @classmethod
    def find_by_id (cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        qurry = 'select * from users where id=?'
        result = cursor.execute(qurry, (_id,))
        row = result.fetchone()
        if row:
            # simplefy the class methord and class name
            user = cls(*row)  # return the complete row
        else:
            user = None
        connection.close()
        return user

class UserResgister(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="this fild is required ")
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="this fild cant be blank "
                        )

    def post(self):
        data=UserResgister.parser.parse_args()
        if User.find_by_username(data['username']):
            return  {'Message': "User name already Exist"},400
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        qurry='INSERT INTO users values (NULL ,?,?)'
        cursor.execute(qurry,(data['username'],data['password']))
        connection.commit()
        connection.close()
        return {'message':"new User created "},201
