Command  = ""
started = False
while True:
    Command = input(">").upper()
    if Command == 'HELP':
        print('start - to start the car')
        print('stop - to Stop the car')
        print('quit - to exit')
    elif Command.upper() == 'START':
        if started:
            print("Already Started")
        else:
            started = True
            print("Car Started Ready To Go!")

    elif Command.upper() == 'STOP':
        if not started:
            print("Already Stopped")
        else:
            started = False
            print("Car Stopped!")
    elif Command.upper() =='QUIT':
            break
    else:
        print("Please enter valid cmd")


