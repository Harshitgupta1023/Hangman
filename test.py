# used to modify the file //no use in game
a = open('file.txt','r')
c = {}
k = ord('a')
for i in range(ord('A'),ord('Z')+1):
	c[chr(i)] = chr(k)
	k+=1
for i in a:
	for j in i :
		if j in c :
			j = c[j]
		print(j,end='')