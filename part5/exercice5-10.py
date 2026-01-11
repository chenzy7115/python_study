current_user = ['admin', 'eric', 'willie', 'erin','michael']
current_user = [user.lower() for user in current_user]
print(current_user)
new_user = ['chris', 'david', 'admin', 'eric']
new_user = [user.lower() for user in new_user]
print(new_user)
for user in new_user:
    if user in current_user:
        print(f"ID {user} already exists.")
    else:
        print(f"ID {user} is available.")