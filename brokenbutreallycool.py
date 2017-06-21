#physics problem
###########################################################

#Written in 2013 By Anthony Galassi

###########################################################



from math import fmod,floor
from numpy import *		#Might as well use all of numpy, as this will probly be mathy.
from scipy.integrate import odeint #This will be out integrator
import matplotlib.pyplot as p	   #using Matplotlib to plot as usual



#This is our Pendulum EQ set up for integration.
def PendulumEq(thetas,t):
	#Constant values
	wd= 2.0/3.0;gamma = 1./2.;A =1.15
	
	
	#these are the two first order ode's we'll be integrating
	#stored as the value duo which returns a 1X2 list of both
	#eqs evalutade at t,theta1,theta2
	theta2,theta1= - gamma*thetas[1] - sin(thetas[0]) + thetas[2]*cos(wd*t), thetas[1]
	
	return [theta1,theta2]

def normal(rfed,rtest,d0,A):

	normtheta = (d0*(rtest[0] - rfed[0])/(sqrt((rtest[0] - rfed[0])**2 + (rtest[1] -rfed[1])**2)))
	normdtheta = (d0*(rtest[1] - rfed[1])/(sqrt((rtest[0] - rfed[0])**2 + (rtest[1] -rfed[1])**2)))
	
	newr = [rfed[0] + normtheta,rfed[1] + normdtheta,A]
	return newr
	
 
tf = 2000.0				 
iterations = 100000
time_vector = linspace(0,tf,iterations) #time vector this isn't a helpful comment
d0 = 0.001
tau = 2.0
t = 0
testies = []
for i in range(iterations):
	if i%200 == 0:
		testies.append(i)
		print i
	



 # different Amplitude constants for part1b

X,V,A = [1.337], [0.23],[1.15] #again initial position and velocity for partb when needed
colour = ['b']
thetas0 = X[0], V[0], A[0] #calling initial conditions for their respective loops

solution = odeint(PendulumEq,thetas0,time_vector) #solving ode at conditions along time
position = solution[400::,0]						  #tf at 10000 intervals in between
velocity = solution[400::,1]

for i in range(len(velocity)):	
	if -0.001 <= velocity[i] <= 0.001:
		
		start = [position[i] + d0,velocity[i],A[0]]
		index = i
		p.scatter(start[0],start[1],color = 'r')
		break

p.plot(position[i::],velocity[i::],color = 'r')


j = 0
for i in range(len(solution)):
	if testies[j] == i*200:
		print "heyyo!"
		j += 1
	
		testtime = linspace(0,tau,100*tau)
		testorbit = odeint(PendulumEq,start,testtime)
		t += tau
		rfed = [solution[i,0],solution[i,1]]
		
		start = normal(rfed,start,d0,A[0])
		
		p.plot(testorbit[:,0],testorbit[:,1])
		if testies[j] == max(testies):
			print time_vector[i],
			break
		
p.show()





	

