i =1
while(i<=3):
    Secret= int(input('Guess:'))
    i+=1
    if(Secret==9):
        print("you won!")
        break
else:
    print("Sorry,you failed!")