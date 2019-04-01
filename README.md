# ecef2lla
Co-ordinate transformation (ECEF <-> LLA) routines written in Python.


It is noted that while the transformation from (lat, lon, alt) to (x, y, z) is a relatively straightforward process, the inverse transformation is more involved.

The work here is based on code previously available (https://www.mathworks.com/matlabcentral/mlc-downloads/downloads/submissions/7942/versions/1/previews/lla2ecef.m/index.html, https://en.wikipedia.org/wiki/Geographic_coordinate_conversion#From_geodetic_to_ECEF_coordinates) for the first transformation, and follows the work of Hugues Vermeille ("An analytical method to transform geocentric into geodetic coordinates, 2011)" and Zhu (https://en.wikipedia.org/wiki/Geographic_coordinate_conversion#The_application_of_Ferrari's_solution, https://ieeexplore.ieee.org/document/303772) to produce two functions for the latter transformation.

The ecef2lla.py module contains the ecef2lla_hugues() and ecef2lla() methods corresponding to the two methods of this transformation. The first one however is not ready for prime time and needs some clarification regarding the value of longitude returned.
