import random
def play():
  try:
    user = (input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissor\n"))
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
      print("It's a tie")
    elif (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
      print("You won!")
    else:
      print("You lost!")
  except Exception as e:
      print(e)
play()