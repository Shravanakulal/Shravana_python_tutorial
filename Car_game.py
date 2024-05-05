cmd=""
started=False
stopped=False
while(True):
    cmd= input("> ").lower()
    if cmd=='help':
        print("""
start-to start the car 
stop-to stop the car
quit-to exit
          """)
    elif cmd=='start':
        if started:
            print("car already started")
        else:
            started=True
            print('car started...Ready To Go!!')
    elif cmd=='stop':
        if stopped:
            print("car already stopped")
        else:
            stopped=True
            print('car Stopped!!')
    elif cmd=='quit':
        break
    else:
        print('sorry!I Dont Understand that')

