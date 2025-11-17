def measurement():
    normal = True
    temp = float(input("what is your temperature? "))
    oxygen = float(input("what is your oxygen level? "))
    heart = int(input("what is your heartrate? "))
    if temp > 37.5:
        print("your temperatue is high")
        normal = False
    if oxygen < 92:
        print("your oxygen is low")
        normal = False
    if heart <= 60 or heart >= 100:
        print("your heartrate is abnormal")
        normal = False
    if normal:
        print("everything is normal")
 

def yes():
    max = 0
    steps = [0] * 7
    days = ["monday", "tuesday", "wedensday", "thursday", "friday", "saturday", "sunday"]
    yesterday = 0
    day = 0
    for i in range(0,7):
        today = int(input("how many steps did you do today? "))
        steps[i] = today
        if day == 0:
            input("great start!")
            day = 1
            max = today
            maxday = 0
        else:
            if today >= yesterday:
                input("well done! ")
            else:
                input("you can do it tommorrow! ")
            if today > max:
                input("that was your best this week!")
                max = today
                maxday = i
        yesterday = today
    for i in range(0,7):
        input(f"on {days[i]} you walked {steps[i]} steps ")
    input(f"your best day was {days[maxday]} where you walked {steps[maxday]}")

yes()
