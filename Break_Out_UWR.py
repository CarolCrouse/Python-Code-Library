############################################################################################################
#### Creates separate layers for unique values in the source data.         
#### In this case a DESCRIPT field identifies the various layers to create (ex.. GRIZZ, SRMZ, CARIB) 
############################################################################################################
import arcpy
import os
from arcpy import env

# SET THE SOURCE LAYER
print "RMP prep - for coverage conversion"
ws = "P:\\babine\\fg_18_176_bab_lakes_tsa_analysis\\gis\\seamless\\rmp_leg.gdb\\"

# MAKE A LAYER FROM THE FEATURE CLASS
arcpy.MakeFeatureLayer_management("P:\\babine\\fg_18_176_bab_lakes_tsa_analysis\\gis\\seamless\\rmp_leg.gdb\\rmp", "rmp_layer")

# USE SEARCH CURSOR TO LIST UNIQUE VALUES FROM THE DESCRIPn code field
values = [row[0] for row in arcpy.da.SearchCursor("rmp_layer", ("DESCRIPT"))]
uniqueValues = set(values)
print (uniqueValues)

####################################################################################################################

rmpTemp = ws + "rmp_temp"

# CHECK TO SEE IF RMP_TEMP EXISTS< DELETE IS IT DOES
if arcpy.Exists(rmpTemp):
	print "Deleting existing rmpTemp fc"
	arcpy.Delete_management(rmpTemp)

# EXPORT SELECTED POLYGONS TO NEW FEATURE CLASS
arcpy.FeatureClassToFeatureClass_conversion("rmp_layer", "P:\\babine\\fg_18_176_bab_lakes_tsa_analysis\\gis\\seamless\\rmp_leg.gdb", "rmp_temp")

print "Creating new uwrTemp_layer"
# MAKE A TEMPORARY LAYER FROM THE FEATURE CLASS
arcpy.MakeFeatureLayer_management("P:\\babine\\fg_18_176_bab_lakes_tsa_analysis\\gis\\seamless\\rmp_leg.gdb\\rmp_temp", "rmp_temp_layer")

####################################################################################################################

#define counter
count = 0

# CREATE NEW RMP LAYERS BASED ON UNIQUE DESCRIPT CODES FROM uniqueValues LIST FROM ABOVE
for rmpType in uniqueValues:
	print "Exporting " + rmpType
	
	#  SET rmpType TO VARIABLE 
	outFeature = rmpType
	outFeaturePath = ws + outFeature

	# CHECK TO SEE IF SEPARATED RMP LAYER EXISTS, DELETE IF IT DOES
	if arcpy.Exists(outFeaturePath):
		print "Deleting existing..." + outFeature
		arcpy.Delete_management(outFeaturePath)

	
	# CREATE NEW SEPARATED RMP LAYERS
	arcpy.SelectLayerByAttribute_management("rmp_temp_layer", "NEW_SELECTION", " \"DESCRIPT\" = '%s'"%rmpType)

	arcpy.FeatureClassToFeatureClass_conversion("rmp_temp_layer", "P:\\babine\\fg_18_176_bab_lakes_tsa_analysis\\gis\\seamless\\rmp_leg.gdb", outFeature)
	
	# SET VARIABLES
	fieldName1 = rmpType
#	fieldName2 = "RMP_" + DESCRIPT
	outLayer = rmpType + "_layer"
	outFeaturePath = ws + outFeature

	print "Creating new layer for " + rmpType + " to calculate fields: " + fieldName1 # + " and " + fieldName2 + " into layer: " + outLayer
	
	# MAKE A LAYER FROM THE FEATURE CLASS
	arcpy.MakeFeatureLayer_management(outFeaturePath, outLayer)
	
	# CALCULATE NEW FIELDS, TO AVOID DROPPING DURING OVERLAY
	print "Adding new fields"
	arcpy.AddField_management(outLayer, fieldName1, "TEXT", "", "", 75)
#	arcpy.AddField_management(outLayer, fieldName2, "TEXT", "", "", 8)

	print "Calculating new fields"
	arcpy.CalculateField_management(outLayer, fieldName1, "!LEGAL_FEAT_OBJECTIVE!", "PYTHON")
#	arcpy.CalculateField_management(outLayer, fieldName2, "[SEED_PLAN_ZONE_VEGETATION_CODE]", "VB")

	print "Dropping old fields"
	dropFields = "LEGAL_FEAT_OBJECTIVE", "DESCRIPT"
	arcpy.DeleteField_management(outLayer, dropFields)

	print "Overlaying.." + outLayer
	
	# UNIONING THE SEPARATED LAYERS TOGETHER
	#Set tmp variables
	tmp1 = ws + "tmp1"
	tmp2 = ws + "tmp2"
	unionFeatures = [outFeaturePath, tmp1]


	if count == 0:
		if arcpy.Exists(tmp1):
			arcpy.Delete_management(tmp1)
		arcpy.CopyFeatures_management(outFeaturePath,tmp1)
	else:
		if arcpy.Exists(tmp2):
			arcpy.Delete_management(tmp2)
		arcpy.Union_analysis(unionFeatures, tmp2, "ALL", 0.01, "NO_GAPS")
		print "Droping tmp1 UID..."
		arcpy.DeleteField_management(tmp2,"FID_TMP1")
		print "Delete..."
		arcpy.Delete_management(tmp1)
		print "Rename..."
		arcpy.Rename_management(tmp2,tmp1)
	
	count += 1

#################################################################################################################

#set final variable
finalUWR = ws + "rmp_final"

#Rename overlayed UWR layers UWR
if arcpy.Exists(finalUWR):
	arcpy.Delete_management(finalUWR)
print "Creating UWR_combined"
arcpy.Rename_management(tmp1, finalUWR)
if arcpy.Exists(tmp2):
	arcpy.Delete_management(tmp2)

##################################################################################################################

