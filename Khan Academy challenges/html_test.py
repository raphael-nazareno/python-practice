"""Fills in an HTML template with user data to construct a custom webpage."""

# Collect user profile data.
first_name = input("What's your first name? ")
user_email = input("What's your email address?: ")
user_bio = input("Write a short bio for your profile: ")

page = f"""
<!DOCTYPE html>
<html>
<head>
    <title>{first_name}'s Profile</title>
</head>
<body>

<h1>{first_name}'s profile</h1>
<h2>Hello, {first_name}!</h2>
<p>{user_email}</p>

<h2>About {first_name}</h2>
<p>{user_bio}</p>

<button>Like</button>
<p>Notifications: 4</p>

</body>
</html>
"""

# write to HTML file
with open("profile.html", "w") as file:
    file.write(page)

print("Profile page created: profile.html")