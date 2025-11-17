import random

def rectangle():
    length = float(input("what isthe length of the rectangle? "))
    width = float(input("what is the width of the rectangle? "))
    area = length * width
    perimiter = (width * 2) + (length * 2)
    print(f"the area of the rectangle is {area} and the perimiter of the rectangle is {perimiter}")

def timeTime():
    conversion = 0
    while conversion != 1 and conversion != 2:
        conversion = int(input("would you like to convert minutes to hours (1) or hours to minutes (2) "))
        if conversion != 1 and conversion != 2:
            input("invalid input ")
    if conversion == 1:
        number = int(input("how many minutes do you have? "))
        hours = number // 60
        print(f"you have {hours} hours")
    elif conversion == 2:
        number = float(input("how many hours and minutes do you have (eg. 3 hours and 45 minutes = 3.45) "))
        boat = (number % 1) * 100
        floats = (number // 1) * 60
        whatever = int(floats + boat)
        print(f"you have {whatever} minutes")

def hopital():
    plan = "False"
    name = input("what is the patients name? ")
    age = int(input("what is the patients age? "))
    bill = float(input("what is the patients bill? "))
    superBill = bill + (bill * 0.2)
    if age < 18:
        input("age discount has been applied ")
        superBill = superBill * 0.95
    if superBill >= 1000:
        input("not looking good for you buddy")
        plan = str(input("would you like to use a 12 month payement plan (T) or not (F) "))
    if plan == "T":
        print(f"the monthly payement is £{superBill / 12}")
    else:
        print(f"the bill is £{superBill}")

def loopTime():
    password = random.randint(1,9999)
    true = False
    if password < 10:
        string =  "000" + password
    elif password < 100:
        string = "00" + password
    elif password < 1000:
        string = "0" + password
    else:
        string =  str(password)
    while not true:
        guess = int(input("ENTER 4 DIGIT PIN: "))
        if guess == password:
            input("password is correct")
            true = True
        else:
            response = random.randint(1,5)
            if response == 1:
                input("sorry, thats wrong :( ")
            if response == 2:
                input("you can do it! ")
            if response == 3:
                input("getting warmer (probably) ")
            if response == 4:
                input("your a dissapointment. ")
            if response == 5:
                input("what kinda flipping guess was that idiot ")
            helptime = random.randint(1,100)
            if helptime == 100:
                choice = str(input("wound you like a hint? (input T if yes) "))
                if choice == "T":
                    hint = random.randint(1,4)
                    print(f"digit no.{hint} of the password is {string[hint - 1]}")

def hopitL2():
    running = True
    while running == True:
        descisions = int(input("would you like to add patient details (1), calculate BMI (2), check medicine dosage (3) "))
        if descisions == 1:
            input("important patient details stuff ")
        if descisions == 2:
            input("important BMI stuff ")
        if descisions == 3:
            input("important dosage stuff ")
        running = bool(input("would you like to continue (True) or not (False) "))

loopTime()  