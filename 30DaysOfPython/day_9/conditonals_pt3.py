# Exercises: Level 3

# Here we have a person dictionary.
person_dict ={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
person_dict_keys = person_dict.keys()

if 'skills' in person_dict_keys:
    print("'skills' does exist in the person dictionary")
    if len(person_dict['skills']) % 2 == 0:
        middle = len(person_dict['skills']) // 2 
    else:
        middle = len(person_dict['skills']) // 2
    print(f"The middle skill in skills is {person_dict['skills'][middle]}")



# Check if the person dictionary has skills key, if so check if the person has 'Python' skill 
# and print out the result.
if 'skills' in person_dict_keys:
    print("'skills' does exist in the person dictionary")
    if 'Python' in person_dict['skills']:
        print("The person does have Python skills")
print()


# If a person skills has only JavaScript and React, print('He is a front end developer'), 
# if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills 
# has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') 
# - for more accurate results more conditions can be nested!

title = ""

skill_set = set(person_dict['skills'])

if "Node" in skill_set and "MongoDB" in skill_set and "React" in skill_set:
    title = "fullstack"
elif "Node" in skill_set and "MongoDB" in skill_set and "Python" in skill_set:
    title = "backend"
elif "JavaScript" in skill_set and "React" in skill_set:
    title = "frontend"
else:
    title = "Unknown"

print(f"Person is a {title} developer!")












# If the person is married and if he lives in Finland, print the information in the following format: