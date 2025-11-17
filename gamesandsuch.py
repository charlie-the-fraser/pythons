import random
games = ["devil may cry 3", "dark souls 2", "elden ring", "persona 3 reload", "borderlands 2", "cyberpunk 2077", "five nights at theo parvins", "resident evil 2"]
played = []
favourited = []
for i in range (0,len(games)):
    favourited.append(random.randint(1,9999))
    played.append(random.randint(1,99999) + favourited[i])
choice = 0
while choice != 4:
    choice = int(input("would you like to mark a game as played (1), mark a game as favourited (2), veiw the most popular games (3), leave (4), list index assignment out of range (5) "))
    if choice == 1:
        game = str(input("what game would you likle to mark as played "))
        for i in range (0, len(games)):
            if games[i] == game:
                played[i] = played[i] + 1
        print("succsessfully logged")
    elif choice == 2:
        game = str(input("what game would you likle to mark as favourited "))
        for i in range (0, len(games)):
            if games[i] == game:
                favourited[i] = favourited[i] + 1
        print("succsessfully logged")
    elif choice == 3:
        maximum = 0
        for i in range(0, len(games)):
            maximum = 0
            for b in range(i, len(games)):
                score = played[b] + (favourited[b] * 2)
                if score > maximum:
                    tempgame = games[b]
                    tempplayed = played[b]
                    tempfavourite = favourited[b]
                    played[b] = played[i]
                    played[i] = tempplayed
                    favourited[b] = favourited[i]
                    favourited[i] = tempfavourite
                    games[b] = games[i]
                    games[i] = tempgame
                    maximum = score
        for i in range(len(games), 0, -1):
            if i != 1:
                print(f"{i} - {games[i - 1]}, played - {played[i - 1]}, favourited - {favourited[i - 1]}")
            else:
                input(f"{i} - {games[i - 1]} played - {played[i - 1]}, favourited - {favourited[i - 1]}")
    elif choice == 4:
        input("bye bye!")
    elif choice == 5:
        games[999] = "list index assignment out of range"
    else:
        input("invalid input ")
        




                    
            
