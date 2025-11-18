lanes = ["available"] * 31

def tryInt(input):
    valid = False
    try:
        int(input)
        valid = True
    except:
        input("invalid input")
    return(valid)
def laneTime():
    global lanes
    deciscion = 0
    available = []
    for i in range(0, len(lanes)):
        if lanes[i] == "available":
            available.append(i + 1)
    print(f"the following names are available: {available}")
    while deciscion <= 0 or deciscion > 31:
        valid = True
        deciscion = input("which lane would you like to book? ")
        try:
            int(deciscion)
        except:
            input("invalid input")
            deciscion = 0
            valid = False
        if valid:
            deciscion = int(deciscion)
            if deciscion > 31 or deciscion <= 0:
                input("you have entered a lane outside the valid range")
            elif lanes[deciscion - 1] != "available":
                input("this lane is already taken")
                lists = str(input("input 'yes' if you would like a list of available lanes "))
                if lists == "yes":
                        print(f"the following names are available: {available}")
            else:
                input("this lane is available! procceeding to pricing")
                lanes[deciscion - 1] = "taken"
    return deciscion

def pricing():
    valid = False
    price = 0
    while not valid:
        party = input("how many people are in your group? ")
        try:
            int(party)
            valid = True
        except:
            Valid = False
            input("invalid input")
        if valid:
            party = int(party)
            if party <= 0 or party > 8:
                valid = False
                input("party size outside valid range (1 - 8)")
    party = int(party)
    ages = []
    valid = False
    while not valid:
        games = input("how many games would you like to play (maximum of 3) ")
        try:
            int(games)
            valid = True
            games = int(games)
        except:
            input("invalid input ")
        if valid:
            if games < 1 or games > 3:
                valid = False
                input("number of games must be between 1 and 3")
    for i in range(1, party):
        valid = False
        while not valid:
            age = input(f"what is the age of guest no.{i}")
            try:
                int(age)
                valid = True
            except:
                input("invalid input")
                valid = False
            if valid: 
                age = int(age)
                if age < 0:
                    valid = False
                    input("invalid age")
                else:
                    if age < 16:
                        ages.append("junior")
                        price = price + 6.20 * games
                    else:
                        ages.append("senior")
                        price = price + 7.20 * games
    input(f"thank you for booking, your total is {price}")
    return(price)

pricing()