# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 22:07:30 2019

@author: metal
"""

#bu dosyada iyi kötü çalışan bir şeyler var değiştirme

from tkinter import Tk, Menu, filedialog, Canvas, NW
from ip_project1_classes import Filter, Exposure, Transform, Morphology
from PIL import Image, ImageTk

class FileOperations:
    def __init__(self, root):
        self.root = root

    def open_file(self):
        self.root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    
    def save_file(self):
        self.root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

class MainWindow:
    def __init__(self, root, menu=None):
        self.root = root
        self.menu = menu
        
    def create_canvas(self):
        c = Canvas(self.root, height=250, width=300, bg="white")
        c.pack()
        
    def canvas_image(self, c, img):
        photo = ImageTk.PhotoImage(image = Image.fromarray(img))
        c.create_image(0, 0, image=photo, anchor=NW)
        
    
    def create_menu(self):
        self.menu_file()
        self.menu_transform()
        self.menu_filter()
        self.menu_morphology()
        self.menu_exposure()
    
    def menu_file(self):
        file_menu = Menu(self.menu) 

        f_ops = FileOperations(root)
        
        #buradaki commandler değişecek strategy fonksiyonu yapılıp orada
        #birleştirilip ekrana basan bir fonksiyon olacak
        
        self.menu.add_cascade(label="File", menu= file_menu) 
        file_menu.add_command(label="New") 
        file_menu.add_command(label="Open", command= f_ops.open_file)
        file_menu.add_command(label="Save", command= f_ops.save_file)
        file_menu.add_separator() 
        file_menu.add_command(label="Exit", command= root.destroy)
        
    def menu_transform(self): #add input parameters
        trs_menu = Menu(self.menu)
#if command crush add lambda func with method call
        self.menu.add_cascade(label="Transform", menu= trs_menu)
        trs_menu.add_command(label="Resize", command= Transform.resize)
        trs_menu.add_command(label="Rotate", command= Transform.rotate)
        trs_menu.add_command(label="Rescale", command= Transform.rescale)
        trs_menu.add_command(label="Swirl", command= Transform.swirl)
        trs_menu.add_command(label="Crop", command= Transform.crop)
        
    def menu_filter(self):
        flt_menu = Menu(self.menu)
        
        self.menu.add_cascade(label="Filter", menu= flt_menu)
        flt_menu.add_command(label="Minimum Threshold", command= Filter.min_thr_filter)
        flt_menu.add_command(label="Otsu Threshold", command= Filter.otsu_thr_filter)
        flt_menu.add_command(label="Bilateral", command= Filter.bilateral_filter)
        flt_menu.add_command(label="Gabor", command= Filter.gabor_filter)
        flt_menu.add_command(label="Gaussian", command= Filter.gaussian_filter)
        flt_menu.add_command(label="Laplace", command= Filter.laplace_filter)
        flt_menu.add_command(label="Prewitt", command= Filter.prewitt_filter)
        flt_menu.add_command(label="Scharr", command= Filter.scharr_filter)
        flt_menu.add_command(label="Sobel", command= Filter.sobel_filter)
    
    def menu_morphology(self):
        morph_menu = Menu(self.menu)
        
        self.menu.add_cascade(label="Morphological", menu= morph_menu)
        morph_menu.add_command(label="Black Tophead", command= Morphology.black_tophead)
        morph_menu.add_command(label="Closing", command= Morphology.closing)
        morph_menu.add_command(label="Convex Hull", command= Morphology.convex_hull)
        morph_menu.add_command(label="Dilation", command= Morphology.dilation)
        morph_menu.add_command(label="Erosion", command= Morphology.erosion)
        morph_menu.add_command(label="Opening", command= Morphology.opening)
        morph_menu.add_command(label="Skeletonize", command=Morphology.skeletonize)
        morph_menu.add_command(label="Square", command= Morphology.square)
        morph_menu.add_command(label="Watershed", command= Morphology.watershed)
        morph_menu.add_command(label="White Tophead", command= Morphology.white_tophead)
    
    def menu_exposure(self):
        exp_menu = Menu(self.menu)
        
        self.menu.add_cascade(label="Exposure", menu= exp_menu)
        exp_menu.add_command(label="Histogram", command= Exposure.show_hist)
        #to be developed
        


root = Tk()
root.title("Image Processing Project 1")
root.geometry("500x200")

#upper side
menu = Menu(root)

window = MainWindow(root, menu)
window.create_menu()
window.create_canvas()



root.config(menu= menu)




root.mainloop()


