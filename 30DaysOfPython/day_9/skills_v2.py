person_dict = {'skills': ['JavaScript', 'Node', 'MongoDB', 'Python'],}

skill_categories = {"fullstack": ["React", "Node", "MongoDB"],
                    "backend": ["Node", "Python", "MongoDB"],
                    "frontend": ["JavaScript", "React", "HTML"],
                    }

skill_scores = {"fullstack": 0,
          "backend": 0,
          "frontend": 0
          }

skill_list = person_dict['skills']
title = "unknown"

for category, required_skills in skill_categories.items(): # Loops through keys in dict, assigned category to keys and required_skill to values                                                        
    
    for required_skill in required_skills:

        if required_skill in skill_list:

            if category == "fullstack":
                skill_scores[category] += 1

            elif category == "backend":
                skill_scores[category] += 1

            elif category == "frontend":
                skill_scores[category] += 1 

print(skill_scores)

scores = skill_scores.values()
highest_score = max(scores)

for score in skill_scores.items():
    if score[1] == highest_score:
        title = score[0]



print(f"Person is a {title} developer!")
