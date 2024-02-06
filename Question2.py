# • Create an empty dictionary called dog
dog = {}
# • Add name, color, breed, legs, age to the dog dictionary
dog.update({"Name": "Spot", "Color": "White", "Breed": "Dalmation", "Legs": "Long", "Age": "3 Years"})
print ("dog directory: ", dog)

# • Create a student dictionary and add first_name, last_name, gender, age, marital status,
# skills, country, city and address as keys for the dictionary
students = {"first_name": "", "last_name": "", "gender": "", "age": ""
            , "marital_status": "", "skills": [], "country": ""
            , "city": "", "address": ""}

# • Get the length of the student dictionary
print("Length of students directory: ", len(students))

# • Get the value of skills and check the data type, it should be a list
print("Skills category type: ",type(students.get("skills")))

# • Modify the skills values by adding one or two skills
students["skills"] += ["Programming", "Breathing"]
print("Full list: ", students)

# • Get the dictionary keys as a list
keysList = list(students.keys())
print("Keys: ", keysList)

# • Get the dictionary values as a list
valuesList = list(students.values())
print("Values: ", valuesList)
