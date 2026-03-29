
# DATA
person_dict = {'skills': ['JavaScript', 'Node', 'React', 'MongoDB', 'Python'],}

skill_categories = {"fullstack": ["React", "Node", "MongoDB"],
                    "backend": ["Node", "Python", "MongoDB"],
                    "frontend": ["JavaScript", "React", "HTML"],
                    }

skill_scores = {"fullstack": 0,
                "backend": 0,
                "frontend": 0
                }

skill_priorities = {"fullstack": 1,
                    "backend": 2,
                    "frontend": 3   
                    }

skill_list = person_dict['skills']
title = "unknown"


# SCORING SYSTEM
for category, required_skills in skill_categories.items(): # Loops through keys in dict, assigned category to keys and required_skill to values                                                        
    for required_skill in required_skills:
        if required_skill in skill_list:
            skill_scores[category] += 1



# Determining highest score
scores = skill_scores.values()
highest_score = max(scores)

high_score_categories =[]

for score in skill_scores.items():
    if score[1] == highest_score:
        high_score_categories.append(score[0])

if len(high_score_categories) == 1:
    title = high_score_categories[0]


# Determining title from priorities
current_best = high_score_categories[0]
for category in high_score_categories:
    if skill_priorities[current_best] > skill_priorities[category]:
        current_best = category

title = current_best



print(f"Person is a {title} developer!")
