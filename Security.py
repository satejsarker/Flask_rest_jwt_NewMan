from werkzeug.security import safe_str_cmp

from user import User
#Old style
# users = [
#     User(1, 'satej', 'sarker')
# ]
#
# username_maping = {u.username: u for u in users}
# userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    # user = username_maping.get(username, None)
    user=User.find_by_username(username)
    if user and safe_str_cmp(user.password,password):
        return user
def identity(payload):
    user_id=payload['identity']
    return  User.find_by_id(user_id)
#
#
# def authenticate(username, password):
#     user = username_maping.get(username, None)
#
#     if user and safe_str_cmp(user.password,password):
#         return user
# def identity(payload):
#     user_id=payload['identity']
#     # return  User.find_by_id(user_id)
#     return userid_mapping.get(user_id,None)