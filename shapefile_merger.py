'''
A python script to combine shapefiles contained in multiple folders into a single feature class within a gdb

Taylor J Mckeeman 2019
'''
import os
import arcpy
base = "P:/chinook_comfor/fg_19_518_ccf_chinookcf_timber_supply/gis/src/fromTesera/aspect/"


# get a list of the subdirectories 
def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]
			
# move through each subdirectory and create a list of the location and name of each shapefile
folder_list = get_immediate_subdirectories(os.getcwd())
shape_list = []
for item in folder_list:

	print "Working on %s" % (item)
	arcpy.env.workspace = base+item
	arcpy.env.OverwriteOutput = True
	for shapefile in arcpy.ListFeatureClasses():
		shape_list.append(arcpy.env.workspace+"/"+shapefile)
		
print "Merging Final Layer"
arcpy.env.workspace = base[0:-1]
# move through the list of shapefiles and merge them together into the output gdb
arcpy.Merge_management(shape_list, "P:/chinook_comfor/fg_19_518_ccf_chinookcf_timber_supply/gis/src/fromTesera/aspect/Aspect_Combined.gdb/aspect")


