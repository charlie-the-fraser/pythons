machines = {"pinball wizard":{"category" : "pinball", "status" : "working"}, "dance floor X" : {"category" : "rhythm", "status" : "working"}, "retro racing" : {"category" : "racing", "status" : "needs service"}, "alien blaster" : {"category" : "shooter", "status" : "working"}}
choice = "0"
while choice != "7":
    choice = str(input("would you like to veiw all machines (1), add a new machine (2), update a machines status (3), delete a machine entery (4), list index assignment out of range (5), find all games of a category (6) end program (7) "))
    if choice == "1":
        print(machines)
    elif choice == "2":
        name = str(input("what is the name of the machine? "))
        category = str(input("what is the machine's category? "))
        status = str(input("what is the status is the machine? "))
        machines[name] = {"category" : category, "status" : status}
    elif choice == "3":
        name = str(input("which machine would you like to update? "))
        if name in machines.keys():
            status = str(input(f"what is the status off {name}? "))
            machines[name]["status"] = status
        else:
            input("machine is not found")
    elif choice == "4":
        name = str(input("which machine would you like to remove? "))
        if name in machines.keys():
            del(machines[name])
            input(f"{name} succesfully removed")
        else:
            input(f"{name} could not be found")
    elif choice == "5":
        balls = [0]
        balls[67] = "theo parvin"
    elif choice == "6":
        found = 0
        category  = str(input("which category do you want? "))
        for i in range(0, len(machines)):
            machineName = list(machines.keys())[i]
            if machines[machineName]["category"] == category:
                input(machineName)
                found = 1
        if found == 0:
            input("no machines of this category where found")
    elif choice == "7":
        input("good bye!")
    else:
        input("invalid input ")