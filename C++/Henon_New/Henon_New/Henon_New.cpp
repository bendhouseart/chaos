// Henon_New.cpp : Defines the entry point for the console application.
//


#include "stdafx.h"
#include <stdint.h>
#include <conio.h>
#include <math.h>
#include <iostream>
#include <conio.h>
#include <vector>
#include <fstream>
#include <Windows.h>
#include <string>
#include <vector>

using namespace std;


double Ax(double t, double x, double vx)
{
	
	double wd = 2./3.;
	double A = 1.15;
	double gamma = 0.5;
	double accel =  -gamma*vx - sin(x) + A*sin(wd*t);

	return accel;

}


double Vx(double t, double x,double vx)
{
	
	double ret;
	ret = vx;
	return vx;

}

void main()
{
	//our integration loops are nested inside of this initial condtion loop
	//for a range of allowable conditions y crossings at our plane will 
	//generated and recorded. Par for the course fists of ham will be used
	//to generate a very dense output of both initial conditions and thus
	//a dense sos plot. Plotting will be performed outside of the scope of this
	//cpp program, in mathematica possibly if it plays nice and doesn't
	//crash upon import.
	
	//Opening Storage File for saving x vx phase space stuffs
	ofstream plane,lambdak;
	//plane.open("C:\\Users\\Uma Mobile\\Dropbox\\Spring 2013\\380\\hw6\\Plots\\phasedata.txt");
	//lambdak.open("C:\\Users\\Uma Mobile\\Dropbox\\Spring 2013\\380\\hw6\\Plots\\lambdadata.txt");
	plane.open("C:\\Users\\Uma\\My Documents\\My Dropbox\\Spring 2013\\380\\hw6\\Plots\\phasedata.txt");
	lambdak.open("C:\\Users\\Uma\\My Documents\\My Dropbox\\Spring 2013\\380\\hw6\\Plots\\lambdadata.txt");

	
	//Variable Declaration fiducial Orbit rk4
	double x,vx;
	double tf,t;
	double pi = 3.1415926535898;
	int count = 0, foolproof;
	double k1x,k1vx;
	double k2x,k2vx;
	double k3x,k3vx;
	double k4x,k4vx;

	//Variable Declaration for Test Orbit rk4
	double xy,vxy;
	double d0;
	double k1xy,k1vxy;
	double k2xy, k2vxy;
	double k3xy, k3vxy;
	double k4xy, k4vxy;
	int taui;
	double dt;
	double loggy,tempxy,tempvxy;
	int  counter;

	vector<double> lambda;
	vector<double> kk;

	//Initiliazing Conditions for 
	d0 = 0.001;
	x = 3;
	vx = 0.0;
	xy = x + .001;
	vxy = vx;
	taui = 1000;
	double tau = (double) taui;
	tf = 1000000.0;
	t = 0.0;
	foolproof = 0;
	loggy = 0.0;
	counter = 0;
	dt = 0.01;
	
	
	//First loop executes RK4 for trajectories over a Period of seconds = tf
	while (t < tf)
	{
		
		t += dt;
		foolproof += 1;
		
		k1x  = Vx(t, x, vx);
		k1vx = Ax(t, x, vx);
		
		k1xy  = Vx(t, xy, vxy);
		k1vxy = Ax(t, xy, vxy);

		k2x  = Vx(t, x + 0.5*dt*k1x, vx + 0.5*dt*k1vx);
		k2vx = Ax(t, x + 0.5*dt*k1x, vx + 0.5*dt*k1vx);
			
		k2xy  = Vx(t, xy + 0.5*dt*k1xy, vxy + 0.5*dt*k1vxy);
		k2vxy = Ax(t, xy + 0.5*dt*k1xy, vxy + 0.5*dt*k1vxy);

		k3x  = Vx(t, x + 0.5*dt*k2x, vx + 0.5*dt*k2vx);
		k3vx = Ax(t, x + 0.5*dt*k2x, vx + 0.5*dt*k2vx);

		k3xy  = Vx(t, xy + 0.5*dt*k2xy, vxy + 0.5*dt*k2vxy);
		k3vxy = Ax(t, xy + 0.5*dt*k2xy, vxy + 0.5*dt*k2vxy);
		
		k4x  = Vx(t, x + dt*k3x, vx + dt*k3vx);
		k4vx = Ax(t, x + dt*k3x, vx + dt*k3vx);

		k4xy  = Vx(t, xy + dt*k3xy, vxy + dt*k3vxy);
		k4vxy = Ax(t, xy + dt*k3xy, vxy + dt*k3vxy);

		x =  x  + dt*(1.0/6.0)*(k1x + 2*k2x   + 2*k3x  + k4x);
		vx = vx + dt*(1.0/6.0)*(k1vx + 2*k2vx + 2*k3vx + k4vx);

		xy =  xy  + dt*(1.0/6.0)*(k1xy + 2*k2xy   + 2*k3xy  + k4xy);
		vxy = vxy + dt*(1.0/6.0)*(k1vxy + 2*k2vxy + 2*k3vxy + k4vxy);

		
		

		if (foolproof%(taui) == 0)
		{
			
			
			counter += 1;
			
			kk.push_back(counter*d0*10);
	
			tempxy =   x + (d0*(xy -x))/sqrt((xy - x)*(xy - x)+ (vxy - vx)*(vxy - vx));

			tempvxy = vx + (d0*(vxy- vx))/sqrt((vxy - vx)*(vxy - vx) + (xy - x)*(xy - x));
			
			lambda.push_back(log((sqrt(((xy - x)*(xy - x))+ (vxy - vx)*(vxy - vx)))/d0));
	
			plane << x << ' ' << vx << ' ' << xy << ' ' << vxy << endl;

			xy = tempxy;
			
			vxy = tempvxy;

						
		}

		
	}
	
	
	

	double sum,out1,out2;
	for (int i = 0; i < lambda.size(); i++)
	{
		
		sum = 0;
		

		for ( int j = 0; j < i  ; j++)
		{
			sum += (lambda[j])/(kk[i]*tau);
			

		}
		
		out1 = sum;
		out2 = kk[i];
		lambdak << out2 << ' ' << out1 << ' ' <<  endl;

	}
	
	
	plane.close();
	lambdak.close();
	cout << "Maths has computed"<< endl;
	
	
	//program exits at keyboard input
	//_getch();
	
}
