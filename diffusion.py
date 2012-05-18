#!/usr/bin/env python

from numpy import meshgrid, exp, pi, linspace
import matplotlib.pyplot as plt


# units [cm^2/sec]
# diffusion coefficient for ATP in cytoplasm
D = 0.15 * 10**-5
x0 = 0.002
y0 = -0.003

def rho(x,y,x0,y0,t):
	return exp(-((x-x0)**2 + (y-y0)**2)/(4*D*t))/(4*pi*D*t)

x_min = -0.01
x_max = 0.01
y_min = -0.01
y_max = 0.01
X, Y = meshgrid(linspace(x_min,x_max,1000), linspace(y_min,y_max,1000))
timepts = linspace(0,1,10)

for i in range(len(timepts)):
	if timepts[i] == 0:
		continue
	plt.figure(i)
	plt.title('ATP in cytoplasm, t = ' + str(timepts[i]) + ' sec')
	plt.xlabel('X [cm]')
	plt.ylabel('Y [cm]')
	plt.imshow(rho(X,Y,x0,y0,timepts[i]), extent = [ x_min, x_max, y_min, y_max])
plt.show()
