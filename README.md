# ecef2lla
Co-ordinate transformation (ECEF - LLA) routines in Python
Functions in Python written to convert between ECEF and (Lat, Long, Alt) coordinates.

While the transformation from (lat, lon, alt) to (x, y, z) is a relatively straightforward process, the inverse transformation is more involved.

Here, we use the code previously available (https://www.mathworks.com/matlabcentral/mlc-downloads/downloads/submissions/7942/versions/1/previews/lla2ecef.m/index.html, https://en.wikipedia.org/wiki/Geographic_coordinate_conversion#From_geodetic_to_ECEF_coordinates) for the first transformation, and follow the work of Hugues Vermeille ("An analytical method to transform geocentric into geodetic coordinates, 2011)" and Zhu (https://en.wikipedia.org/wiki/Geographic_coordinate_conversion#The_application_of_Ferrari's_solution, https://ieeexplore.ieee.org/document/303772)to produce two functions for the latter transformation.
