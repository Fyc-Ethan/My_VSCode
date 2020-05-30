#Card game
command = ""
start = 0
stop = 0
while True: #lower() become the lower character
    command = input(">>> ").lower() #we don't need always to call the function
    if command == "start" and start == 0:
        start = 1
        print("Car start...")
    elif command == "start" and start == 1:
        print("what are you doing ? the car is already started")
    elif command == "stop" and stop == 0:
        stop = 1
        print("Car stopper")
    elif command == "stop" and stop == 1:
        print("what are you doing ? the car is stopped")
    elif command == "help": #""" is multi-line output
        print("""           
    start - to start the car
    stop  - to stop the car
    quit  - to quit        
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that!")







