import random
from pprint import pprint

n=10
k=14
priceRange = [5,20]
variability = 0.2
density = 0.2
sigma = 0.4
numberRange = [1,3]

def price(median):
	if (random.random() > density):
		return None
	else:
		price = random.gauss(median,sigma)
		return abs(round(price,2))


medianPrices = [random.randint(priceRange[0],priceRange[1]) for x in range(n)]
pricesArray = [[price(medianPrices[z]) for x in range(k)] for z in range(n)]

print "Artikel\Geschaeft,Menge",
for x in range(1,k):
	print ", g"+str(x),
print ""
for i in range(n):
	print "a"+str(i),
	print ", "+str(random.randint(numberRange[0],numberRange[1])),
	for j in range(1,k):
		if pricesArray[i][j]:
			print ",",pricesArray[i][j],
		else:
			print ",",
	print ""


