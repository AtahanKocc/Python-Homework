"""
Author: Atahan Koc
Description Part: In this question, using interpolation.We were asked to use the interp1d method of the SciPy package.
I have included these packages in our code. I have written down the years and prices given. I have drawn the interpolated results of these and obtained the output.
"""
# PART 1
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import numpy as np

years= np.array([1991,1994,1999,2013,2006,2009,2012])
prices = np.array([0.05,0.45,4.90,20,28,54,98])

f_lineer = interp1d(years, prices)
f_cubic = interp1d(years, prices)

new_years = [year for year in range(1991, 2013)]

# The input data and interpolated results  is plotted
plt.title("Annual prices of 1 gram of gold")
plt.plot(years, prices)
plt.plot(new_years, f_lineer(new_years))
plt.plot(new_years, f_cubic(new_years))
plt.xlabel("years")
plt.ylabel("prices")
plt.grid(True)
plt.show()