# game layout
import ge_word
#get a word
word = ge_word.word()
#print(word) #  showing the word
all_enter_words = []
c = []
k = len(set(word))
number_of_turns = k+1
while number_of_turns >= 0 and len(c)<k :
	print("YOU CAN GUESS WORD :",number_of_turns,"times")
	a = input('enter : ',)
	if a in all_enter_words:
		print("YOU HAVE ALREADY ENTERED THIS WORD")
	if a not in all_enter_words:
		all_enter_words.append(a)
		number_of_turns-=1
	if a in word :
		c.append(a)
	for i in word :
		if i in all_enter_words :
			print(i,end = ' ')
		else:
			print('-',end=' ')
	print()
c = set(c)
if len(c)== k :
	print("YOU WON THE GAME")
else:
	print("YOU LOSE THE GAME TRY AGAIN")
	print("The word was",word)
