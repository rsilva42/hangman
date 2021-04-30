import random

#initiate the word bank and run the user interface
def main():
	word_bank = init_default_words()

	main_menu(word_bank)
	print("Thanks for playing!")

def init_default_words():
	'''usage: init_default_words()

	initiate a default set of words containing five categories with ten words each'''

	return {	"fruits"	: ["mango", "pineapple", "pitaya", "papaya", "banana",
								"apple", "pear", "lemon", "cantaloupe", "watermelon"],
				"meats"		: ["beef", "pork", "chicken", "lamb", "venison",
								"fish", "lobster", "goat", "turkey", "crab"],
				"cheeses"	: ["gruyere", "mozzarella", "cheddar", "ricotta", "swiss",
								"provolone", "manchego", "parmesan", "muenster", "oaxaca"],
				"vegetables": ["corn", "onion", "broccoli", "carrot", "zucchini",
								"potato", "eggplant", "bean", "turnip", "cabbage"],
				"pastries"	: ["croissant", "strudel", "cake", "madeleine", "cookie",
								"macaron", "cupcake", "brownie", "flan", "tart"]}

def main_menu(word_bank={}):
	'''usage: main_menu(word_bank={})

	sets up a user interface, giving the options:
		"play": to play the game
		"add": to add a category or a word to the word bank
		"exit": to exit the input loop

	if no word bank is supplied an empty word bank will be initialized'''

	#infinite loop until user inputs 'exit'
	while True:
		user_input = input("What would you like to do?\nOptions are: 'play', 'add', and 'exit'\n").lower()

		try:
			if user_input == "play":
				select_category(word_bank)
			elif user_input == "add":
				bank_add(word_bank)
			elif user_input == "exit":
				break
			else:
				print("Invalid option...")
		except Exception as error:
			print(error)

def select_category(word_bank):
	'''usage: select_category(word_bank)

	selects a category and runs the hangman game

	when selecting a category the user is also given the options:
		"random": to let the program choose a random category
		"list": to list the categories in the current word bank'''

	while True:
		user_input = input("Insert a category.\nYou may also try 'random' for a random category and 'list' for a list of the categories in the word bank\n").lower()

		#respond to user input accordingly
		#if input is list then print the categories and loop back
		if user_input == "list":
			print("The current bank contains:")
			for category in list(word_bank.keys()):
				print(category)
			continue
		#else fill category variable for the game to use
		elif user_input == "random":
			category = random.choice(list(word_bank.keys()))
		elif user_input not in list(word_bank.keys()):
			print("Category not found, try again...")
			continue
		else:
			category = user_input
		print("The category is {}".format(category))

		#select a random word from the category
		word = random.choice(word_bank[category])

		hangman_guess(word)

		#allow the player to try again or exit
		user_input = input("Try again? yes/no").lower
		if user_input == "yes":
			break

def hangman_guess(word, lives=10):
	'''usage: hangman_guess(lives=10, word)

	will allow the user 'lives' amount of wrong guesses to complete the word one letter at a time.
	upon completion print a congratulations and exit'''

	#create a set of blanks for the letters guessed right
	blanks = [ "_" for i in range(len(word)) ]
	letters_used = ""

	while lives:
		guess = input("Guess a letter\n").lower()

		#check if only one letter was input
		if len(guess) != 1:
			print("Only one letter at a time please!")
		#check if the letter has been guessed already
		elif guess in letters_used:
				print("You already guessed that character!")
		else:
			if guess in word:

				#scan for letter guessed in word and replace them in the display
				for i in range(len(word)):
					if word[i] in guess:
						blanks[i] = word[i]

				print("Correct!")
				display_blanks(blanks)
			else:
				lives -= 1
				print("wrong, lives left: {}".format(lives))

			letters_used += (guess)

			#if no blanks are left the game is won
			if not '_' in blanks:
				print("CONGRATULATIONS!\nYOU WIN!")
				return

	#if the loop is broken, lives hit 0
	print("you ran out of lives!")

def display_blanks(blanks):
	for char in blanks:
		print(char, end=' ')
	print('')

def bank_add(word_bank):
	print("add invoked")
	user_input = input("What would you like to add?\nOptions are: 'category' and 'word'\n").lower()
	print(user_input)

#TODO define play and its options to select a category or to use a random category
#also handle the error for if the word bank is empty
#define add and its options to add a category or a word to a category
#maybe reformat the user loop to work within one try except to catch all errors at once




if __name__ == '__main__':
	main()