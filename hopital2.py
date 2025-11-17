total_patients = 0
name = []
age = [] 
def add_patient():
    global total_patients, name, age
    total_patients += 1
    name = name + [0]
    age = age + [0]
    name[total_patients - 1] = input("Enter name: ")
    age[total_patients - 1] = int(input("Enter age: "))
    print("Patient added:", name[total_patients - 1], "," , age[total_patients - 1])

def view_total():
    global total_patients, name, age
    input(f"Total patients: {total_patients}")
    for i in range(0, total_patients):
        input(f"the patients name is {name[i]} and the age is {age[i]}")

def iDoNotHateChildren():
    global total_patients, name, age
    name = []
    age = []
    total_patients = 0
    print("patients have been succsesfully erased")

def screwThisGuyInParticular():
    found = 0
    global total_patients, name, age
    temp = input("enter name of patient to be remove: ")
    for i in range(0, total_patients):
        if name[i] == temp:
            num = i
            found = 1
    if found == 1:
        name[num] = 0
        age[num] = 0
        total_patients = total_patients - 1
        input("data succsessfully eraced")
        for n in range(num,total_patients):
            name[n] = name[n + 1]
            age[n] = age[n + 1]
    else:
        input("could not find patient you are looking for")

choice = 1
while choice >= 1 and choice <= 4:
    choice = int(input("would you like to register a patient (1), view patients, (2) or reset patient data (3), remove a patient (4) or leave (5) "))
    if choice < 1 and choice > 4:
        input("invalid selection")
    elif choice == 1:
        add_patient()
    elif choice == 2:
        view_total()
    elif choice == 3:
        iDoNotHateChildren()
    elif choice == 4:
        screwThisGuyInParticular()
    elif choice == 5:
        input("goodbye!")


