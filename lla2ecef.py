# The conversion from WGS-84 to Cartesian has an analytical solution
import numpy as np

def lla2ecef(lat, lon, alt):
	a = 6378137
	a_sq = a**2
	e_sq = 6.69437999014e-3

	N = a/np.sqrt(1 - e_sq*np.sin(lat)**2)
	x = (N+alt)*np.cos(lat)*np.cos(lon)
	y = (N+alt)*np.cos(lat)*np.sin(lon)
	z = ((1-e_sq)*N+alt)*np.sin(lat)

	return x, y, z
