#301 GAME

#DEFINE NUMBER OF THROWS
numthrows = 3 

#PRINT GAME TITLE
print("Game: 301")
print(" ")

#ENTER NUMBER OF PLAYERS
numplayers = raw_input("Enter the number of players:")
print(" ")

#ENTER PLAYER NAMES
for i in numplayers:
    playername[i] = raw_input("Enter player " + i + "name" ")
    print(" ")
    print("Welcome " + playername[i] + "!")
    print(" ")

print("Player order")
for i in numplayers:
    print(i + ": " + playername[i]

print(" ")
print("Game Start")
print(" ")

for i in numplayers:
    for d in numthrows:
        print(playername[i] + ": 1st throw"
	#CALL HIT CHECK









