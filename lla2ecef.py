# The conversion from WGS-84 to Cartesian has an analytical solution
import numpy as np

def lla2ecef(lat, lon, alt):
	a = 6378137
	a_sq = a**2
	e = 8.181919084261345e-2
	e_sq = e**2
	b_sq = a_sq*(1 - e_sq)

	lat = np.array([lat]).reshape(np.array([lat]).shape[-1], 1)*np.pi/180
	lon = np.array([lon]).reshape(np.array([lon]).shape[-1], 1)*np.pi/180
	alt = np.array([alt]).reshape(np.array([alt]).shape[-1], 1)

	N = a/np.sqrt(1 - e_sq*np.sin(lat)**2)
	x = (N+alt)*np.cos(lat)*np.cos(lon)
	y = (N+alt)*np.cos(lat)*np.sin(lon)
	z = ((b_sq/a_sq)*N+alt)*np.sin(lat)

	return x, y, z
