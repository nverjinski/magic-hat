import numpy as np
import random as random

# Functions
def randomOrder(l):
	print("********** RANDOM ORDER **********\n")
	new_order = np.random.choice(l, len(l), replace=False)
	for i in new_order:
		print(i)
	print("\n********** ********** **********")

def randomPick(l):
	print("********** RANDOM PICK **********\n")
	random_integer = random.randint(0, (len(l)-1))
	print( l[random_integer] )
	print("\n********** ********** **********")

def randomPairs(l):
	# If the list isn't even, add "Bye" as an option
	if(len(l) % 2 != 0):
		l.append('Bye')

	randomized_list = np.random.choice(l, len(l), replace=False).tolist()

	print("********** RANDOM PAIRS **********\n")
	for i in range(len(randomized_list) / 2):
		print(randomized_list.pop())
		print(randomized_list.pop() + "\n")
	print("********** ********** **********")


def printOptions():
	print("********** OPTIONS **********\n")
	print("Select an option:")
	print("Press 1 for Random Order")
	print("Press 2 for Random Pick")
	print("Press 3 to create Random Pairs")
	print("Press 4 to Quit\n")
	print("********** ********** **********")

def main():
	print("\n********** The Magic Hat ************")
	print("Place items into the hat and tell me, \nthe Magic Hat, what to do with them!")
	print("**********   **********   **********")
	raw_contents = raw_input("\nWhat goes in the hat? ")
	print("")
	raw_contents = raw_contents.strip()
	contents = raw_contents.split(' ')
	quit = False;

	printOptions()

	while(quit != True):

		selection = raw_input("\nPlease Select an Option: ")
		print("")
	
		if(selection == '1'):
			randomOrder(contents)
		elif(selection == '2'):
			randomPick(contents)
		elif(selection == '3'):
			randomPairs(contents)
		elif(selection == '4'):
			quit = True;


main()