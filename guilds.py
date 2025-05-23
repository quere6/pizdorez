import json

def load_guilds():
    with open("data/guilds.json", "r") as f:
        return json.load(f)

def save_guilds(guilds):
    with open("data/guilds.json", "w") as f:
        json.dump(guilds, f, indent=4)
