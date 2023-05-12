import random
user_wins=0
comp_wins=0
tie=0
options=["rock","scissors","paper"]
while True:
  user_input=str(input("Enter your options: "))
  if user_input=="q":
    break
  else:
    number=random.randint(0,2)
    comp_input=options[number]
    print("Computer chose: ",comp_input)

    if user_input=="rock" and comp_input=="scissors":
      print("You won!")
      user_wins+=1
    elif user_input=="scissors" and comp_input=="paper":
      print("You won!")
      user_wins+=1
    elif user_input=="paper" and comp_input=="rock":
      print("You won!")
      user_wins+=1
    elif user_input=="rock" and comp_input=="rock":
      print("Tied!")
      tie+=1
    elif user_input=="scissors" and comp_input=="scissors":
      print("Tied!")
      tie+=1
    elif user_input=="paper" and comp_input=="paper":
      print("Tied!")
      tie+=1
    elif user_input=="rock" and comp_input=="paper":
      print("You Loose!")
      comp_wins+=1
    elif user_input=="scissors" and comp_input=="rock":
      print("You Loose!")
      comp_wins+=1
    elif user_input=="paper" and comp_input=="scissors":
      print("You Loose!")
      comp_wins+=1

print("You Won: ",user_wins, "times.")
print("Comp  Won: ",comp_wins, "times.")
print("Tied: ",tie, "times.")
      