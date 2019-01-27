# ecef2lla
Co-ordinate transformation (ECEF - LLA) routines in Python
Functions in Python written to convert between ECEF and (Lat, Long, Alt) coordinates.
The transformation assumes WGS84 ellipsoid

The conversion from ECEF to LLA is an iterative process without an exact numerical solution. To this end, 
included in the repo is a 'testbench.py' routine that calculates the transformation for 100 points (default value) and prints
the mean error in altitude compared to the ground truth.

Following the calculations and code from the website : https://ea4eoz.blogspot.com/2015/11/simple-wgs-84-ecef-conversion-functions.html
