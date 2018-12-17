import os, sys, csv
import arcpy
from arcpy import env  # WHAT DOES THIS DO?
#import xl
#import pandas as pd
    
    
#########################################
# Dec 14, 2018
# This code adds a new field to the GDB
#########################################


ws = "C:\\Working_Files\\Example_Python_Code\\Test_Data_Set.gdb\\"

#Create list of geodatabase layers
layerList = ['VRI_test_set_sm']  

##########################
###### ADD FIELD ########   
##########################

def addFIELD():
   for fc in layerList:
	   outFeaturePath = ws + fc
	   outLayer = fc + "_layer"

	   arcpy.MakeFeatureLayer_management(outFeaturePath, outLayer)

	   print "Adding field"

	   arcpy.AddField_management(outLayer, "STRUC_CODE", "TEXT", "", "", 5)
     arcpy.AddField_management(outLayer, "ASPEN_TOT_VOL", "LONG", "", "", "")
				

addFIELD()

    
    
    
    
