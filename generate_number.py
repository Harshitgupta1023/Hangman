# take words from a file

def words_list():
	a = open('file.txt','r')
	b = []
	c = []
	for i in a :
		b.append(i)
	for j in range(len(b)-1) :
		c.append(b[j][:len(b[j])-1])
	return (c,len(b))
