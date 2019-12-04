import json
x='{"info": [{"name": "sam", "id": 1}, {"name": "joy", "id": 2}, {"name": "mic", "id": 3}], "details": [{"name": "sam", "des": "tester"}, {"name": "joy", "des": "Developer"}, {"name": "mic", "des": "automation"}]}'
c=json.loads(x)


a=int(input("Enter the ID : "))
b=str()
for i in c["info"]:
    if a==i["id"]:
        print("Name "+ i["name"])
        b=i["name"]
for j in c["details"]:
    if b==j["name"]:
        print("position :"+j["des"])
