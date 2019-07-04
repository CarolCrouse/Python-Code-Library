#############################################################
#  Script exports feature classes within a GDB to coverages
#  July 4,2019
#  Carol Ann Crouse
#############################################################

import arcpy
import os
from arcpy import env

env.workspace = "C:\\Working_Files\\PYTHON_TESTING\\NFF.gdb\\"

#Create list of geodatabase layers
layerList = ['lu_n']

# Store input GDB, output directory, tolerance and precision in variables
in_gdb = "C:\\Working_Files\\PYTHON_TESTING\\NFF.gdb\\"
out = "C:\\Working_Files\\PYTHON_TESTING\\"
cTolerance = 0.01
precision = "DOUBLE"

#Convert feature class to coverage
for fc in layerList:
	fc_in = in_gdb + fc
	inCover = [[fc_in, "POLYGON"]]
	outCover = out + fc

	if arcpy.Exists(outCover):
		arcpy.Delete_management(outCover)

	arcpy.FeatureclassToCoverage_conversion(inCover, outCover, cTolerance, precision)
	arcpy.CreateLabels_arc(outCover, "")
