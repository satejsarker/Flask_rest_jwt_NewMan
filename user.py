import  sqlite3
class  User:
    def __init__(self,_id,username,password):
        self.id =  _id
        self.username = username
        self.password = password
    # @classmethod
    # def find_by_username(cls,username):
    #     connection= sqlite3.connect('database.db')
    #     cursor=connection.cursor()
    #     qurry='select * from users where username=?'
    #     result=cursor.execute(qurry,(username,))
    #     row=result.fetchone()
    #     if row:
    #         #simplefy the class methord and class name
    #         user=cls(*row) #return the complete row
    #     else:
    #         user=None
    #     connection.close()
    #     return user
    #
    # @classmethod
    # def find_by_id (cls, _id):
    #     connection = sqlite3.connect('database.db')
    #     cursor = connection.cursor()
    #     qurry = 'select * from users where id=?'
    #     result = cursor.execute(qurry, (_id,))
    #     row = result.fetchone()
    #     if row:
    #         # simplefy the class methord and class name
    #         user = cls(*row)  # return the complete row
    #     else:
    #         user = None
    #     connection.close()
    #     return user
