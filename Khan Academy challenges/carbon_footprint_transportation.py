footprint = 0

has_pet = input("Do you have a pet (yes/no)? ")
if has_pet == "yes":
    # Pets consume resources like water, litter, and toys.
    footprint = footprint + 5
    petfood_has_meat = input("Does your pet food contain any meat? (yes/no?) ")
    if petfood_has_meat == "yes":
        # Meat production uses more resources than non meat products.
        footprint = footprint + 10


days = int(input("How many days a week do you commute to school or work? "))

if days != 0 :
    transport = input("Do you commute by foot, bike, bus, train, or car? ")
# Different methods of transportation have different environmental impacts.
    if transport == "car":
        footprint = footprint + (8 * days)
    elif transport == "bus" or transport == "train":
        footprint = footprint + (4 * days)
    elif transport == "bike" or transport == "foot":
        footprint = footprint + days

print("Your environmental footprint score is " + str(footprint) + ".")
