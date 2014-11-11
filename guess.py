import random

#Create a flag that keeps track of number of guesses
guessToken = 0
#Taking user information
print "Hello, what is your name?"
myName = raw_input()
#Displaying the message to player
print "Hello, "+myName+", I am thinking a number between 1 and 20"
myNum = random.randint(1, 20)

#Game logic
while guessToken < 6:
  print "Take a guess"
  curr_num = int(raw_input())
  if curr_num > myNum:
    print "Number too high"
  if curr_num < myNum:
    print "Number too low"
  if curr_num == myNum:
    print "Right! Congrats!"
    break
  guessToken += 1

print "You took", guessToken+1, "guesses"


