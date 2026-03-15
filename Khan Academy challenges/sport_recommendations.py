# Recommendation variable is blank to begin with to prevent unwanted outputs
recommendation = ""

# --- Sport options ---
# Store all possible recommendations
volleyball = "Volleyball"
basketball = "Basketball"
baseball = "Baseball"
soccer = "Soccer"
swimming = "Swimming"
mma = "Mixed Martial Arts (MMA)"
tennis = "Tennis"
mongolian_wrestling = "Mongolian Wrestling"


# --- Input validation ---
# Asks the user questions and repeats the question until the user enters a valid answer.
while True:
    team_or_individual = input("Do you prefer team sports or individual sports? (Enter 'team' or 'individual'): ").lower()
    if team_or_individual == "team" or team_or_individual == "individual":
        break
    else:
        print("Invalid input. Please enter 'team' or 'individual'.")

while True:
    location = input("Do you prefer indoor or outdoor sports? (Enter 'indoor' or 'outdoor'): ").lower()
    if location == "indoor" or location == "outdoor":
        break
    else:
        print("Invalid input. Please enter 'indoor' or 'outdoor'")

while True:
    level_of_contact = input("Do you prefer high-contact or low-contact sports? (Enter 'high' or 'low'): ").lower()
    if level_of_contact == 'high' or level_of_contact == 'low':
        break
    else:
        print("Invalid input. Please enter 'high' or 'low'")


# --- Recommendation Logic ---
# Determine sport based on preferences
if team_or_individual == "team":
    if location == "indoor":
        if level_of_contact == "high":
            recommendation = basketball
        elif level_of_contact == "low":
            recommendation = volleyball
    
    elif location == "outdoor":
        if level_of_contact == "high":
            recommendation = soccer
        elif level_of_contact == "low":
            recommendation = baseball

elif team_or_individual == "individual":
    if location == "indoor":
        if level_of_contact == "high":
            recommendation = mma
        elif level_of_contact == "low":
            recommendation = swimming

    elif location == "outdoor":
        if level_of_contact == "high":
            recommendation = mongolian_wrestling
        elif level_of_contact == "low":
            recommendation = tennis

# --- Output Results ---
# Display recommended sport
print("\nBased on your preferences, we recommend you try: " + recommendation + "!")

                           