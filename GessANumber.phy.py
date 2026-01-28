import random

num=random.randint(1,20)


while True:

       guess=int(input("guess A Number Between 1 to 20 : "))
       if guess==num:
           print("you Guessed A Correct Number")
           break
       elif guess>num:
            print("you Guessed A Greater Number")
       elif guess<num:
            print("you Guessed A Smaller Number")
            
