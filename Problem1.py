##########################################################
#this code was used for parts 1a and b respectively
#ie since you're not going to remember that 
#this code can integrate a second order diff eq
#after transformation into 2 1st order ode's
#specfically a Damped driven Pendulum for 380.03
#the front end is a bit more work than feeding an rk4
#but the integration step is a 1 liner
#needs some manhandling to effictively integrate in many
#smaller intervals, but would slice after the fact
#for the strobes by storing each trajectory to a temp file
#or pickling etc.
#otherwise quite fast, would use again for any other 
#physics problem
###########################################################

#Written in 2013 By Anthony Galassi

###########################################################




from numpy import *		#Might as well use all of numpy, as this will probly be mathy.
from scipy.integrate import odeint #This will be out integrator
import matplotlib.pyplot as p	   #using Matplotlib to plot as usual
import matplotlib as mpl


#This is our Pendulum EQ set up for integration.
def PendulumEq(thetas,t):
	#Constant values
	wd= 2.0/3.0;gamma = 1./2.;A =1.15
	
	
	#these are the two first order ode's we'll be integrating
	#stored as the value duo which returns a 1X2 list of both
	#eqs evalutade at t,theta1,theta2
	theta2,theta1= - gamma*thetas[1] - sin(thetas[0]) + thetas[2]*cos(wd*t), thetas[1]
	
	return [theta1,theta2]


 
tf = 500.0				 #total run time in terms of period
time_vector = linspace(0,tf,1000000) #time vector this isn't a helpful comment
counter = zeros((1,),dtype = uint16) # didn't use this should have deleted not commented
#-3*pi to 3*pi x axis, -pi to pi y axis note to self





 # different Amplitude constants for part1b
for i in range(2):
	X,V,A = [pi,pi + 0.001], [0.23,0.23],[1.15,1.15] #again initial position and velocity for partb when needed
	colour = ['b','g']
	thetas0 = X[i], V[i], A[i] #calling initial conditions for their respective loops

	solution = odeint(PendulumEq,thetas0,time_vector) #solving ode at conditions along time
	position200 = solution[:,0]						  #tf at 10000 intervals in between
	velocity200 = solution[:,1]
	position = solution[1000::,0]	
	velocity = solution[1000::,1]					  #see time_vector if above unclear
	#p.axis([-3*pi,3*pi,-pi,pi]) #formating occasionally used, but selection was better for this system
	p.title("Fiducial and Comparator orbit at t = " + str(tf) +  '(s)')# pretty obvious


	p.legend()#using only in cases with 2 or less plots, would flood graph otherwise
	p.ylabel(r'$\theta$' + "dot");p.xlabel(r'$\theta$') #labeling axes
	p.scatter(X[i],V[i], color = 'r') #Plotting point at initial start
	p.plot(position200,velocity200,color = colour[i]) #plotting trajectory from 0 to 200th iteration
	#p.plot(position,velocity,label = str(A[0]),color = 'b') #again obvious
	p.scatter(X[i],V[i], color = 'r') #Plotting point at initial start
	

p.show() #displaying plot