import numpy as np

def ecef2lla(x, y, z):
	# x, y and z are either scalars or vectos containing ECEF co-ordinates
	  a=6378137;            # radius
	  e=8.1819190842622e-2 # eccentricity
	  a_sq=a**2
	  e_sq=e**2
	  
	  #x=xyz(1)
	  #y=xyz(2)
	  #z=xyz(3)
	  
	  b = np.sqrt(a_sq*(1-e_sq))
	  
	  b_sq = b**2
	  ep = np.sqrt((a_sq - b_sq)/b_sq)
	  p = np.sqrt(x**2 + y**2)
	  
	  th = np.arctan2(a*z, b*p)
	  lon = np.arctan2(y, x)
	  lat = np.arctan2((z + ep*ep*b*sin(th)**3), (p-e_sq*a*cos(th)**3)) 
	  N = a/(np.sqrt(1 - e_sq*sin(lat)**2))
	  
	  g = lla2xyz([lon lat 0])
	  gm = np.sqrt(g(1)*g(1)+g(2)*g(2)+g(3)*g(3))
	  am = np.sqrt(x**2 + y**2 + z**2)
	  alt = am-gm
	  lla = [lon lat alt]
	
	return lat, long, alt