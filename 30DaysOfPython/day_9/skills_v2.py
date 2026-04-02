# DATA
person_dict = {'skills': ['JavaScript', 'Node', 'MongoDB', 'Python'],}

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
            skill_scores[category] += 1   # If a required skill is found in the person's skill list, the category the skill is associated with is assigned one point


# Determining highest score
scores = skill_scores.values()  
highest_score = max(scores)    # Evalutes highest score from a list of the categories' scores
high_score_categories =[]

for score in skill_scores.items():       # Checks the scores, compares those scores with the highest score found and if a score is equal to the highest, 
    if score[1] == highest_score:        # its corresponding category is noted in a list
        high_score_categories.append(score[0])  


# Determining title from highest scoring category
if len(high_score_categories) == 1:    # Checks if only one category has the highest score.
    title = high_score_categories[0]   
# Determining title from priorities if there is a tie in score
elif len(high_score_categories) > 1:   # Checks if more than one category has the highest score
    current_best = high_score_categories[0]
    for category in high_score_categories:
        if skill_priorities[current_best] > skill_priorities[category]:
            current_best = category
    title = current_best


# Outputting Job title depending on skillset
if len(skill_list) == 1:
    skills = skill_list[0]
elif len(skill_list) == 2:
    skills = "and ".join(skill_list)
else:
    start_of_list = ", ".join(skill_list[:-1]) 
    end_of_list = ", and " + skill_list[-1]
    skills = start_of_list + end_of_list

print(f"Person is proficient in {skills}. Therefore is a {title} developer!")
