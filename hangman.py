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
		"remove": to remove a category or a word from the word bank
		"exit": to exit the input loop

	if no word bank is supplied an empty word bank will be initialized'''

	#infinite loop until user inputs 'exit'
	while True:
		user_input = input("What would you like to do?\nOptions are: 'play', 'add', 'remove' and 'exit'\n").lower()

		try:
			if user_input == "play":
				select_category(word_bank)
			elif user_input == "add":
				bank_add(word_bank)
			elif user_input == "remove":
				bank_remove(word_bank)
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
	user_input = "yes"

	while user_input == "yes":
		user_input = input("Insert a category.\nYou may also try 'random' for a random category and 'list' for a list of the categories in the word bank\n").lower()

		#if input is list then print the categories and loop back
		if user_input == "list":
			print("The current bank contains:")
			for category in list(word_bank.keys()):
				print(category)
			continue

		#if input is random then fill category variable with a random category
		elif user_input == "random":
			category = random.choice(list(word_bank.keys()))

		#if input is not a category, print an error and ask for input again
		elif user_input not in list(word_bank.keys()):
			print("Category not found, try again...")
			continue

		#fill category with input
		else:
			category = user_input
		print("The category is {}".format(category))

		#select a random word from the category
		word = random.choice(word_bank[category])

		hangman_guess(word)

		#allow the player to try again or exit
		user_input = input("Try again? yes/no\n").lower()

def hangman_guess(word, lives=10):
	'''usage: hangman_guess(lives=10, word)

	will allow the user 'lives' amount of wrong guesses to complete the word one letter at a time.
	upon completion print a congratulations and exit'''

	#create a set of blanks for the letters guessed right and an empty string of letters already guessed
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

			letters_used += guess

			#if no blanks are left the game is won
			if not '_' in blanks:
				print("CONGRATULATIONS!\nYOU WIN!")
				return

	#if the loop is broken, lives hit 0
	print("you ran out of lives!\nGAME OVER")

def display_blanks(blanks):
	'''usage: display_blanks(blanks)

	where blanks is a list of characters to be printed in hangman format
	ex: "_ i _ _ _"'''

	for char in blanks:
		print(char, end=' ')
	#empty print for the new line at the end
	print('')

def bank_add(word_bank):
	user_input = input("What would you like to add?\nOptions are: 'category' and 'word'\n").lower()

	if user_input == "category":
		add_category(word_bank)
	elif user_input == "word":
		add_word(word_bank)

def add_category(word_bank):
	category_to_add = input("What category would you like to add?\n").lower()

	user_input = input("Is {} good? yes/no (this will overwrite existing categories)\n".format(category_to_add)).lower()

	if user_input == "yes":
		word_bank[category_to_add] = []
		print("{} category added".format(category_to_add))


def add_word(word_bank):
	category = input("What category would you like to add the word to?\n").lower()

	if (category in word_bank.keys()):
		word_to_add = input("What is the word?\n").lower()

		user_input = input("Is {} good? yes/no\n".format(word_to_add)).lower()

		if user_input == "yes":
			word_bank[category].append(word_to_add)
			print("Word {} added".format(word_to_add))
	else:
		print("category not found, please try again...")

def bank_remove(word_bank):
	user_input = input("What would you like to remove?\nOptions are: 'category' and 'word'\n").lower()

	if user_input == "category":
		remove_category(word_bank)
	elif user_input == "word":
		remove_word(word_bank)

def remove_category(word_bank):
	category_to_remove = input("What category would you like to remove?\n").lower()

	if category_to_remove in word_bank.keys():
		user_input = input("Are you sure you want to remove the {} category? yes/no (this cannot be undone)\n".format(category_to_remove)).lower()

		if user_input == "yes":
			word_bank.pop(category_to_remove)
			print("{} category removed".format(category_to_remove))
	else:
		print("{} category does not exist".format(category_to_remove))

def remove_word(word_bank):
	category = input("In which category is the word you would like to remove?\n").lower()

	if (category in word_bank.keys()):
		word_to_remove = input("What is the word?\n").lower()

		if word_to_remove in word_bank[category]:
			user_input = input("Are you sure you want to remove {}? yes/no (this cannot be undone)\n".format(word_to_remove)).lower()

			if user_input == "yes":
				word_bank[category].remove(word_to_remove)
				print("Word {} removed".format(word_to_remove))
		else:
			print("{} word not found".format(word_to_remove))
	else:
		print("category not found, please try again...")

#TODO documentation for add and remove functions

if __name__ == '__main__':
	main()
