# Placeholder for MongoDB models if you choose to abstract collections

# Example: MongoDB collection abstraction
def get_user_collection():
    from app import db
    return db['users']

def get_account_collection():
    from app import db
    return db['accounts']

# You can add more collection abstractions here.
