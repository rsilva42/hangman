#initiate the word bank and run the user interface
def main():
	word_bank = init_default_words()

	main_menu(word_bank)

#initiate a default set of words containing five categories with ten words each
def init_default_words():
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

	while user_input != "exit"
		user_input = input("What would you like to do?\noptions are: 'play', 'add', and 'exit'").lower()

		if user_input == "play":
			try:
				play(word_bank)
			except Exception as e:
				print(e)

#TODO define play and its options to select a category or to use a random category
#also handle the error for if the word bank is empty
#define add and its options to add a category or a word to a category
#maybe reformat the user loop to work within one try except to catch all errors at once
