import json

def load_profile(user_id):
    with open("data/users.json", "r") as f:
        users = json.load(f)
    return users.get(str(user_id), {})

def save_profile(user_id, profile):
    with open("data/users.json", "r") as f:
        users = json.load(f)
    users[str(user_id)] = profile
    with open("data/users.json", "w") as f:
        json.dump(users, f, indent=4)
