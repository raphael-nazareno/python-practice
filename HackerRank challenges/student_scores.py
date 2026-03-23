python_students = []
scores = []
students = []

for a in range(int(input())):
    name = input("name:")
    score = float(input("score:"))

    records = [name, score]

    scores.append(score)            # adds score to scores list
    python_students.append(records) # name and score to python_students list as nested list [[name, score], [name,score]]

min1 = min(scores)
scores.sort()

for x in scores:
    if x > min1:
        second_lowest = x
        break                  # sorts though scores list and breaks loops after first value larger than the minimum

for x in python_students:
    if x[1] == second_lowest:
        students.append(x[0])  # if a score is equal to the lowest in nested list, add the name to another list.

students.sort()

for x in students:
    print(x)                   # print students name who score the second lowest    




    


    







        