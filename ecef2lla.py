# Converting ECEF (x, y, z) coordinates to (lat, lon, alt) values
# Author: Karthik Venkataramani
# Date 02/23/2019

import numpy as np

def ecef2lla_hugues(x, y, z):
	# x, y and z are scalars in meters (CANNOT use vectors for this method)
	# Following "An analytical method to transform geocentric into geodetic coordinates"
	# By Hugues Vermeille (2011)

	x = np.array([x]).reshape(np.array([x]).shape[-1], 1)
	y = np.array([y]).reshape(np.array([y]).shape[-1], 1)
	z = np.array([z]).reshape(np.array([z]).shape[-1], 1)

	a=6378137
	a_sq=a**2
	e = 8.181919084261345e-2
	e_sq = 6.69437999014e-3

	p = (x**2 + y**2)/a_sq
	q = ((1 - e_sq)*(z**2))/a_sq
	r = (p + q - e_sq**2)/6.

	evolute = 8*r**3 + p*q*(e_sq**2)

	if(evolute > 0):
		u = r + 0.5*(np.sqrt(8*r**3 + p*q*e_sq**2) + np.sqrt(p*q*e_sq**2))**(2/3.) + \
				0.5*(np.sqrt(8*r**3 + p*q*e_sq**2) - np.sqrt(p*q*e_sq**2))**(2/3.)
	else:
		u_term1 = np.sqrt(p*q*e_sq**2)/(np.sqrt(-8*r**3 - p*q*e_sq**2) + np.sqrt(-8*r**3))
		u_term2 = (-4.*r)*np.sin((2./3.)*np.arctan(u_term1))
		u_term3 = np.cos(np.pi/6. + (2./3.)*np.arctan(u_term1))
		u       = u_term2*u_term3

	v = np.sqrt(u**2 + q*e_sq**2)
	w = e_sq*(u + v - q)/(2.*v)
	k = (u + v)/(np.sqrt(w**2 + u + v) + w)
	d = k*np.sqrt(x**2 + y**2)/(k + e_sq)
	h = np.sqrt(d**2 + z**2)*(k + e_sq - 1)/k
	phi = 2.*np.arctan(z/((np.sqrt(d**2 + z**2) + d)))

	if((q == 0) and (p <= e_sq**2)):
		h = -(a*np.sqrt(1 - e_sq)*np.sqrt(e_sq - p))/(e)
		phi1 = 2*np.arctan(np.sqrt(e_sq**2 - p)/(e*(np.sqrt(e_sq - p)) + np.sqrt(1 - e_sq)*np.sqrt(p)))
		phi2 = -phi1
		phi = (phi1, phi2)


	case1 = (np.sqrt(2) - 1)*np.sqrt(y**2) < np.sqrt(x**2 + y**2) + x
	case2 = np.sqrt(x**2 + y**2) + y < (np.sqrt(2) + 1)*np.sqrt(x**2)
	case3 = np.sqrt(x**2 + y**2) - y < (np.sqrt(2) + 1)*np.sqrt(x**2)

	if(case1):
		print("case1")
		lambd = 2.*np.arctan(y/(np.sqrt(x**2 + y**2) + x))
		return phi*180/np.pi, lambd*180/np.pi, h
	if(case2):
		print("case2")
		lambd = (-np.pi/2) - 2.*np.arctan(x/(np.sqrt(x**2 + y**2) - y))
		return phi*180/np.pi, lambd*180/np.pi, h
	if(case3):
		print("case3")
		lambd = (np.pi/2) - 2.*np.arctan(x/(np.sqrt(x**2 + y**2) + y))
		return phi*180/np.pi, lambd*180/np.pi, h


def ecef2lla(x, y, z):
	# x, y and z are scalars or vectors in meters
	x = np.array([x]).reshape(np.array([x]).shape[-1], 1)
	y = np.array([y]).reshape(np.array([y]).shape[-1], 1)
	z = np.array([z]).reshape(np.array([z]).shape[-1], 1)

	a=6378137
	a_sq=a**2
	e = 8.181919084261345e-2
	e_sq = 6.69437999014e-3

	f = 1/298.257223563
	b = a*(1-f)

	# calculations:
	r = np.sqrt(x**2 + y**2)
	ep_sq  = (a**2-b**2)/b**2
	ee = (a**2-b**2)
	f = (54*b**2)*(z**2)
	g = r**2 + (1 - e_sq)*(z**2) - e_sq*ee*2
	c = (e_sq**2)*f*r**2/(g**3)
	s = (1 + c + np.sqrt(c**2 + 2*c))**(1/3.)
	p = f/(3.*(g**2)*(s + (1./s) + 1)**2)
	q = np.sqrt(1 + 2*p*e_sq**2)
	r_0 = -(p*e_sq*r)/(1+q) + np.sqrt(0.5*(a**2)*(1+(1./q)) - p*(z**2)*(1-e_sq)/(q*(1+q)) - 0.5*p*(r**2))
	u = np.sqrt((r - e_sq*r_0)**2 + z**2)
	v = np.sqrt((r - e_sq*r_0)**2 + (1 - e_sq)*z**2)
	z_0 = (b**2)*z/(a*v)
	h = u*(1 - b**2/(a*v))
	phi = np.arctan((z + ep_sq*z_0)/r)
	lambd = np.arctan2(y, x)


	return phi*180/np.pi, lambd*180/np.pi, h
