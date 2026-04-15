# Day 12 - 30 Days of Python Challenge

# Exercises - Level 1
# Write a function which generates a six digit/character random_user_id.
import string
from random import random, randint

def generate_random_user_id():
    characters = string.ascii_letters + string.digits   
    random_user_id = ""
    
    for _ in range(6):
        random_user_id += characters[randint(0,len(characters)-1)]

    return random_user_id

print(generate_random_user_id())

# Modify the previous task. Declare a function named user_id_gen_by_user. 
# It doesn’t take any parameters but it takes two inputs using input(). 
# One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user(): 
    number_of_characters = int(input("Enter number of Characters: "))
    number_of_ids = int(input("Enter number of IDs: "))

    characters = string.ascii_letters + string.digits 
    ids = []


    for _ in range(number_of_ids):
        random_user_id = ""
        for _ in range(number_of_characters):
            random_user_id += characters[randint(0,len(characters)-1)]
        ids.append(random_user_id)

    return ids

generated_ids = user_id_gen_by_user()

for ids in generated_ids:
    print(ids)

# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_colour_gen():
    return f"rgb({randint(0,255)},{randint(0,255)},{randint(0,255)})"

print(rgb_colour_gen())


# Exercises: Level 2
# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. 
# Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f.) 
def list_of_hexa_colours(num):
    hexa_system = 'abcdef' + string.digits   
    colours = []

    for _ in range(num):
        hexa_code = ""
        for _ in range(6):
            hexa_code += hexa_system[randint(0,len(hexa_system)-1)]
        colours.append('#' + hexa_code)
    
    return colours

print(list_of_hexa_colours(3))

# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colours(num):
    colours = []

    for _ in range(num):
            red = randint(0,255)
            green = randint(0,255)
            blue = randint(0,255)
            colours.append(f"rgb({red},{green},{blue})")

    return colours

print(list_of_rgb_colours(3))

# Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colours(system, num):
    hexa_system = "abcdef" + string.digits   
    colours = []

    if system == 'hexa':
        for _ in range(num):
            hexa_code = ""
            for _ in range(6):
                hexa_code += hexa_system[randint(0,len(hexa_system)-1)]
            colours.append('#' + hexa_code)

    elif system == "rgb":
        for _ in range(num):
            red = randint(0,255)
            green = randint(0,255)
            blue = randint(0,255)
            colours.append(f"rgb({red},{green},{blue})")

    return colours

print(generate_colours("rgb", 2))
print(generate_colours('hexa', 2))


# Exercises: Level 3
# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
from random import shuffle
def shuffle_list(lst):
    shuffled_list = lst.copy()
    shuffle(shuffled_list)

    return shuffled_list
    

lst = ["a","b","c","d","e"]
print(shuffle_list(lst))

#Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def seven_random_numbers():
    random_numbers =[]

    while len(random_numbers) < 7 :
        number = randint(0,9)
        if number not in random_numbers:
            random_numbers.append(number)
    
    return random_numbers

print(seven_random_numbers())
