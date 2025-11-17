conv = input("do you want to convert to celcius (c) or farenheight (f)? ")
while conv != "c" and conv != "f":
    conv = input("c or f motherflipper ")
temp = float(input("enter temp "))
if conv == "f":
    temp = temp * (9 / 5) + 32
elif conv == "c":
    temp = (temp - 32) * (5/9)
print(f"the temperature is {temp}° {conv}")