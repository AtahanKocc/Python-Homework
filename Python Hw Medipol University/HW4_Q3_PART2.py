"""
Author: Atahan Koc
Description Part: In this problem, the problem, according to the table of NumPy polyfit and polyval polynomial regression methods using the package rates for all years between the years 1991-2012 we asked to estimate annual 1 gram of gold. First, the year and price information were entered, and then the data were modeled using the polyfit method. After obtaining a polynomial modeling the data, the value of the polynomial for the given years was determined using the polival method.
Then the output was successfully obtained.
"""

import numpy as np
from matplotlib import pyplot as plt

years= np.array([1991,1994,1999,2013,2006,2009,2012])
prices = np.array([0.05, 0.45, 4.90, 20,28,54,98])

new_years = [year for year in range(1991, 2013)]

# i model the data using the polyfit method.
pol1= np.polyfit(years,prices,1)
pol3= np.polyfit(years,prices,3)
pol5=np.polyfit(years,prices,5)

# this method find the value of the polynomial for the given years.
eval_pol1= np.polyval(pol1,new_years)
eval_pol3= np.polyval(pol3,new_years)
eval_pol5= np.polyval(pol5,new_years)


plt.title("Annual prices for gram gold")
plt.plot(new_years, eval_pol1, label=" first order polynomial regression")
plt.plot(new_years, eval_pol3, label=" third order polynomial regression")
plt.plot(new_years, eval_pol5, label=" fifth order polynomial regression")
plt.legend(loc="upper left")
plt.xlabel("years")
plt.ylabel("prices")
plt.grid(True)
plt.show()
