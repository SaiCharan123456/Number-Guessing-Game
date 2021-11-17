import random; 

number=random.choice([1,2,3,4,5,6,7,8,9])
print("Number Guessing Game")
print("Guess a Number (between 1 and 9) :")
guess=int(input("Enter your Guess :- "))
chance=0
while (chance < 5) :
     chance = chance + 1  
     break
else:
    print("YOU LOSE !!! The Number is :-",number )

while guess < number:
    print("The Guess is Too Low :- Guess a number higher than ",guess)
    guess=int(input("Enter your Guess :- "))
    break
else :
    print("The Guess is Too High :- Guess a number lesser than ",guess)
    guess=int(input("Enter your Guess :- "))    
if guess == number :
    print(" Congratulation YOU WON !!! ")
    
     
