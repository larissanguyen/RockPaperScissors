import random

#compares the user and computer's moves
def compareMoves (a, b):
	#print "User move = %d" % a 
	#print "Comp move = %d" % b 
	if a == b:
		#print "IN A TIE"
		return 0
	elif a == 0: #rock
		if b == 1: #rock v. paper
			return -1 #loss
		elif b == 2: #rock v. scissors
			return 1
		else:
			return 10 #error
	elif a == 1: #paper
		if b == 0: #paper v. rock
			return 1 #win
		elif b == 2: #paper v. scissors
			return -1 #loss
		else:
			return 10
	elif a == 2: #scissors
		if b == 0: #scissors v. rock
			return -1 #loss
		elif b == 1: #scissors v. paper
			return 1 #win
		else:
			return 10
	else:
		return 10

#start the game and ask if the user wants to play
print "Hi! Welcome to this rock, paper, scissors game."
play = raw_input("Wanna play? y/n: ")
while play.lower() != "y" and play.lower() != "n" and play.lower() != "yes" and play.lower() != "no":
		play = raw_input("Sorry, I missed that. Wanna play? y/n?: ")

#variables that store the values
wins = 0
losses = 0
ties = 0

#the actual game
while play == "y":
	move = raw_input("Rock, paper, scissors, shoot!: ") #ask for user's move
	while move != "rock" and move != "paper" and move != "scissors": #checks for valid user input
		move = raw_input("What do you choose? Type 'rock', 'paper' or 'scissors' please!: ")
	
	compMove = random.randint(0,2) #randomly select a move
	randToWord = { #dictionary that maps the random value to a string, the computer's move
		0: "rock",
		1: "paper",
		2: "scissors"
	}
	compMoveStr = randToWord.get(compMove, "Oops")

	moveToInt = { #dictionary that maps the user input to a value 
		"rock": 0,
		"paper": 1,
		"scissors": 2
	}
	moveInt = moveToInt.get(move, 10)

	#get game results
	result = compareMoves(moveInt, compMove)
	if result == 1:
		wins += 1
		print "%s vs. %s. You Won!" % (move, compMoveStr)
	elif result == 0:
		ties += 1
		print "%s vs. %s. A tie." % (move, compMoveStr)
	elif result == -1:
		losses += 1
		print "%s vs. %s. Sorry! You lost." % (move, compMoveStr)
	else:
		#print "Result= %d" % result
		print "Oops. Something went wrong. Let's start over"
	print "w: %d l: %d t: %d" % (wins, losses, ties)

	#Ask the user if they want to play again
	play = raw_input("Want to play again?: ")
	while play.lower() != "y" and play.lower() != "n" and play.lower() != "yes" and play.lower() != "no":
		play = raw_input("Sorry, I missed that. Wanna play? y/n?: ")

print "Bye!"

