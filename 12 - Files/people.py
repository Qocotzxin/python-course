keys = ["id", "first_name", "last_name", "dob"]
file = open("people.txt", "r")
lines = file.readlines()
file.close()

for l in lines:
    user = dict(zip(keys, l.replace("\n", "").split(";")))
    print("---------")
    print("ID: " + user["id"])
    print("First Name: " + user["first_name"])
    print("Last Name: " + user["last_name"])
    print("Date of birth: " + user["dob"])
    print("---------")
