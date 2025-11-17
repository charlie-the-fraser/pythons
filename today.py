def conversion():
    CONVERSION = 18
    number = int(input("how many units? "))
    choice = 0
    while choice != 1 and choice != 2:
        choice = int(input("would you like to convert to mg/dL from mmol/L (1) or to mmol/l from mg/dL (2) "))
        if choice != 1 and choice != 2:
            input("invalid input")
    if choice == 1:
        answer = number * CONVERSION
        print(f"you have {answer}mg/dL")
    elif choice == 2:
        answer = number / CONVERSION
        print(f"you have {answer}mmol/L")

def fever():
    MAX = 38
    heat = 0
    measurements = int(input("how many temperatures would you like to record? "))
    for i in range(0, measurements):
        temp = 1
        while temp < 30 or temp > 45:
            temp =  int(input(f"input temperature no.{i + 1} "))
            if temp < 30 or temp > 45:
                input("impossible value detected, temps must be between 30 and 45")
        heat = heat + temp
     
    average = heat / measurements
    if average >= MAX:
        input("WARNING! fever threshhold has been passed (enter to continue)")
        print(f"the average temperature is {average}°c which is {average - MAX}°c over the fever threshhold.")
    else:
        print(f"the average is {average}°c which is {MAX - average}°c bellow the fever threshhold")
    
def heartbeat():
    CONSTANT = 220
    patients = int(input("how many patients would you like to test "))
    for i in range(0,patients):
            age = int(input(f"what is the patient no.{i + 1} age? "))
            maximum = CONSTANT - age
            rate = int(input(f"what is the patient no.{i + 1} resting heart rate? "))
            if rate == 0:
                input("the patient has flatlined")
            elif rate < 60:
                input("the patient's heart rate is low")
            elif rate < 100:
                input("the patient has a good resting heart rate")
            elif rate >= maximum:
                input("WARNING! patient is above the safe maximum heart rate")
            else:
                input("the patient's heart rate is high")
  
def mmmmWater():
    GOAL = 3.7
    intake = int(input("what is todays water intake (L) "))
    if intake >= GOAL:
        input("goal has been met, well done!")
    else:
        input(f"the goal was not met. {GOAL - intake}L more is needed to meet the goal")

running = True
while running:
    task = 0
    while task < 1 or task > 4:
        task = int(input("would you like to see task 1, task 2, task 3, or task 4 "))
        if task < 1 or task > 4:
            input("enter a valid task number")
    if task == 1:
        conversion()
    elif task == 2:
        fever()
    elif task == 3:
        heartbeat()
    elif task == 4:
        mmmmWater()
    
    continues = "b"
    while continues != "F" and continues != "T":
          continues = str(input("would you like to see another task (T) or not (F)? "))
          if continues != "F" and continues != "T":
              input("invalid input ")
    
    if continues == "F":
        running = False
    elif continues == "T":
        running = True

input("goodbye!")
