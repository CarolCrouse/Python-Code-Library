########################################## July 4, 2019# Carol Ann Crouse# This script deletes fields within a GDB#########################################import os, sys, csvimport arcpy
from arcpy import env ws = "C:\\Working_Files\\PYTHON_TESTING\\NFF.gdb\\"#Create list of geodatabase layerslayerList = ['lu_n', 'lu_s'] dropfields = ["ASPEN_PERCENT", "BIRCH_PERCENT", "PINE_PERCENT", "FIR_PERCENT", "LARCH_PERCENT", "WILLOW_PERCENT", "SPRUCE_PERCENT", "TOTAL_PERCENT"] ################################### DELETE FIELDS ########   #############################def deleteFIELD():   for fc in layerList:		outFeaturePath = ws + fc		outLayer = fc + "_layer"		arcpy.MakeFeatureLayer_management(outFeaturePath, outLayer)		print "Deleting fields in Layer"		arcpy.DeleteField_management(outLayer, dropfields)				deleteFIELD()                