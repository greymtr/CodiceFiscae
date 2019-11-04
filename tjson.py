import json

x="""{name:"Matt",surname:"Edabit",gender:"M",dob:"1/1/1900"}"""

print(x)

y=json.loads(x)

print(y["name"])

