# Day 8 - 30 Days Of Python Challenge

# Exercises: Level 1

# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog = {"name":"Doggy", "colour":"Black","breed":"German Shepherd", "Legs":4, "age":5}
print(dog["name"])
print()

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, 
# country, city and address as keys for the dictionary
student_dict = {"first_name":"Raphael", 
                "last_name":"Manalo", 
                "gender":"Male", 
                "age":23, 
                "marital_status":"Partnered",
                "skills":["Python", "Java", "HTML", "JavaScript"],
                "country":"Australia",
                "city":"Melbourne",
                "address": 
                    {"street": "123 Guest Street", 
                    "suburb": "Suburb 2"}
                }

# Get the length of the student dictionary
print(len(student_dict))
print()

# Get the value of skills and check the data type, it should be a list
print(f"{student_dict["skills"]} and {type(student_dict['skills'])}")
print()

# Modify the skills values by adding one or two skills
student_dict["skills"].append("CCST")
print(f"{student_dict['skills']}")
print()

# Get the dictionary keys as a list
keys = list(student_dict.keys())
print(keys)
print()

# Get the dictionary values as a list
values = list(student_dict.values())
print(values)
print()

# Change the dictionary to a list of tuples using items() method 
student_tuple = student_dict.items()
print(student_tuple)
print()

# Delete one of the items in the dictionary
student_dict.pop('city')
print(student_dict)
print()

# Delete one of the dictionaries
del student_dict