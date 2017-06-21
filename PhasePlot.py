import pylab as p
import numpy as n
import matplotlib.pyplot as pyplot

solution = n.loadtxt("phasedata.txt")
lambdak = n.loadtxt("lambdadata.txt")
#print solution

#p.plot(solution[:,0],solution[:,1],color = 'r')
#p.xlabel(r'$\theta$');p.ylabel(r'$\omega$')
#p.scatter(solution[:,2],solution[:,3],color = 'b')
#p.show()

sub = 'LCE'
fig = pyplot.figure()
semi = fig.add_subplot(1,1,0)

plts, = semi.semilogx(lambdak[:,0],lambdak[:,1])
average = round(n.mean(lambdak[400::,1]),5)
uncert  = round(n.std(lambdak[400::,1]),6)
pyplot.text(10,0.6,'         	 ' + r'$\lambda$'+ ' = ' + str(average) + '\n' + "Uncertainty = " + str(uncert) )
p.ylabel(r'$\lambda_k$');p.xlabel('k')
p.title(r'$\tau$' + ' = 2')
p.show()

#p.clf()
#p.scatter(lambdak[:,0],lambdak[:,1])
#p.set_xscale('log')
#p.show()


fig = pyplot.figure()
semi = fig.add_subplot(1,1,0)
p.title("LogLog Plot of " + r'$\tau$' + ' = 2')
plts, = semi.loglog(lambdak[:,0],lambdak[:,1])
pyplot.text(10,0.6,'         	 ' + r'$\lambda$'+ ' = ' + str(average) + '\n' + "Uncertainty = " + str(uncert) )
p.ylabel(r'$\lambda_k$');p.xlabel('k')
p.show()

print max(lambdak[:,0])
print n.mean(lambdak[400::,1])