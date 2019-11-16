# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 18:15:48 2019

@author: Melike Mat
"""

from tkinter import Tk, Menu, filedialog, Canvas, NW, Scrollbar, Frame
from ip_project1_classes import Filter, Exposure, Transform, Morphology
from PIL import Image, ImageTk

glb_img = Image.Image()

class FileOperations:
    def __init__(self, root):
        self.root = root
        self.files = [('All Files', '*.*'), ('JPEG', ('*.jpg', '*.jpeg', '*.jpe')), ('PNG Document', '*.png'), ('GIF', '*.gif')]
    
    def open_file(self):
        filename =  filedialog.askopenfilename(initialdir = "/Desktop", title = "Select file", filetypes = self.files)
        return filename
        
    def save_file(self):
        filename =  filedialog.asksaveasfilename(initialdir = "/Desktop", title = "Select file", filetypes = self.files)
        
        if filename:
            glb_img.save(filename)
            
class MainWindow:
    def __init__(self, root, menu):
        self.root = root
        self.menu = menu
        self.canvas = Canvas(self.root)
        
         
    def open_image(self):
        global glb_img
        fops = FileOperations(self)
        
        try:
            glb_img = Image.open(fops.open_file())
            self.photo = ImageTk.PhotoImage(glb_img)
            self.canvas_clear()
            self.canvas_set()
            self.canvas_image(self.photo)
        except:
            return
        
    def save_image(self):
        f_ops = FileOperations(root)
        return f_ops.save_file()
        
    def canvas_image(self, img):
        self.canvas.create_image(0, 0, image= img, anchor=NW)
        
    def canvas_clear(self):
        try:
            self.canvas.delete("all")
        except:
            return
        
    def frame_config(self, ):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
    def canvas_set(self): #tam olmadı
        frame = Frame(self.canvas, bd=2, relief="sunken")
        frame.pack()
        
        xscrollbar = Scrollbar(self.root, orient = "horizontal", command=self.canvas.xview)
        xscrollbar.pack(side = "bottom", fill = "x")
        
        yscrollbar = Scrollbar(self.root, orient = "vertical", command=self.canvas.yview)
        yscrollbar.pack(side = "right", fill = "y")
        
        self.canvas.configure(xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=frame, anchor="nw")  
        frame.bind("<Configure>", lambda event, canvas=self.canvas: self.frame_config())
                
    def create_menu(self):
        self.menu_file()
        self.menu_transform()
        self.menu_filter()
        self.menu_morphology()
        self.menu_exposure()
        
    def menu_file(self):
        file_menu = Menu(self.menu)
        
        self.menu.add_cascade(label="File", menu= file_menu) 
        file_menu.add_command(label="Open", command= self.open_image)
        file_menu.add_command(label="Save", command= self.save_image)
        file_menu.add_separator() 
        file_menu.add_command(label="Exit", command= root.destroy)
        
    def menu_transform(self):
        trs_menu = Menu(self.menu)
        
        self.menu.add_cascade(label="Transform", menu= trs_menu)
        trs_menu.add_command(label="Radon", command= self.cmd_trs_rdn)
        trs_menu.add_command(label="Resize", command= self.cmd_trs_rsz)
        trs_menu.add_command(label="Rotate", command= self.cmd_trs_rtt)
        trs_menu.add_command(label="Rescale", command= self.cmd_trs_rscl)
        trs_menu.add_command(label="Swirl", command= self.cmd_trs_swirl)
        
    def menu_filter(self):
        flt_menu = Menu(self.menu)
        
        self.menu.add_cascade(label="Filter", menu= flt_menu)
        flt_menu.add_command(label="Bilateral", command= self.cmd_flt_bil)
        flt_menu.add_command(label="Gabor", command= self.cmd_flt_gabor)
        flt_menu.add_command(label="Gaussian", command= self.cmd_flt_gaussian)
        flt_menu.add_command(label="Laplace", command= self.cmd_flt_laplace)
        flt_menu.add_command(label="Minimum Threshold", command= self.cmd_flt_minthr)
        flt_menu.add_command(label="Otsu Threshold 1", command= self.cmd_flt_otsu1thr)
        flt_menu.add_command(label="Otsu Threshold 2", command= self.cmd_flt_otsu2thr)
        flt_menu.add_command(label="Prewitt", command= self.cmd_flt_prewitt)
        flt_menu.add_command(label="Scharr", command= self.cmd_flt_scharr)
        flt_menu.add_command(label="Sobel", command= self.cmd_flt_sobel)
    
    def menu_morphology(self):
        morph_menu = Menu(self.menu)
        
        self.menu.add_cascade(label="Morphological", menu= morph_menu)
        morph_menu.add_command(label="Black Tophead", command= self.cmd_mrph_blctop)
        morph_menu.add_command(label="Closing", command= self.cmd_mrph_cls)
        morph_menu.add_command(label="Convex Hull", command= self.cmd_mrph_cvx)
        morph_menu.add_command(label="Dilation", command= self.cmd_mrph_dlt)
        morph_menu.add_command(label="Erosion", command= self.cmd_mrph_ers)
        morph_menu.add_command(label="Opening", command= self.cmd_mrph_opn)
        morph_menu.add_command(label="Skeletonize", command= self.cmd_mrph_sklt)
        morph_menu.add_command(label="Square", command= self.cmd_mrph_sqr)
        morph_menu.add_command(label="Watershed", command= self.cmd_mrph_wtr)
        morph_menu.add_command(label="White Tophead", command= self.cmd_mrph_whttop)
    
    def menu_exposure(self):
        exp_menu = Menu(self.menu)
        
        self.menu.add_cascade(label="Exposure", menu= exp_menu)
        exp_menu.add_command(label="Histogram", command= self.cmd_exp_hist)
        exp_menu.add_command(label="Equalize Histogram", command= self.cmd_exp_eqhist)
        exp_menu.add_command(label="Rescale Intensity", command= self.cmd_exp_rscl)
         
    #command functions block 
    #filter process commands
    def cmd_flt_bil(self):
        self.img = Filter(glb_img).bilateral_filter()
        return self.canvas_image(self.img)
    
    def cmd_flt_gabor(self):
        self.img = Filter(glb_img).gabor_filter()
        return self.canvas_image(self.img)
    
    def cmd_flt_gaussian(self):
        self.img = Filter(glb_img).gaussian_filter()
        return self.canvas_image(self.img)
        
    def cmd_flt_laplace(self):
        self.img = Filter(glb_img).laplace_filter()
        return self.canvas_image(self.img)
    
    def cmd_flt_minthr(self):
        self.img = Filter(glb_img).min_thr_filter()
        return self.canvas_image(self.img)
    
    def cmd_flt_otsu1thr(self):
        self.img = Filter(glb_img).otsu1_thr_filter()
        return self.canvas_image(self.img)
    
    def cmd_flt_otsu2thr(self):
        self.img = Filter(glb_img).otsu2_thr_filter()
        return self.canvas_image(self.img)
    
    def cmd_flt_prewitt(self):
        self.img = Filter(glb_img).prewitt_filter()
        return self.canvas_image(self.img)
    
    def cmd_flt_scharr(self):
        self.img = Filter(glb_img).scharr_filter()
        return self.canvas_image(self.img)
    
    def cmd_flt_sobel(self):
        self.img = Filter(glb_img).sobel_filter()
        return self.canvas_image(self.img)
    
    #morphological process commands
    def cmd_mrph_blctop(self):
        self.img = Morphology(glb_img).black_tophead()
        return self.canvas_image(self.img)
    
    def cmd_mrph_whttop(self):
        self.img = Morphology(glb_img).white_tophat()
        return self.canvas_image(self.img)
    
    def cmd_mrph_cls(self):
        self.img = Morphology(glb_img).closing()
        return self.canvas_image(self.img)
    
    def cmd_mrph_cvx(self):
        self.img = Morphology(glb_img).convex_hull()
        return self.canvas_image(self.img)
    
    def cmd_mrph_dlt(self):
        self.img = Morphology(glb_img).dilation()
        return self.canvas_image(self.img)
    
    def cmd_mrph_ers(self):
        self.img = Morphology(glb_img).erosion()
        return self.canvas_image(self.img)
    
    def cmd_mrph_opn(self):
        self.img = Morphology(glb_img).opening()
        return self.canvas_image(self.img)
    
    def cmd_mrph_sklt(self):
        self.img = Morphology(glb_img).skeletonize()
        return self.canvas_image(self.img)
    
    def cmd_mrph_sqr(self):
        self.img = Morphology(glb_img).square()
        return self.canvas_image(self.img)
    
    def cmd_mrph_wtr(self):
        self.img = Morphology(glb_img).watershed()
        return self.canvas_image(self.img)
    
    #exposure process commands
    def cmd_exp_hist(self):
        self.img = Exposure(glb_img).show_hist()
        return self.canvas_image(self.img)
    
    def cmd_exp_eqhist(self):
        self.img = Exposure(glb_img).eq_hist()
        return self.canvas_image(self.img)
    
    def cmd_exp_rscl(self):
        self.img = Exposure(glb_img).rescale_intensity()
        return self.canvas_image(self.img)
    
    #transform process commands
    def cmd_trs_rsz(self):
        self.img = Transform(glb_img).resize()
        return self.canvas_image(self.img)
    
    def cmd_trs_rtt(self):
        self.img = Transform(glb_img).rotate()
        return self.canvas_image(self.img)
    
    def cmd_trs_rscl(self):
        self.img = Transform(glb_img).rescale()
        return self.canvas_image(self.img)
    
    def cmd_trs_swirl(self):
        self.img = Transform(glb_img).swirl()
        return self.canvas_image(self.img)
    
    def cmd_trs_rdn(self):
        self.img = Transform(glb_img).radon()
        return self.canvas_image(self.img)
        
root = Tk()
root.title("Image Processing Project 1")

menu = Menu(root)

window = MainWindow(root, menu)
window.create_menu()

root.config(menu= menu)

root.mainloop()
