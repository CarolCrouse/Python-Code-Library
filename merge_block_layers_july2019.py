'''
A python script to normalize block fields so they don't overlap
** THIS CODE WILL MODIFY INPUT FEATURE CLASSES***
Taylor J Mckeeman 2019
'''

import arcpy
arcpy.env.workspace = "C:\\Working_Files\\Arc_Testing\\NewFileGeodatabase.gdb"

#Define field matrix
# [[layer_name, forest_file_id, harvest_start_date, harvest_start_status, harvest_completion_date, harvest_completion_status, reserves], etc...]
layer_matrix = [["rslt_op", "FOREST_FILE_ID", "DISTURBANCE_START_DATE", "OPENING_STATUS_CODE", "DISTURBANCE_END_DATE", "rs_"],

				["ften_cb", "CUT_BLOCK_FOREST_FILE_ID", "DISTURBANCE_START_DATE", "BLOCK_STATUS_CODE", "DISTURBANCE_END_DATE", "ft_"]]
				

short_fields = ["", "FFID", "DSTDT", "ST_STAT", "DENDT"]

#******** BEGIN FUNCTION SPACE *******

#******** END FUNCTION SPACE *******


#******** BEGIN EXECUTABLES *******
for layer in layer_matrix:
	lyrname = layer[0]  # this is the layer name at the first position in the matrix
	print "Processing layer %s" % (lyrname)
	
	for x in range(1,len(layer)-1):   # this reads the values in the matrix from position 1 to the 2nd last position
		if layer[x] == "":
			pass
		else:
			arcpy.AlterField_management(lyrname, layer[x], layer[-1] + short_fields[x])   # this renames the fields to be the last position value & the short field name
			
print "Performing Union..."
arcpy.Union_analysis(["rslt_op", "ften_cb"], "unioned_blocks", cluster_tolerance = 0.1)
print "\n\n***DONE***"
#******** END EXECUTABLES *******