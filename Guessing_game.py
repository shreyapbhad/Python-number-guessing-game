import random
secret = random.randint(1,10)
attempts = 3
while attempts > 0 :
  magical_no=int(input("enter your magical no:"))
  
  if magical_no==secret :
    print("You Won!!")
    break
  else :
    attempts=attempts - 1
    print("wrong no")
  
  if attempts > 0 :
    print("attempts left :",attempts)
  else :
    print("You Lost!! ,the secret is :",secret)
