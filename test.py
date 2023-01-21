import json

with open("./items.json",mode="r") as file:
    data = json.load(file)
del data["timering"][data["timering"].index("1234")]
print(data)