#############################################################
#  July 4, 2019
#  Carol Ann Crouse
#  This script reads a gdb and prints out the projection of 
#  each feature class in the gdb.
#############################################################

# import modules
import arcpy

# set workspace
arcpy.env.workspace = r"C:\Working_Files\PYTHON_TESTING\NFF.gdb"

# set up a describe object for each feature class in the gdb
fcList = arcpy.ListFeatureClasses()
for fc in fcList:
	layer = fc
	desc = arcpy.Describe(fc)
	print desc.spatialReference.name,'-', layer
	
print "Script Completed"