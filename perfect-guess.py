import random

rand_no=random.randint(1,100)
userGuess=None
guesses=0

print("========= Welcome! In the Game of Perfect Guess ============")

a=input("Enter your Name :")
print(f"Hello, {a} Lets Start the Game...")


while(userGuess!=rand_no):
    userGuess=int(input("Enter any Number between 1 to 100 :"))
    guesses += 1
    
    if(userGuess==rand_no):
        print("Congrats ! Your Guess is Correct")
    
    else:
        if(userGuess>rand_no):
            print("your Guess is Wrong ! Please Select a Smaller Number.")
        else:
            print("your Guess is Wrong ! Please Select a Greater Number.")


print(f"you guessed the correct number in {guesses} guesses.")
