

def changingVariables():        
    patientName = str(input("enter patient name? "))
    height = float(input("enter height in m "))
    return height, patientName
dateOfBirth = str(input("what is the patients date of birth (dd/mm/yyyy) "))
height, patientName = changingVariables()
end = False
while not end:
    print("date of birth is ",dateOfBirth," name is ",patientName, "height is",height)
    end = bool("is patient data True or False?")
    if not end:
        changingVariables()

def BMIcalculator(height):
    weight = float(input("what is the patients weight in killograms? "))
    bmi = weight / (height * height)
    if bmi <= 18.5:
        catagory = "underweight"
    elif bmi <= 24.9:
        catagory = "healthy weight"
    elif bmi <= 29.9:
        catagory = "overweight"
    elif bmi <= 39.9:
        catagory = "obese"
    elif bmi >= 40:
        catagory = "morbidly obese"
    return bmi, catagory

end2 = False
while end2 == False:
    bmi, category = BMIcalculator(height)
    print(f"BMI is {bmi} and the patient is {category}")
    end2 = bool(input("is patient data true or false? "))

maximum = int(input("enter maximum dosage"))
dosage = int(input("enter patient dosedge"))
if dosage >= maximum:
    print("stop taking medicine ") 
else:
    print("should be fine")
country = input("are you english or american? ")
if country == "american":
    price = "$999999999999999999999999999999999999999999999999999999999999999999999999999999999999 + $2 VAT and your left kidney"
elif country == "english":
    price = "free"
print(f"the price is {price}")





