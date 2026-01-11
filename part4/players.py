players = ["charles", "martina", "michael", "florence", "eli"]
print("Here are displaying list of players:")
print(players)

print("Here are the first three players on my team:")
print(players[0:3])

print("Here are the second three players on my team:")
print(players[1:4])

print("Here are the zero to third players on my team:")
print(players[:4])

print("Here are the third to the end players on my team:")
print(players[2:])

print("Here are the last three players on my team:")
print(players[-3:])

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
