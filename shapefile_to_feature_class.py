###########################################
# May 4, 2020
# Carol Ann Crouse
# This script exports shapefiles to a GDB
###########################################

import os, sys, csv
import arcpy
from arcpy import env 

env.workspace = "C:\\Working_Files\\basedata_downloads\\"
outpath = "P:\\basedata\\ogc.gdb\\"

# Get a list of all the shapefiles in the workspace
layerList = arcpy.ListFeatureClasses()
# Or list the shapfiles in the workspace which are to be exported
#layerList = ['ADMINISTRATIVE_ZONES_PY.shp', 'COMMINGLING_AREAS_PY.shp'] 


###############################
###### EXPORT SHAPEFILES ######   
###############################

for shapes in layerList:	
	
	arcpy.FeatureClassToGeodatabase_conversion(shapes, outpath)
	print "Exporting" + shapes

		