num = int(input("enter number "))
if num >= 1 and num <= 100:
    print("correct")
else:
    print("incorrect")

txt = f"the price is {70 * num} pounds"
print(txt)

name = input("what is your name? ")
age = int(input("what is your age? "))
score = float(input("what did ypou score? "))
if score > 50:
    passed = True
else:
    passed = False
answer = f"it is {passed} that you passed the exam, score is {score}"
print(answer)