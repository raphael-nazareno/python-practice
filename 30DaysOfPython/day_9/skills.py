person_dict = {'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],}

skill_categories = {"fullstack": ["React", "Node", "MongoDB"],
                    "backend": ["Node", "Python", "MongoDB"],
                    "frontend": ["JavaScript", "React"],
                    }

skill_set = set(person_dict['skills'])
title = "unknown"

for category, required_skills in skill_categories.items(): # Loops through keys in dict, assigned category to keys and required_skills to values                                                        
    if set(required_skills).issubset(skill_set):           # If ALL of the skills required for a category are IN the person's skill_set then true
        title = category
        break

print(f"Person is a {title} developer!")
