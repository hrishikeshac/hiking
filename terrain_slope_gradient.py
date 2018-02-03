#1. Import necessary python package(s)
import numpy as np

#2. Write a function
def get_slope_gradient(distance_hiked, elevation_change):
    """
    Input: horizontal distance in miles, elevation change in feet
    Output: terrain slope (degrees) and terrain gradient (%)
    """
    #1. Convert feet to miles
    elevation_change = elevation_change*0.000189394
    #2. Get horizontal distance using Pythagoras theorem (distance_hiked = hypotenuse)
    horizontal_dist  = np.sqrt(distance_hiked**2 - elevation_change**2)
    #3. Compute ratio between horizontal distance change vs vertical elevation change.
    ratio            = elevation_change/horizontal_dist
    #4. Compute gradient. It is just percent of that ratio
    gradient         = (ratio)*100
    #5. Compute slope. It is the inverse Tangent of the ratio.
    slope            = np.rad2deg(np.arctan(ratio))
    #6. Print Slope and Gradient information
    deg = u"\xb0"
    print 'Slope     = %.1f '%np.round(slope, decimals = 1) + deg
    print 'Gradient  = %.1f %%'%np.round(gradient,decimals = 1)

#3. Collect inputs from the user
elevation_change = float(raw_input('Please enter elevation change in feet '))
distance_hiked   = float(raw_input('Please enter distance hiked in miles '))

#4. Run the function
get_slope_gradient(elevation_change = elevation_change, distance_hiked = distance_hiked)
