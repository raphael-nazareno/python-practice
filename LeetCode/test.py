
ransomNote = "aa"
magazine = "aab"


mag_dict ={}

for letter in magazine:
    if letter not in mag_dict:
        mag_dict[letter] = 1
    else:
        mag_dict[letter] += 1

for leter in ransomNote:
    if letter in mag_dict and mag_dict[letter] != 0:
        mag_dict[letter] -= 1
    else:
        return False
return True