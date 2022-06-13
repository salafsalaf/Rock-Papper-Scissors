import random

print("Enter \'R\' for Rock")
print("Enter \'P\' for Papper")
print("Enter \'S\' for Scissors")

list1 = ['R', 'P', 'S']
playerScore, cpuScore = 0, 0

def conv(value):
    if(value == 'R'):
        return "Rock"
    elif(value == 'P'):
        return "Papper"
    elif(value == 'S'):
        return "Scissors"

for i in range(3):
    cpu = random.choice(list1)
    player = input("Enter your choice: ")
    
    if(player != 'R' and player != 'P' and player != 'S'):
        print("Incorrect selection!")
        i -= 1
        continue
    
    print("Player (" + conv(player) + ") : CPU (" + conv(cpu) + ")")
    
    if(player == cpu):
        print("Ties!")
    elif((player == 'R' and cpu == 'S') or (player == 'S' and cpu == 'P') or (player == 'P' and cpu == 'R')):
        print("Player Wins!")
        playerScore += 1
    elif((cpu == 'R' and player == 'S') or (cpu == 'S' and player == 'P') or (cpu == 'P' and player == 'R')):
        print("CPU Wins!")
        cpuScore += 1

if(playerScore > cpuScore):
    print("Player Wins The Game!")
elif(cpuScore > playerScore):
    print("CPU Wins The Game!")
else:
    print("The Game Ends In Ties!")