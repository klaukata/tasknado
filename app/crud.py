from .database import users_collection

# auth related
def create_user(user_details):
    users_collection.insert_one(user_details.dict())
    return {
        'details': 'User created!'
    }