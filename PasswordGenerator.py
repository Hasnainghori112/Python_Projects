import random
import string

def generate_random_word(length=10):
  characters = string.ascii_letters + string.digits + string.punctuation
  return ''.join(random.choice(characters) for i in range(length))

# Example usage:
random_word = generate_random_word()
print("!.....Paswrod Genrator.....!")

number = int(input("How much password you generate : "))
len = int(input("Enter password length : "))
for i in range(number):
  pasword = ''
  for le in range(len):
    pasword += random.choice(random_word)
  print(pasword)