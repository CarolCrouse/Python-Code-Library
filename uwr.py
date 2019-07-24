################################################################
#### Creates a uwr resultant of unique type codes,          ####
#### so that it can be coverted to a coverage.              ####
#### Sarah Lucas, Jan 2014                                  ####  
####                                                        ####
#### The UWR layer must first be formatted.                 #### 
#### Add a field called UWR_NUM = UWR_NUMBER and change the ####
#### values to be u_2_001 instead of u-2-001.  Then drop    ####
#### all other fields.                                      ####   
################################################################
import arcpy
import os
from arcpy import env

print "UWR prep - for coverage conversion"
ws = "C:\\Working_Files\\Arc_Testing\\NewFileGeodatabase.gdb\\"

#Make a layer from the feature class
arcpy.MakeFeatureLayer_management("C:\\Working_Files\\Arc_Testing\\NewFileGeodatabase.gdb\\ungulate", "uwr_layer")

#Use search cursor to list unique values from the vegetation code field
values = [row[0] for row in arcpy.da.SearchCursor("uwr_layer", ("UWR_NUM"))]
uniqueValues = set(values)
print (uniqueValues)

####################################################################################################################

uwrTemp = ws + "uwr_temp"

#Check to see if uwr_temp exists, delete if it does
if arcpy.Exists(uwrTemp):
	print "Deleting existing uwrTemp fc"
	arcpy.Delete_management(uwrTemp)

#Export selected polgyons to new feature class
arcpy.FeatureClassToFeatureClass_conversion("uwr_layer", "C:\\Working_Files\\Arc_Testing\\NewFileGeodatabase.gdb", "uwr_temp")

print "Creating new uwrTemp_layer"
#Make a layer from the feature class
arcpy.MakeFeatureLayer_management("C:\\Working_Files\\Arc_Testing\\NewFileGeodatabase.gdb\\uwr_temp", "uwr_temp_layer")

####################################################################################################################

#define counter
count = 0

#Create new uwr layers based on unique vegetation codes
for uwrType in uniqueValues:
	print "Exporting " + uwrType
	
	#Set uwrType variable
	outFeature = uwrType
	outFeaturePath = ws + outFeature

	#Check to see if seperated uwr layer exists, delete if it does
	if arcpy.Exists(outFeaturePath):
		print "Deleting existing..." + outFeature
		arcpy.Delete_management(outFeaturePath)

	
	#Create new seperated uwr layers
	arcpy.SelectLayerByAttribute_management("uwr_temp_layer", "NEW_SELECTION", " \"UWR_NUM\" = '%s'"%uwrType)

	arcpy.FeatureClassToFeatureClass_conversion("uwr_temp_layer", "C:\\Working_Files\\Arc_Testing\\NewFileGeodatabase.gdb", outFeature)
	
	#Set variables
	fieldName1 = uwrType
	outLayer = uwrType + "_layer"
	outFeaturePath = ws + outFeature

	print "Creating new layer for " + uwrType + " to calculate fields: " + fieldName1
	
	#Make a layer from the feature class
	arcpy.MakeFeatureLayer_management(outFeaturePath, outLayer)
	
	#Calculate new fields, to avoid dropping during overlay
	print "Adding new fields"
	arcpy.AddField_management(outLayer, fieldName1, "TEXT", "", "", 15)


	print "Calculating new fields"
	arcpy.CalculateField_management(outLayer, fieldName1, "!UWR_NUM!", "PYTHON")


	print "Dropping old fields"
	dropFields = "UWR_NUM", "GEOMETRY_Length", "GEOMETRY_Area"
	arcpy.DeleteField_management(outLayer, dropFields)

	print "Overlaying.." + outLayer
	
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
finalUWR = ws + "uwr_final"

#Rename overlayed UWR layers UWR
if arcpy.Exists(finalUWR):
	arcpy.Delete_management(finalUWR)
print "Creating UWR_combined"
arcpy.Rename_management(tmp1, finalUWR)
if arcpy.Exists(tmp2):
	arcpy.Delete_management(tmp2)

##################################################################################################################

