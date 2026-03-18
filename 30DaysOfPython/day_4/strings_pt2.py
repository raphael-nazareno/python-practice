# Day 4 - 30 days Of Python Challenge pt 2

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
index_number = {0:'1st', 1:'2nd', 2:'3rd', 3:'4th', 4:'5th',
                5:'6th', 6:'7th', 7:'8th', 8:'9th', 9:'10th',
                10:'11th', 11:'12th', 12:'13th', 13:'14th', 14:'15th',
                31:"32st"}                                           # Dictionary for an index_number and their corresponding position in the str 

word_to_find = "because"
word_index = sentence.index(word_to_find)
word_position = index_number[word_index]

print("The first occurence of the word '", word_to_find, "' in the sentence is in the", word_position, "position")


# Use rindex to find the position of the last occurrence of the word 'because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"

word_to_find = "because"
word_index = sentence.rindex(word_to_find)  # Find index of last occurence of 'because'
word_number = str(word_index + 1)           # Actual position is index + 1 since index starts at 0
number_plus_suffix = ""                     # You wouldn't say 0th position

if word_number[-1] == '1':
    number_plus_suffix = word_number,"st"
elif word_number[-1] == '2':
    number_plus_suffix = word_number,"nd"
elif word_number[-1] == '3':
    number_plus_suffix = word_number,"rd"
else:
    number_plus_suffix = word_number,"th" # attached suffix depending on the last value in number

word_position = "".join(number_plus_suffix) # concatenates the position number and suffix

print("The last occurence of the word '", word_to_find, "' in the sentence is in the", word_position, "position")
print()


# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"

first_half_of_sentence = sentence[0:31]                             # Slices sentence just before the first 'because' 
second_half_of_sentence = sentence[-16:]                            # Slices sentence just after the last "because"
new_sentence = first_half_of_sentence + second_half_of_sentence     # combines both sentences together 
print(new_sentence)                     
# ----
sentence = "You cannot end a sentence with because because because is a conjunction"
because_string = "because because because "
new_sentence = sentence.replace(because_string, "")

print(new_sentence)
#-------
sentence = "You cannot end a sentence with because because because is a conjunction"
new_sentence = sentence.replace("because ", "")

print(new_sentence)
print()


# Does 'Coding For All' start with a substring Coding?
slogan = "Coding For All"
print("The str 'Coding For All' starts with substring 'Coding':", slogan.startswith("Coding"))
# Does 'Coding For All' end with a substring coding?
print("The str 'Coding For All' ends with substring 'coding':", slogan.endswith("Coding"))
print()

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
slogan_with_spaces = "   Coding For All      "
slogan_with_spaces_removed = slogan_with_spaces.strip()
print(slogan_with_spaces_removed)
print()

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. 
# Join the list with a hash with space string.
library = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
new_list = " - ".join(library)

print(new_list)
print()

# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
print("I am enjoying this challenge.\n")
print("I just wonder what is next.")
print()


# Use a tab escape sequence to write the following lines
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print("Name\t  Age\tCountry\t City")
print("Asabeneh  250\tFinland\t Helsinki")
print()

# Use the string formatting method to display the following:
# The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2

print(f"The area of a circle with radius {radius} is {area} meters square.")
print()

# Make the following using string formatting methods:
# 8 + 6 = 14                      
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2                                                   
# 8 // 6 = 1                                                    
# 8 ** 6 = 262144        
                                                                                                
a = 8                                                                                                          
b = 6  

print(f"{a} + {b} =", a + b)
print(f"{a} - {b} =", a - b)
print(f"{a} * {b} =", a * b)
print(f"{a} / {b} =", round(a / b, 2))
print(f"{a} % {b} =", a % b)
print(f"{a} // {b} =", a // b)
print(f"{a} ** {b} =", a ** b)