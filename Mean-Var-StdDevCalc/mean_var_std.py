#Start from boilerplate code from https://freecodecam-boilerplate-nd4sfldtyd1.ws-us110.gitpod.io/
import numpy as np

def calculate(list):
    array = np.array([list[:3],
                     list[3:6],
                     list[6:]])
    print(array)


    #should return
    #    {
    #  'mean': [axis1, axis2, flattened], or [meancoloumns], [mean rows], meanalldata
    #  'variance': [axis1, axis2, flattened],
    #  'standard deviation': [axis1, axis2, flattened],
    #  'max': [axis1, axis2, flattened],
    #  'min': [axis1, axis2, flattened],
    #  'sum': [axis1, axis2, flattened]
    #}

    return calculations