# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 10:15:13 2021

@author: Yoshitomo Yamasaki of Vebots, Hokkaido Univ.
"""

import sys
sys.path.append("D:\\Vebots\\My_master_research\\HSC\\Examples\\lib") #Change the directory according to user
import NH7

#### You have to change the absolute path below ####
path = "D:\\Vebots\\My_master_research\\HSC\\Examples\\sample_data\\For_ReadNH7"

#### If you have changed the filename, you must change the name below ####
filename = "example.nh7"


#### Make an instance of the NH7 file ####
nh7 = NH7.file(path,filename)

#### Read the NH7 file ####
if nh7.read() != False:
            
    #### Show the nh7 data shape ####
    data = nh7.rawdata
    print(data.shape)
    
    #### Make an RGB image array ####
    #### You can change the brightness and the white balance (default: all 1.0) ####
    #### In this case, the values of red, green, blue get 5x by brightness=5,
    #### and then, the red, green and blue get 1x, 2x and 3x, respectively ####
    rgbNdArray = nh7.makeRGBimage(brightness=5,r=1,g=2,b=3)
    
    #### Show the RGB array represented as uint16 ####
    print(rgbNdArray)
    
    #### Show the RGB image ####
    nh7.showRGBimage(imgname="nh7")
    
    #### Save the RGB image ####
    #### You can change imgname and directory ####
    nh7.saveRGBimage(imgname="sample.png",directory=path)
    
    #### Delete nh7 instance ####
    del nh7
    