# Day 4 - 30 Days of Python Challenge

# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
message = ["Thirty", "Days", "Of", "Python"]
result = " ".join(message)
print(result)
print()

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
message = ["Coding", "For", "All"]
result = " ".join(message)
print(result)
print()

# Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# Print the variable company using print().
print(company)
print()

# Print the length of the company string using len() method and print().
print("print(len(company)):")
print(len(company))
print()

# Change all the characters to uppercase letters using upper() method.
print("print(company.upper()):")
print(company.upper())
print()

# Change all the characters to lowercase letters using lower() method.
print("print(company.lower()):")
print(company.lower())
print()

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())
print()

# Cut(slice) out the first word of Coding For All string.
last_two_words = company[7:]
print(last_two_words)
print()

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index('Coding'))
print(company.find('Coding'))
print("'company' starts with 'Coding:'", company.startswith('Coding'))
print()

# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))
print()

# Change "Python for Everyone" to "Python for All" using the replace method or other methods.
slogan = "Python for Everyone"
print(slogan.replace('Everyone', 'All'))
print()

# Split the string 'Coding For All' using space as the separator (split()) .
coding_for_all = "Coding For All"
print(coding_for_all.split(" "))
print()

#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(", "))
print()

# What is the character at index 0 in the string Coding For All.
print("Character at index 0 for 'Coding For All' string is:", coding_for_all[0])
# What is the last index of the string Coding For All.
print("Character at the last index for 'Coding For All' string is:", coding_for_all[-1])
# What character is at index 10 in "Coding For All" string.
print("Character at index 10 for 'Coding For All' string is:", coding_for_all[10])
print()

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
slogan = "Python For Everyone"
split_slogan = slogan.split(" ")
print(split_slogan[0][0], split_slogan[1][0], split_slogan[2][0],sep=".") # first [] return substring, second [] returns character. 
print()                                                                         # ie [0][0] returns the first character of the first substring.

# Create an acronym or an abbreviation for the name 'Coding For All'.
slogan_two = "Coding For All"
split_slogan_two = slogan_two.split(" ")
print(split_slogan_two[0][0], split_slogan_two[1][0], split_slogan_two[2][0], sep=".")
print()

# Use index to determine the position of the first occurrence of C in Coding For All.
# Use index to determine the position of the first occurrence of F in Coding For All.
coding_for_all = "Coding For All"
index_number = {0:'1st', 1:'2nd', 2:'3rd', 3:'4th', 4:'5th',
                5:'6th', 6:'7th', 7:'8th', 8:'9th', 9:'10th'}   # Dictionary for an index_number and their corresponding position in the str 

letters = ('C', 'F')
for a in range(0,2,1):    # Loops script until all of the letters in the list are checked
    letter = letters[a]

    index_value = coding_for_all.index(letter)  # Index number for first occurence of a letter in str
    letter_postion = index_number[index_value]  # Returns position number from dictionary by calling index_value

    print("The first occurrence of the letter", letter, "in the str '", coding_for_all, "' is in the", letter_postion, "position")

print()
# Use rfind to determine the position of the last occurrence of l in Coding For All People.
coding_for_all_people = "Coding For All People"
index_number = {0:'1st', 1:'2nd', 2:'3rd', 3:'4th', 4:'5th',
                5:'6th', 6:'7th', 7:'8th', 8:'9th', 9:'10th',
                10:'11th', 11:'12th', 12:'13th', 13:'14th', 14:'15th'}   # Dictionary for an index_number and their corresponding position in the str 

letters = ('l')
for a in range(0,1,1):    # Loops script until all of the letters in the list are checked
    letter = letters[a]

    index_value = coding_for_all.rfind(letter)  # Index number for last occurence of a letter in str
    letter_postion = index_number[index_value]  # Returns position number from dictionary by calling index_value

    print("The last occurrence of the letter", letter, "in the str '", coding_for_all_people, "' is in the", letter_postion, "position")








