def arithmetic():
    steps = 7345
    goal = 10000
    percent_of_goal = (steps / goal) * 100
    if goal >= steps:
        remaining_steps = goal - steps
        end = "remaining"
    else:
        remaining_steps = "goal completed"
        end = ""
    print(f"{percent_of_goal}% done, {remaining_steps} {end}")

def bmicalc():
    weight = int(input("enter weight in Kg "))
    height = int(input("enter height in M "))
    bmi = weight // (height ** 2)
    if bmi <= 18.5:
        state = "underweight"
    elif bmi > 18.5 and bmi <= 25:
        state = "healthy"
    elif bmi > 25 and bmi <= 30:
        state = "overweight"
    elif bmi > 30:
        state = "obese"
    print(f"you are {state}")

def screen():
    steps = int(input("how many steps? "))
    daily_screen_minutes = int(input("how many daily screen minutes? "))
    night_screen_minutes = int(input("enter night screen minutes"))
    Warning = night_screen_minutes > 60 or (daily_screen_minutes > 240 and steps < 5000)
    print(Warning)

def hydration():
    water = int(input("how much water in ml have you drank? "))
    points = water // 250
    bonus = (water // 2000) * 5 
    points = points + bonus
    print(points)
    return points, water
    

def freeclass():
    age = int(input("enter age "))
    registered = "balls"
    while registered != "yes" and registered != "no":
        registered = str(input("are you a a registered low-income participant "))
        if registered != "yes" and registered != "no":
            print("invalid input")
    days_since_last = int(input("how many days since last free class? "))
    eligable = (((age >= 16 and age <= 25) or registered == "yes") and days_since_last > 30)
    print(eligable)

def reward():
    steps = int(input("how many steps? "))
    water = int(input("how much water(ml) "))
    points = (steps // 1000) * 2 + (water // 500)
    if points > 40:
        teir = "gold"
    elif points >= 20:
        teir = "silver"
    else:
        teir = "bronze"
    print(teir)

def mathsYAYYYYYYYYY():
    total_minutes = int(input("HOW MANY MINUTES IN TOTAL? "))
    sessions = int(input("how many sessions? "))
    if sessions == 0:
        average = 0
    else:
        average = total_minutes / sessions 
        round(average, 1)
    print(average)

def integration():
    points, water = hydration()    
    steps = int(input("how many steps? "))
    screen = int(input("how many minutes of screen time "))
    goal = 10000
    percent = (steps / goal) * 100
    if screen <= 240:
        ok = "ok"
    else:
        ok = "high"
    print(f"steps: {steps} ({percent}%), water: {water} (+{points} pts), screen: {screen} mins - {ok}")


