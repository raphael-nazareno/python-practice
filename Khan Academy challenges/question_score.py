score = 0

answer = input("What data type is the value 6.3? ")
if answer == "float":
    print("You got it!")
    score = score + 1
elif answer == "integer":
    print("Integers can't have decimals.")
else:
    print("The correct answer is float.")
    

answer = int(input("What does len(\"hi\") evaluate to? "))
if answer == 2:
    print("You got it!")
    score = score + 1
else:
    print("The correct answer is 2.")

if score >= 2:
    answer = input("BONUS QUESTION: Who created python?: ")
    if answer == "Guido van Rossum" or answer == "Rossum" or answer == "Guido":
        print("You got it!")
        score = score + 1
    else:
        print("It was actually Guido van Rossum")
    


final_score = str(score)
print("Your final score is " + final_score + "!")