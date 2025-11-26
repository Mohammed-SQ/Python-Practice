usernames = ["alex99", "maria01", "johnny", "sara88"]

print("Existing usernames:", usernames)

# Ask for new username
new_user = input("Enter a new username: ")

# Case-insensitive comparison:
lower_list = []
for u in usernames:
    lower_list.append(u.lower())

# Step 1: Check if username exists
if new_user.lower() in lower_list:
    print("Username already exists!")

    # Step 2: Keep adding numbers until unique
    base = new_user
    number = 1

    # Try base + number, base + (number+1), etc.
    generated = base + str(number)
    while generated.lower() in lower_list:
        number += 1
        generated = base + str(number)

    print("New username generated:", generated)
    usernames.append(generated)

else:
    # Not in list → just add it
    usernames.append(new_user)

# Print updated list
print("Updated list:", usernames)
