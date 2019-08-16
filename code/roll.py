import random
import sys

def roll(min, max):
  return random.randint(min, max)


def play_round():
  result = roll(1, 6)
  
  print("You got " + str(result))
  if result == 6:
    print("Nice!")
  if result == 1:
    print("not good...")


play = True
while play:
  play_round()

  answer = input("Roll again? y/n: ")
  if (answer != "y"):
    play = False

print("Bye!")
