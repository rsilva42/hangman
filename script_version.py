import random

#this is a proof of concept script that implements the simple functionality of the game
print("Welcome to hangman...")

lives = 10

word_bank = {   "fruits" : ["apple", "banana", "pear"],
                "meats" : ["poultry", "beef", "pork"] }

category = random.choice(list(word_bank.keys()))

word = word_bank[category][random.randrange(len(word_bank[category]))]

blanks = [ "_" for i in range(len(word)) ]

letters_used = ""

print("The category is " + category)

# print pretty
# for i in blanks:
# 	print(i, end= ' ')
# print('')

print(blanks)

while lives:
	guess = input("Guess a letter: ").lower()
	if len(guess) != 1:
		print("Only one letter at a time please!")
	else:
		if guess in letters_used:
			print("You already guessed that character!")
		elif guess in word:
			for i in range(len(word)):
				if word[i] in guess:
					blanks[i] = word[i]
			print("Correct!")
			print(blanks)
		else:
			lives -= 1
			print("wrong, lives left: {}".format(lives))
		letters_used += (guess)
		if not '_' in blanks:
			print("CONGRATULATIONS!\nYOU WIN!")
			exit()
print("GAME OVER")