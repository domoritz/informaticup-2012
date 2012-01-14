import random
from pprint import pprint

k=12
distRange = [10,100]
density = 0.3

def value():
	if (random.random() > density):
		return None
	else:
		return random.randint(distRange[0],distRange[1])

a = [[value() for x in range(k)] for z in range(k)]

print "Fahrtkosten",
for x in range(k):
	print ", g"+str(x),
print ""
for i in range(k):
	print "g"+str(i),
	for j in range(k):
		if i==j:
			a[j][i] = 0
		a[i][j] = a[j][i]
		if a[i][j] != None:
			print ",",a[i][j],
		else:
			print ",",
	print ""


