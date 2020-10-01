# Opens a text file containing words and forms a list out of the word present in them.

def words_list():
	a = open('file.txt','r')
	b = []
	c = []
	for i in a :
		b.append(i)
	for j in range(len(b)-1) :
		c.append(b[j][:len(b[j])-1])
	c.append(b[-1])
	return (c,len(b))
