#Name:Akash Cheerla
#R.no:111601029

import numpy as np
import sys

def prob(x,a):
	pw_min = [0.01,0.02,0.03,0.1,0.3]
	pw_max = [0.1,0.2,0.3,0.5,0.7]
	pr_min = 0.5
	pr_max = 0.8

	if a>5:
		a = a-1

	a=a-1

	pw = pw_min[r] + (pw_max[r]-pw_min[r]) * (x-1)/9
	pr = pr_min + (pr_max-pr_min) * (x-1)/9
	return pw,pr


if __name__=="__main__":

	states = [11,10,9,8,7,6,5,4,3,2,1] 
	n      = 9
	v      = np.random.rand(n)
	scores = [1,2,3,4,6]
	print v
	alpha = 0.00001
	diff  = True
	while diff:
		diff=False
		for s in states:
			for b in range(300):
				for a in scores:
					pass



sys.exit(0)
