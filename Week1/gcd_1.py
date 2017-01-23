import sys
import random
def gcd(x):
	minimum_number = min(x)
	gcd = []
	for i in range(1,min(x)+1):
		t=[]
		for j in x:
			if j%i==0:
				t.append(j)
		if len(t)==len(x):
			gcd.append(i)
	return max(gcd)

#Enter the numbers example: "python gcd_1.py 14 21" for finding gcd of 14 and 21'
l = sys.argv[1:]
#l = [random.randint(1,1000)for i in range(2)] for testing
#print l
x=[int(t) for t in l]
y=gcd(x)
print y

