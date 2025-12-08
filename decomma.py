hello = list(str(input("what would you like to remove the commas from? ")))
newstring = ""
for i in range(0, len(hello)):
    if hello[i] != ",":
        newstring = newstring + hello[i]
print(newstring)
