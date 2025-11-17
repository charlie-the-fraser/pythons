x = 25
y = 3.14
print(type(x), type(y))

average = 0
a = int(input("how many scores? "))
scores = [0] * a

for i in range (0, a):
    scores[i] = int(input("enter score "))
    average = average + scores[i]

print(average / a)
print(scores)

first = input("enter first name ")
second = input("enter second name ")
name = first + second
length = len(name)
if length >= 20:
    print("screw you and your long ass name ")
    input("enter ")
    print("good boy")
else:
    print(name, length)