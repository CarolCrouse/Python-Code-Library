import arcpy
import os
from arcpy import env

ws = "C:\\Working_Files\\Example_Python_Code\\Test_Data_Set.gdb\\"


#Create list of geodatabase layers

layerList = ['SOURCE']  # THIS IS THE SOURCE TABLE THAT THE DATA IS BEING JOINED TO

##########################
###### ADD FIELDS ########
##########################

def addFIELD():

	for fc in layerList:

		outFeaturePath = ws + fc
		outLayer = fc + "_layer"

		arcpy.MakeFeatureLayer_management(outFeaturePath, outLayer)

		print "Adding Fields"

		arcpy.AddField_management(outLayer, "STRUC_CODE", "TEXT", "", "", 5)


###########################
###### JOIN TABLES ########
###########################

def addTABLES():

	for fc in layerList:

		print "Joining Tables"

		outFeaturePath = ws + fc
		outLayer = fc + "_layer"

		joinField = "FEATURE_ID"  		# THIS IS THE JOIN FIELD
		cfTable = ws + "JoiningTable"  	# THIS IS THE OTHER TABLE CONTAINING THE JOIN FIELDS


		#arcpy.MakeFeatureLayer_management(outFeaturePath, outLayer)  # IF YOU COMMENT OUT THE "ADD FIELD" STEP ABOVE, MAKE SURE TO UNCOMMENT THIS STEP! YOU WILL NOT HAVE MADE A TEMP LAYER FILE YET!!  

		arcpy.AddJoin_management(outLayer, joinField, cfTable, joinField)

		arcpy.CalculateField_management(outLayer, "STRUC_CODE", "[JoiningTable.STRUC_CODE]", "VB")  # THIS IS THE FIELD MADE ABOOVE WHICH IS HAVING JOINED DATA ADDED TO IT
#		arcpy.CalculateField_management(outLayer, "POLYGON_ID", "[polygon.POLYGON_NUMBER]", "VB")
#		arcpy.CalculateField_management(outLayer, "INVENTORY_STANDARD_CD", "'V'", "PYTHON_9.3")
#		arcpy.CalculateField_management(outLayer, "NON_PRODUCTIVE_DESCRIPTOR_CD", "[polygon.NON_PRODUCTIVE_DESCRIPTOR_CODE]", "VB")

addFIELD()
addTABLES()


