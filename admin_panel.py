banned_users = set()

def ban_user(user_id):
    banned_users.add(user_id)

def is_banned(user_id):
    return user_id in banned_users
