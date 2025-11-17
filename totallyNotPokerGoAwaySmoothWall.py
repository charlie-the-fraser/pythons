import random
import sys
sys.setrecursionlimit(99999)
suits = ["spades","diamonds","hearts","clubs"]
numbers = ["1","2","3","4","5","6","7","8","9","10","jack","queen","king"] 

numPlayers = int(input("how many players?"))

taken = [0] * (5 + (4 * numPlayers))

def randomtime(numPlayers, numbers, suits):
    i = 0
    taken = []
    cards = []
    while i <= numPlayers * 2 + 7:
        randomnumber = random.randint(0,12)
        randomsuit = random.randint(0,3)
   
        success = True

        for t in range(0, len(taken) - 1):
            if t == 0 or t % 2 == 0:
                if taken[t] == randomnumber and taken[t + 1] == randomsuit:
                    success = False
                  
        if success:
            print(i)
            taken.append(randomnumber)
            taken.append(randomsuit)
            cards.append(numbers[randomnumber] + " of " + suits[randomsuit])    
            
                    
        else:
            i = i - 1
            print(i)
        i = i + 1

    return(cards, taken)
    
cards, taken = randomtime(numPlayers, numbers, suits)
dealer = 0