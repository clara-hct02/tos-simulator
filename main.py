import random

# SET UP THE GAME

# INITIALIZE THE PLAYERS AND THEIR ROLES
# Ask for total number of players
while True:
    try:
        players = input("Please enter your total number of players (9-16):\n")
        players = int(players)
    except ValueError:
        print("Invalid input, please input a valid integer")
        continue
    if players > 16 or players < 9:
        print("Please enter a number between 9 and 16")
    else:
        break

# Set the number of coven and townies
# Choose the players that will be the coven
coven = players // 3
town = players - coven
print(coven)
# These players are the coven
coven_players = random.sample(range(1, players), coven)
# Keeps track of the living players
living_players = list(range(1, players))

# Start the game on day 1
day = 1

# The actual game happens here
while 0 < coven <= town:
    # Daytime events
    print("Day " + str(day))
    if day != 1:
        print("The discussion period may begin, please make your claims")
        print("The town may now vote on who they wish to lynch")
        # Use rng to figure out who was voted out
        lynched = random.choice(living_players)
        living_players.pop(living_players.index(lynched))
        print("The town has voted out " + str(lynched))
        if lynched in coven_players:
            print(str(lynched) + " was a member of the coven")
            coven -= 1
        else:
            print(str(lynched) + " was an innocent town member")
            town -= 1
        if coven == 0 or coven > town:
            break
        # input("Press enter to continue")
    else:
        print("Welcome, please take your leave for tonight")
        # input("Press enter to continue")

    # Nighttime events
    print("Night " + str(day))
    print("The coven may kill a townie tonight")
    killed = random.choice(living_players)
    if killed in coven_players:
        print("The coven's target could not be killed!")
    else:
        living_players.pop(living_players.index(killed))
        print("The coven has killed " + str(killed))
        town -= 1
    day += 1
    print("There are " + str(town) + " townies remaining")
    print("There are " + str(coven) + " coven members remaining")
    # input("Press enter to continue")

# Announce the winner of the game
if coven == 0:
    print("The town has won!")
else:
    print("The coven has won!")
    
    
