address = "1.1.1.1"

defanged_address = address.replace(".","[.]")

print(defanged_address)

for item in address:
    if item == ".":
        item = "[.]"

print(address)