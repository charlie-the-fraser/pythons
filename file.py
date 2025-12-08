import random
scores = {}
people = 0
total = 0
def checkint(number):
    try:
        int(number)
    except:
        input("you have not input an intiger")
    else:
        valid = True
        number = int(number)
    return number, valid
with open("scores.txt", "a") as file:
    name = str(input("enter player name: "))
    valid = False
    while not valid:
        score = str(input("enter score: "))
        score, valid = checkint(score)
    scores[name] = score
    total = total + score
    people = people + 1
    average = total / scores
    print(scores) 

            