def calories():
    chlorine = int(input("how many calories did you burn per minute? "))
    timeTimeTime = int(input("how many minutes were you working out for? "))
    burn = chlorine * timeTimeTime
    print(f"you burned {burn} calories")

# Hello, this is Parvin, Theo here :) I am here to tell you that you need to improve your fnction names or else!!!!

def steps():
    steeps = int(input("how many steps did you walk? "))
    kilometres = steeps // 1300
    print(f"you walked {kilometres} km")

def timetimetimetimetimetimetimeahhhhhhhhhhhhh():
    minutes = int(input("how many minutes until your next medication? "))
    hours = minutes // 60
    mins = minutes % 60
    print(f"you have {hours} hours and {mins} until your next medication")

def mmmyummytablets():
    tanlets = int(input("how many tablets do you have? "))
    people = int(input("how many people do you have to distribute too? "))
    dose = int(input("what is the dosage in no. of tablets? "))
    leftover = tanlets % (people * dose)
    print(f"you have {leftover} tablets leftover")


continues = True
while continues == True:
    option = 0
    while option < 1 or option > 5:
        option = int(input("would you like to use the calorie calculator (1), steps to kilometres calculator (2), time calculator (3), tablet calculator (4) or the suprise (5) "))
        if option < 1 or option > 5:
            input("invalid input")
    if option == 1:
        calories()
    if option == 2:
        steps()
    if option == 3:
        timetimetimetimetimetimetimeahhhhhhhhhhhhh()
    if option == 4:
        mmmyummytablets()
    if option == 5:
        print("to be continued")
        
# 100/10