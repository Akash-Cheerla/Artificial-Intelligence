import sys
import numpy as np

def pstate(val):
	
	return int((val+1.2)*100)

def posi(state):
	
	return (state/100.0)-1.2

def vstate(val):
	return int((val+0.07)*1000)

def velo(state):
	return ((state/1000.0)-0.07)

def prob(sp,sv,sdp,sdv,act):
	pass

def newStateCalc(cp,cv,act):
	
	pos = posi(cp)
	vel = velo(cv)
	new_vel = round(vel + act*0.001 + np.cos(3*pos)*(-0.0025),2)
	new_pos = round(pos + new_vel,1)
	pnew = pstate(new_pos)
	vnew = vstate(new_vel)
	return pnew,vnew




		

class Car:

	def __init__(self):

		self.position=-0.5
		self.numpos = 180
		self.numvel = 140
		self.numstates = self.numpos*self.numvel
		self.velocity=0.0
		self.V = np.zeros((self.numpos,self.numvel)) # V[position_state][velocity_state] = 0.0	
		self.actions=[-1,0,1]
		self.policy=np.zeros((self.numpos*self.numvel))
		self.gamma = 0.75	
		self.alpha = 0.0001

	def valueIteration(self):
		converged = False
		itr = 0
		while not converged:
			converged = True
			for p in range(self.numpos):
				for v in range(self.numvel):
					
					v_array = []
					for a in self.actions:
						
						pnew,vnew = newStateCalc(p,v,a)
						print (pnew , vnew)
						V = 0.0
						V = V + (-1)  #reward is -1 always
						V = V + self.gamma*self.V[pnew][vnew]
						v_array.append(V)
					#updating the value of V
					new_V = max(v_array)
					pi = np.argmax(v_array)
					change = abs(self.V[p][v] - new_V)<self.alpha
					converged = converged and change
					self.V[p][v] = new_V









if __name__=="__main__":
	car = Car()
	#car.valueIteration()
sys.exit(0)
