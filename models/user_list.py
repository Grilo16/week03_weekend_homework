from models.user_class import User
from models.book_list import book_list

admin = User("admin", "pass")
admin.admin = True
admin.login_auth = True
user1 = User("Shanda Leer", "1234")
user2 = User("lalal", "111")

def add_user(name_dict, id_dict, user_object):
    name_dict[user_object.name] = user_object
    id_dict[user_object.userid] = user_object

user_by_name = {}
user_by_id = {}


add_user(user_by_name, user_by_id, admin)
add_user(user_by_name, user_by_id, user1)
add_user(user_by_name, user_by_id, user2)