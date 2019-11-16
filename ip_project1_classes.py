# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 16:13:49 2019

@author: Melike Mat
"""

from skimage import filters, exposure, transform, morphology
from skimage.color import rgb2gray
from skimage.util import invert
import cv2
import numpy as np
from PIL import Image, ImageTk
import matplotlib.pyplot as plt

class Filter():
    def __init__(self, input_img):
        self.input_img = np.asarray(input_img.convert('L'))

    def gaussian_filter(self): #add sigma option later 
        p = filters.gaussian(self.input_img, sigma=10)
        return ImageTk.PhotoImage(Image.fromarray((p * 255).astype("uint8"), mode= "L"))

    def sobel_filter(self):
        p = filters.sobel(rgb2gray(self.input_img))
        return ImageTk.PhotoImage(Image.fromarray((p * 255).astype("uint8"), mode= "L"))

    def gabor_filter(self):
        filt_real, filt_imag = filters.gabor(self.input_img, frequency=0.1)
        return ImageTk.PhotoImage(Image.fromarray(np.uint8(filt_real)))

    def min_thr_filter(self):
        p = filters.threshold_minimum(rgb2gray(self.input_img))
        binary = rgb2gray(self.input_img) > p
        return ImageTk.PhotoImage(Image.fromarray((binary * 255).astype("uint8"), mode= "L"))

    def bilateral_filter(self):
        p = cv2.bilateralFilter(self.input_img, 15, 80, 80)
        return ImageTk.PhotoImage(Image.fromarray(np.uint8(p)))

    def prewitt_filter(self):
        p = filters.prewitt(rgb2gray(self.input_img))
        return ImageTk.PhotoImage(Image.fromarray((p * 255).astype("uint8"), mode= "L"))

    def laplace_filter(self):
        p = filters.laplace(self.input_img)
        return ImageTk.PhotoImage(Image.fromarray((p * 255).astype("uint8"), mode= "L"))

    def scharr_filter(self):
        p = filters.scharr(rgb2gray(self.input_img))
        return ImageTk.PhotoImage(Image.fromarray((p * 255).astype("uint8"), mode= "L"))

    def otsu1_thr_filter(self):
        p = filters.threshold_otsu(rgb2gray(self.input_img))
        binary = rgb2gray(self.input_img) > p #?
        return ImageTk.PhotoImage(Image.fromarray((binary * 255).astype("uint8"), mode= "L"))
    
    def otsu2_thr_filter(self):
        p = filters.threshold_otsu(rgb2gray(self.input_img))
        binary = rgb2gray(self.input_img) < p #?
        return ImageTk.PhotoImage(Image.fromarray((binary * 255).astype("uint8"), mode= "L"))
 
#exposure, histogram görüntüleme ve eşikleme
class Exposure():
    def __init__(self, input_img):
        self.input_img = np.asarray(input_img.convert('L'))
        
    def show_hist(self):
        """#yapmanın yolu varmış"""
        x, y = exposure.histogram(self.input_img)
        hist = plt.plot(y, x)
        return ImageTk.PhotoImage(Image.fromarray(np.uint8(hist)))
    
    def eq_hist(self):
        p = exposure.equalize_hist(self.input_img)
        return ImageTk.PhotoImage(Image.fromarray((p * 255).astype("uint8"), mode= "L"))

    def rescale_intensity(self):
        p = exposure.rescale_intensity(self.input_img)
        return ImageTk.PhotoImage(Image.fromarray((p * 255).astype("uint8"), mode= "L"))
      
class Transform():
    def __init__(self, input_img):
        self.input_img = np.asarray(input_img.convert('L'))
        
    def resize(self):
        p = transform.resize(self.input_img, (1000, 500), mode='reflect')
        return ImageTk.PhotoImage(Image.fromarray((p * 255).astype("uint8"), mode= "L"))
    
    def rotate(self):
        p = transform.rotate(self.input_img, 90)
        return ImageTk.PhotoImage(Image.fromarray((p * 255).astype("uint8"), mode= "L"))
    
    def rescale(self):
        p = transform.rescale(self.input_img, 1000)
        return ImageTk.PhotoImage(Image.fromarray((p * 255).astype("uint8"), mode= "L"))
    
    def radon(self):
        p = transform.radon(self.input_img)
        return ImageTk.PhotoImage(Image.fromarray((p * 255).astype("uint8"), mode= "L"))
    
    def swirl(self):
        p = transform.swirl(self.input_img)
        return ImageTk.PhotoImage(Image.fromarray((p * 255).astype("uint8"), mode= "L"))
    
class Morphology():
    def __init__(self, input_img):
        self.input_img = np.asarray(input_img.convert('L'))
        self.s_elem = morphology.disk(6)

    def square(self): #add parameters
        p = morphology.square(100)
        return ImageTk.PhotoImage(Image.fromarray((p * 255).astype("uint8"), mode= "L"))
    """all white"""

    def convex_hull(self):
        p = morphology.convex_hull_image(invert(self.input_img))
        return ImageTk.PhotoImage(Image.fromarray((p * 255).astype("uint8"), mode= "L"))
    """all white"""

    def erosion(self):
        p = morphology.erosion(self.input_img, self.s_elem)
        return ImageTk.PhotoImage(Image.fromarray(np.uint8(p)))

    def dilation(self):
        p = morphology.dilation(self.input_img, self.s_elem)
        return ImageTk.PhotoImage(Image.fromarray(np.uint8(p)))

    def opening(self):
        p = morphology.opening(self.input_img, self.s_elem)
        return ImageTk.PhotoImage(Image.fromarray(np.uint8(p)))

    def closing(self):
        p = morphology.closing(self.input_img, self.s_elem)
        return ImageTk.PhotoImage(Image.fromarray(np.uint8(p)))

    def white_tophat(self):
        p = morphology.white_tophat(self.input_img, self.s_elem)
        return ImageTk.PhotoImage(Image.fromarray(np.uint8(p)))

    def black_tophead(self):
        p = morphology.black_tophat(self.input_img, self.s_elem)
        return ImageTk.PhotoImage(Image.fromarray(np.uint8(p)))

    def skeletonize(self):
        """burada bi şeyler var"""
        p = morphology.skeletonize(rgb2gray(self.input_img)) #probably wrong
        return ImageTk.PhotoImage(Image.fromarray(np.uint8(p)))

    def watershed(self):
        pass #later
