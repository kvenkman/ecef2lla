# A test bench that produces random lat, long, alt values, converts them
# to ECEF values, and then converts the ECEF values back to lat, long, alt
# The testbench then prints the mean average error associated with this circular
# conversion

import numpy as np
def testbench(samples = 1000):

    lat  = -90. + 180.*np.random.rand(samples, 1)
    long = -180. + 360.*np.random.rand(samples, 1)
    alt  = -11e3 + (20e3)*np.random.rand(samples, 1) # From approximately the bottom of the Mariana trench, to the top of the Everest
