def evilTheo():
    input("It has been 6, maybe 7 months since that day (press enter to continue)")
    input("They put you in the penar explosion chamber")
    input("You were too strong however, and regenerated")
    input("but you were incomplete")
    input("imperfect")
    input("your left nut was imperfect")
    input("you must find the perfect left nut and become whole")

def checkInt(num):
    try:
        int(num)
    except:
        input("input must be a int")
        valid = False
    else:
        num = int(num)
        valid = True
    return(num, valid)
valid = False
while not valid
    path = str(input("would you like to play as Theo (1), or Evil Theo (2) "))
    path, valid = def(path)
    if valid:
        if path == 1:
            print("theo time")
        elif path == 2:
            print("evil theo time")