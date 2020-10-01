# Opens a text file containing words and forms a list out of the word present in them.

def words_list():
	a = open('file.txt','r')
	b = []
	for i in a:
		b.append(i)
	return (b,len(b))
