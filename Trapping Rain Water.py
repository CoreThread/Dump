def findWater(a, n):
	r = 0
	lm = 0
	rm = 0
	lo = 0
	hi = n-1
	while(lo <= hi):
		if(a[lo] < a[hi]):
			if(a[lo] > lm):
				lm = a[lo]
			else:
				r += lm - a[lo]
			lo+= 1
		else:
			if(a[hi] > rm):
				rm = a[hi]
			else:
				r += rm - a[hi]
			hi-= 1
	return r
a = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(a)
print("Maximum water that can be accumulated is ",
		findWater(a, n))