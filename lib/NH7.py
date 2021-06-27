# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 20:07:27 2021

@author: yacht
"""

import os
import numpy as np
import cv2

class file:
    
    def __init__(self,directory,filename):
        
        self.directory = directory
        self.filename = filename
        
        
    def read(self):
        DirExist = os.path.isdir(self.directory)
        if DirExist == False:
            print(self.directory)
            print("Such data path doesn't exist!")
            return False
        
        #Move to target directry and Confirm current directory
        #os.chdir(self.directory)
        #path = os.getcwd()
        #print("current path: %s" % path)
        
        fullpath = self.directory + "\\" +self.filename
        print("nh7 file path: %s" % fullpath)
        
        FileExist = os.path.isfile(fullpath)
        if FileExist == False:
            print("Such file doesn't exist!")
            return False
        
        #Open image files
        file = open(fullpath,'rb') #Read binary data
        dbuf = np.fromfile(file,dtype=np.uint16,count=-1) #Assign the format
        file.close()
        data=dbuf.reshape(1024,151,1280) #Reshape (y,L,x)        
        self.rawdata = np.array(data)
        
        return True
        
        
    def makeRGBimage(self, **kwargs):
        brightness = 1
        r_cor = 1
        g_cor = 1
        b_cor = 1
        
        brightness = kwargs.get("brightness")
        r_cor = kwargs.get("r")
        g_cor = kwargs.get("g")
        b_cor = kwargs.get("b")
        
        #Open image files
        img_list = self.rawdata
        
        r = 70 #700nm
        g = 39 #545nm
        b = 26 #480nm
        
        img_r = img_list[:,r,:]
        img_g = img_list[:,g,:] 
        img_b = img_list[:,b,:] 
    
        reimg_r = img_r.transpose(1,0) *brightness*r_cor #Switch x,y axis
        reimg_g = img_g.transpose(1,0) *brightness*g_cor
        reimg_b = img_b.transpose(1,0) *brightness*b_cor
    
        image_RGB = np.concatenate([[reimg_b],[reimg_g],[reimg_r]]) #Get together r,g,b
        reimage_RGB = image_RGB.transpose(2,1,0)  #Switch y axis for wavelength L
        rereimage_RGB = np.array(reimage_RGB * 16, np.uint16)  #Normalization
        
        result = rereimage_RGB
        self.RGBimg = np.array(result, np.uint16)
        
        return result
    
    def showRGBimage(self, **kwargs):
        imgname = "img"
        imgname = kwargs.get("imgname")
        
        cv2.namedWindow(imgname, cv2.WINDOW_AUTOSIZE)
        cv2.imshow(imgname, self.RGBimg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    def saveRGBimage(self,**kwargs):
        imgname = "sample.png"
        directory = os.getcwd()
        
        imgname = kwargs.get("imgname")
        directory = kwargs.get("directory")
        
        fullpath = directory + "\\" + imgname
        cv2.imwrite(fullpath,self.RGBimg)
        
        

