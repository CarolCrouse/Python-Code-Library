####################################################
#### Creates a fire resultant of years codes,   ####
#### so that it can be coverted to a coverage.  ####
#### Sarah Lucas, Jan 2014                      #### 
####################################################
import arcpy
import os
from arcpy import env

print "Fire prep - for coverage conversion"
ws = "C:\\Working_Files\\Arc_Testing\\NewFileGeodatabase.gdb\\"   ###UPDATE LINE###


#Create FIRE layer, list unique fire years

#Make a layer from the feature class
arcpy.MakeFeatureLayer_management("C:\\Working_Files\\Arc_Testing\\NewFileGeodatabase.gdb\\fires", "fire_layer")   ###UPDATE LINE###

##Use search cursor to list unique values from the field fire year
values = [row[0] for row in arcpy.da.SearchCursor("fire_layer", ("FIRE_YEAR"))]
uniqueValues = set(values)
print (uniqueValues)

######################################################################################

#define counter
count = 0

#Create new fire layers based on unique vegetation codes
for fireYear in uniqueValues:
	print "Exporting " + str(fireYear)
	
	#Set fireYear variable
	outFeature = str(fireYear)
	outFeatureName = "fire_" + outFeature
	outFeaturePath = ws + outFeatureName

	#Check to see if seperated fire layer exists, delete if it does
	if arcpy.Exists(outFeaturePath):
		print "Deleting existing..." + outFeature
		arcpy.Delete_management(outFeaturePath)

	whereClause = " \"FIRE_YEAR\" =" + str(fireYear)

	#Create new seperated fire layers
	arcpy.SelectLayerByAttribute_management("fire_layer", "NEW_SELECTION", whereClause)

	arcpy.FeatureClassToFeatureClass_conversion("fire_layer", "C:\\Working_Files\\Arc_Testing\\NewFileGeodatabase.gdb", outFeatureName)   ###UPDATE LINE###

	#Set variables
	fieldName1 = "Fire_" + str(fireYear)
	outLayer = str(fireYear) + "_layer"

        print "Creating new layer for " + outFeature + " to calculate field: " + fieldName1 + " into layer: " + outLayer

	#Make a layer from the feature class
	arcpy.MakeFeatureLayer_management(outFeaturePath, outLayer)
	
	#Calculate new fields, to avoid dropping during overlay
	print "Adding new fields"
	arcpy.AddField_management(outLayer, fieldName1, "LONG", 9, "", "", "refcode", "NULLABLE", "REQUIRED")

	print "Calculating new fields"
	arcpy.CalculateField_management(outLayer, fieldName1, "!FIRE_YEAR!", "PYTHON")

	print "Dropping old fields"
	dropFields = "FIRE_NUMBER", "VERSION_NUMBER", "FIRE_YEAR", "FIRE_CAUSE", "FIRE_SIZE_HECTARES", "SOURCE", "GPS_TRACK_DATE", "LOAD_DATE", "FIRE_DATE", "CREATION_METHOD", "FEATURE_CODE", "FIRELABEL"
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

###########################################################################################

#set final variable
nextFire = ws + "fires_comb"

#Rename overlayed fire layers fires_comb
if arcpy.Exists(nextFire):
	arcpy.Delete_management(nextFire)
print "Creating fires combined"
arcpy.Rename_management(tmp1, nextFire)
if arcpy.Exists(tmp2):
	arcpy.Delete_management(tmp2)

###################################################################################################################


#Add field to fires_comb called recent_fire

combinedLayer = "comb_layer"

fieldName = "RECENT_FIRE"

#Make a layer from the feature class
arcpy.MakeFeatureLayer_management("C:\\Working_Files\\Arc_Testing\\NewFileGeodatabase.gdb\\fires_comb", combinedLayer)   ###UPDATE LINE###

#Calculate new fields, to avoid dropping during overlay
print "Adding new fields"
arcpy.AddField_management(combinedLayer, fieldName, "LONG", 9, "", "", "refcode", "NULLABLE", "REQUIRED")

####################################################################################################################

#Use update cursor to calculate most recent fire year into new field "RECENT_FIRE"

inDB = "C:\\Working_Files\\Arc_Testing\\NewFileGeodatabase.gdb\\fires_comb"   ###UPDATE LINE###

cursor = arcpy.UpdateCursor(inDB)
for row in cursor:
	valLst = []
	for yr in uniqueValues:
		fname = "Fire_"+str(yr)
		fval = row.getValue(fname)
		valLst.append(fval)
	max_value = max(valLst)
	row.setValue("RECENT_FIRE", max_value)

	cursor.updateRow(row)

# Delete cursor and row objects
del cursor, row

# drop fields

fields = arcpy.ListFields(inDB)
print fields
for field in fields:
	fieldName = field.name
	print fieldName
	if fieldName not in ["RECENT_FIRE", "Shape_Area", "Shape_Length", "OBJECTID", "Shape"]:
		arcpy.DeleteField_management(inDB, fieldName)

# delete intermediate layers

#fcList = arcpy.ListFeatureClasses()
#print fcList
#for fc in fcList:
#	print fc
#	if fc not in ["fires_historical", "fires_comb", "fires_current"]:
#		arcpy.Delete_management(fc)







	
