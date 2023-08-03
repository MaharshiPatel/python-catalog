#!/usr/bin/python
import numpy as np

# Function definition is here
def printme( str ):
    # This prints a passed string into this function
    print (str)
    rng = np.random.default_rng()
    samples = rng.normal(size=2500)
    print (samples)
    return;

# Now you can call printme function
printme("Hello from JFROG");
