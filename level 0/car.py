command = ""
started = False
while True:
    command = input("> ")
    if command.lower() == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started ......")
    elif command.lower() == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("to stop the car")
    elif command.lower() == "help":
        print("start - to start the car \n"+
              "stop - to stop the car\n"+
              "quit - to exit"
              )
    elif command.lower() == "quit":
        break
    else:
        print("I don't understand that .....")