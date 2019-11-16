# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 21:45:21 2019

@author: melike
"""


from skimage import io
from matplotlib import pyplot as plt
from ip_project1_classes import Exposure, Filter

#classes can be more object oriented   


#io --> Image object
load = io.imread("can-warhol.jpg") #input with numpy
io.imshow(load)
io.show()

obj = Exposure(load)
obj2 = Filter(load)

plt.imshow(obj.eq_hist(), cmap="gray")
plt.show()
    

"""
import cv2
from skimage import data, io
from matplotlib import pyplot as plt
from ip_project1_classes import *
import numpy as np

#classes can be more object oriented   



load = data.coins() #input with numpy


obj = Filter(load)

filter_list = [obj.bilateral_filter(), obj.gabor_filter(), obj.gaussian_filter,
               obj.laplace_filter(), obj.min_thr_filter(), obj.otsu_thr_filter(),
               obj.prewitt_filter(), obj.scharr_filter(), obj.sobel_filter()]

#colormap!!!!!!!!!!!!!!!!
for i in range(len(filter_list)):
    img = np.squeeze(i)
    plt.imshow(img, cmap="gray")
    plt.show()
  
 
 """