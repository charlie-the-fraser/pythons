wingdings = list("✌🖏👍👎☜☞☝☟🖐☺😐☹💣🕱🏳🏱✈☼🌢❄🕆✞🕈✠✡☪🗁🗎🗏🗐🗄⌛🖮🖰🖲🗀🖉✂🞈👓🕭♈🕮♋🔾🞐🖴🖂🕿✆📫♉🖬🖃☯🏵☸🙶✁🙷🕯🖎🖴 🖳📪🕮⚫⧫🖴📬🕮♑⧫🖴 📭✍🕉🏶")
normal = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!" + "£$%^&*()-_=+[{]}#~'@;:,<.> /?\|")
valid = False

def ToWing(text):
    global wingdings, normal
    for i in range(0, len(text)):
        for b in range(0, len(normal) - 1):
            if text[i] == normal[b]:
                text[i] = wingdings[b]
    string = "" 
    for i in range(0, len(text)):
        string = string + text[i]
    return string
def toNotDing(text):
    global wingdings, normal
    for i in range(0, len(text)):
        for b in range(0, len(normal) - 1):
            if text[i] == wingdings[b]: 
                text[i] = normal[b]
    string = ""
    for i in range(0, len(text)):
        string = string + text[i]
    return string
while not valid:
    MakeYourChoice = str(input("would you like to convert to (1) or from (2) wingdings "))
    try:
        int(MakeYourChoice)
    except:
        valid = False
    else:
        valid = True
        MakeYourChoice = int(MakeYourChoice)
        if MakeYourChoice != 1 and MakeYourChoice != 2:
            valid = False
    if not valid:
        print("invalid input") 
    else:
        text = str(input("what would you like to translate? "))
        text = list(text.upper())
        if MakeYourChoice == 1:
            text = ToWing(text)
        elif MakeYourChoice == 2:
            text = str(toNotDing(text))
        input(text)



