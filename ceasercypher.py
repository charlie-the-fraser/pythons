alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1",  "2", "3", "4", "5", "6", "7", "8", "9"]
message = str(input("enter message you would like to encrypt or decrypt: "))
valid = False
while not valid:    
    process = str(input("do you want to encrypt (1), or decrypt (2) or check all decryption possibilities (3) "))
    if process != "1" and process != "2" and process !="3":
        input("you have not entered a valid choice")
    else:
        valid = True
valid = False
while not valid and process != "3":
    cypher = str(input("enter encryption key: "))
    try:
        int(cypher)
    except:
        valid = False
    else:
        valid = True
        cypher = int(cypher)
    if valid:
        if cypher > 26 or cypher < 1:
            valid = False
    if not valid:
        input("you did not enter a valid key (int between 1 - 26)")
message = list(message.lower())
encryptedMessage = ""
if process == "1":
    for i in range(0, len(message)):
        currentLetter = message[i]
        encryptedLetter = message[i]
        try:
            int(currentLetter)
        except:
            for b in range(0, len(alphabet)):
                if currentLetter == alphabet[b]:
                    position = b
                    if position + cypher > 25:
                        encryptedLetter = alphabet[position + cypher - 26]
                    else:
                        encryptedLetter = alphabet[position + cypher]
                currentLetter = message[i]
            encryptedMessage = encryptedMessage + encryptedLetter 
        else:
            for b in range(0, len(numbers)):
                if currentLetter == numbers[b]:
                    position = b
                    cypher = cypher % 10
                    if position + cypher > 9:
                        encryptedLetter = numbers[position + cypher - 10]
                    else:
                        encryptedLetter = numbers[position + cypher]
                currentLetter = message[i]
            encryptedMessage = encryptedMessage + encryptedLetter 
    print(encryptedMessage)

elif process == "2":
    for i in range(0, len(message)):
        currentLetter = message[i]
        encryptedLetter = message[i]
        try:
            int(currentLetter)
        except:
            for b in range(0, len(alphabet)):
                if currentLetter == alphabet[b]:
                    position = b
                    if position - cypher < 0:
                        encryptedLetter = alphabet[position - cypher + 26]
                    else:
                        encryptedLetter = alphabet[position - cypher]
                currentLetter = message[i]
            encryptedMessage = encryptedMessage + encryptedLetter 
        else:
            for b in range(0, len(numbers)):
                if currentLetter == numbers[b]:
                    position = b
                    cypher = cypher % 10
                    if position - cypher < 0:
                        encryptedLetter = numbers[position - cypher + 10]
                    else:
                        encryptedLetter = numbers[position - cypher]
                currentLetter = message[i]
            encryptedMessage = encryptedMessage + encryptedLetter 
    print(encryptedMessage)
elif process == "3":

    for count in range(1, 26):
        encryptedMessage = ""
        for i in range(0, len(message)):
            cypher = count
            currentLetter = message[i]
            encryptedLetter = message[i]
            try:
                int(currentLetter)
            except:
                for b in range(0, len(alphabet)):
                    if currentLetter == alphabet[b]:
                        position = b
                        if position - cypher < 0:
                            encryptedLetter = alphabet[position - cypher + 26]
                        else:
                            encryptedLetter = alphabet[position - cypher]
                    currentLetter = message[i]
                encryptedMessage = encryptedMessage + encryptedLetter 
            else:
                for b in range(0, len(numbers)):
                    if currentLetter == numbers[b]:
                        position = b
                        cypher = cypher % 10
                        if position - cypher < 0:
                            encryptedLetter = numbers[position - cypher + 10]
                        else:
                            encryptedLetter = numbers[position - cypher]
                    currentLetter = message[i]
                encryptedMessage = encryptedMessage + encryptedLetter 
        print(str(count) + ": " + encryptedMessage)
        print("########################")

else:
    input("you have not entered a valid choice")

