import random
from pprint import pprint

k=20
maxDist = 100
density = 0.2

def value():
	if (random.random() > density):
		return None
	else:
		return random.randint(0,maxDist)

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
		if a[i][j]:
			print ",",a[i][j],
		else:
			print ",",
	print ""


