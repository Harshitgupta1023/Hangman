# predict a word from the file

import generate_number
import random 
def word():
	a,x = 	generate_number.words_list()
	b = random.randrange(0,x+1)
	return a[b]
	