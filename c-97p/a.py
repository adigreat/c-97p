import random
random=random.randint("12345678910")
guess =""
guess_count=0
guess_limit=5
out_of_guess=False
while guess != random and not(out_of_guess) : 
    if guess_count < guess_limit:
     guess  = int("enter guess:")
     guess_count +=1
    else:
     out_of_guess = True

if out_of_guess:
    print(out_of_guess)
else:
    print("you win")



