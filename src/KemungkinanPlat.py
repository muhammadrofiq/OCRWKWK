# PossiblePlate.py

import cv2
import numpy as np

###################################################################################################
class KemungkinanPlat:

    # constructor #################################################################################
    def __init__(self, plat,x,y,w,h):
        self.imgPlate = plat
        self.imgGrayscale = None
        self.imgThresh = None
        self.intArea = w*h
        self.intLokasiX = x
        self.intLokasiY = y
        self.Lebar = w
        self.Tinggi = h

        self.rrLocationOfPlateInScene = None

        self.strChars = ""
    # end constructor

# end class
