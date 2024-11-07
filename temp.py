# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#pip install numpy
#!pip3 install numpy

import numpy as np
import matplotlib.pyplot as plt

xx = np.linspace(0,10,201,True)
yy = np.sin(xx)

#plt.grid(b=True)
plt.plot(xx,yy)
plt.show()