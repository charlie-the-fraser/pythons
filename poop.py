import random
hello = 0
goodbye = 0
print("hello world!")
print("goodbye world😈")
test = int(input("give me your data "))
for i in range(99999):
    funny = random.randint(1,100)
    if funny == 100:
        print("hello world")
        hello = hello + 1
        print(hello)
    elif funny == 1:
        print("goodbye world😈")
        goodbye = goodbye + 1
        print(goodbye)
        if goodbye % 100 == 0:
            for t in range(random.randint(1,i)):
                 print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
                 print(t)

    print(i * test)
float = 9.67
boolean = True
string = str(boolean)
print(boolean,float,string)

