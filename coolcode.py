def information():
    global name, weight, age
    name = str(input("what ias the patients name? "))
    age  = int(input("what is the patients age? "))
    weight = float(input("whtat is the patients weight? "))
    importance = str(input("what is the patients favourite colour? "))
    if importance == "blue" or importance == "purple":
        input("good choice")

information()
quiz = float(input("what is the air speed velocity of an unladen swallow? "))

def medication():
    global name, age, weight
    safe = "safe"
    if age < 12 or weight < 40:
        safe = "not safe"
    input(f"the medicine is {safe} for the patient {name}.")

def gym():
    global age, name
    access = "can"
    if age < 18:
        yes = "balls and such"
        while yes != "yes" and yes != "no:":
            yes = str(input(f"does the patient {name} have medical clearence to access the intensive zone? "))
            if yes != "yes" and yes != "no":
                input("invalid input")
        if yes == "no":
            access = "cannot"
    input(f"the patient {name} {access} access the intensive zone.")

def honkshoohonkshoo():
    global name
    sleepytime = "balls and such"
    while sleepytime != "yes" and sleepytime != "no":
        sleepytime = str(input(f"is the patient {name} asleep? "))
        if sleepytime != "yes" and sleepytime != "no":
            input("invaliid input")
    if sleepytime == "yes":
        input("have a good sleep! ")
    elif sleepytime == "no":
        rate = int(input("what is the patients heart rate? "))
        if rate > 100:
            input("ALERT ALERT ALERT")
        else:
            input("should be fine then")

continues = "yes"
while continues == "yes":
    choice =  0
    while choice < 1 or choice > 4:
        choice = int(input("would you like to calculate medication (1), get intensive zone access (2), calculate sleep (3) or change patient data (4)? "))
        if choice < 1 or choice > 4:
            input("invalid input")
    if choice == 1:
        medication()
    elif choice == 2:
        gym()
    elif choice == 3:
        honkshoohonkshoo()
    elif choice == 4:
        information()
    continues = str(input("would you like to continue? "))
