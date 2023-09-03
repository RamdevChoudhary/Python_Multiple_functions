# write a python program which will keep adding a stream of numbers inputtee by the user. The adding stops as
#  soon as user process q key on the keyboard

sum = 0
while(True):
    userInput = input("Enter the item priceor press q to quit: \n")
    if (userInput!="q"):
        sum = sum + int(userInput)
        print(f"Order total so far: {sum}")
    
    else:
        print(f"You Bill total is {sum} Thanks for shopping with us")
        break