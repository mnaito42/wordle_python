#!/usr/bin/env python3

import random

def print_info():
	print("Wordleへようこそ!")
	print("5文字の単語を当ててください。6回まで挑戦できます。")
	print("O = 正しい文字と位置")
	print("? = 単語に含まれているが位置が違う")
	print("X = 単語に含まれていない")

def get_words(filename="words.txt"):
	words = []
	with open(filename, "r") as file:
		for word in file:
			words.append(word.strip().lower())
	
	return words

def get_feedback(answer, user_guess):
	feedback = []
	i = 0
	while i < len(user_guess):
		char = user_guess[i]
		if answer[i] == char:
			feedback.append("O ")
		elif answer.find(char) != -1 :
			feedback.append("? ")
		else:
			feedback.append("X ")
		i += 1
	return ("".join(feedback))[:9]


print_info()
words = get_words()
answer = random.choice(words)

print(answer)

attempt = 1
while attempt <= 6:
	user_guess = input(f"挑戦 {attempt}: 推測を入力してください: ")
	if len(user_guess) != 5:
		print("ちょうど5文字を入力してください！")
		continue
	elif user_guess not in words:
		print("その単語は辞書にはありません！")
		continue
	else:
		print(f"単語： {user_guess.upper()}")
		feedback = get_feedback(answer, user_guess)
		print(f"\t{feedback}\n")
		if feedback == "O O O O O":
			print(f"おめでとうございます！ {attempt}回で単語'{answer.upper()}'を見つけました！")
			break

		attempt += 1

if attempt == 7:
	print(f"残念！答えは'{answer.upper()}'でした！")



