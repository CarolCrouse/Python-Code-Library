import arcpy
import os
from arcpy import env

ws = "C:\\Working_Files\\temp\\heals_rifle_flatfile_test.gdb\\"


#Create list of geodatabase layers

layerList = ['delin']



#############################################
### Calculate Stand Percentage Dead #########
#############################################

def addDeadPer():

	for fc in layerList:

		outFeaturePath = ws + fc
		outLayer = fc + "_layer"

		arcpy.MakeFeatureLayer_management(outFeaturePath, outLayer)

		rows = arcpy.UpdateCursor(outLayer)

		for row in rows:
			if row.L1_VRI_DEAD_STEMS_PER_HA == None:
				print row.L1_VRI_DEAD_STEMS_PER_HA
				row.L1_VRI_DEAD_STEMS_PER_HA = 0
				rows.updateRow(row)
		del row
		del rows

		rows = arcpy.UpdateCursor(outLayer)

		for row in rows:
			if row.L1_VRI_LIVE_STEMS_PER_HA == None:
				print row.L1_VRI_LIVE_STEMS_PER_HA
				row.L1_VRI_LIVE_STEMS_PER_HA = 0
				rows.updateRow(row)
		del row
		del rows

		rows = arcpy.UpdateCursor(outLayer)

		for row in rows:
			if row.L1_VRI_DEAD_STEMS_PER_HA != 0:
				stand_tot = row.L1_VRI_LIVE_STEMS_PER_HA + row.L1_VRI_DEAD_STEMS_PER_HA
				print stand_tot
				stand_per = float(row.L1_VRI_DEAD_STEMS_PER_HA) / float(stand_tot)
				stand_per2 = float(stand_per) * 100
				row.STAND_PERCENTAGE_DEAD = float(stand_per2)
				rows.updateRow(row)
		del row
		del rows

#############################################
### Calculate Crown Closure Class   #########
#############################################

def addCC():

	for fc in layerList: #layerList is the feature class [delin] within the open gdb

		outFeaturePath = ws + fc  #this is "P:\\nrcan\\nv_18_626_nrc_tem_vri_updates_2018\\gis\\gis\\seamless\\heals_rifle_flatfile.gdb\\" + fc
		outLayer = fc + "_layer"  #this sets the output feature class layer to be fc & "_layer" 

#		arcpy.MakeFeatureLayer_management(outFeaturePath, outLayer)

		rows = arcpy.UpdateCursor(outLayer)  #this updates the output feature class
											 #arcpy function that creates a cursor that lets you update or delete rows on the specified feature class, shapefile, or table. 
											 #The cursor places a lock on the data that will remain until either the script completes or the update cursor object is deleted.

		for row in rows:   #this goes through the records
			if row.L1_CROWN_CLOSURE <= 5:
				row.L1_CROWN_CLOSURE_CLASS_CD = 0
				rows.updateRow(row)
			if row.L1_CROWN_CLOSURE > 5 and row.L1_CROWN_CLOSURE <= 15:
				row.L1_CROWN_CLOSURE_CLASS_CD = 1
				rows.updateRow(row)
			if row.L1_CROWN_CLOSURE > 15 and row.L1_CROWN_CLOSURE <= 25:
				row.L1_CROWN_CLOSURE_CLASS_CD = 2
				rows.updateRow(row)
			if row.L1_CROWN_CLOSURE > 25 and row.L1_CROWN_CLOSURE <= 35:
				row.L1_CROWN_CLOSURE_CLASS_CD = 3
				rows.updateRow(row)
			if row.L1_CROWN_CLOSURE > 35 and row.L1_CROWN_CLOSURE <= 45:
				row.L1_CROWN_CLOSURE_CLASS_CD = 4
				rows.updateRow(row)
			if row.L1_CROWN_CLOSURE > 45 and row.L1_CROWN_CLOSURE <= 55:
				row.L1_CROWN_CLOSURE_CLASS_CD = 5
				rows.updateRow(row)
			if row.L1_CROWN_CLOSURE > 55 and row.L1_CROWN_CLOSURE <= 65:
				row.L1_CROWN_CLOSURE_CLASS_CD = 6
				rows.updateRow(row)
			if row.L1_CROWN_CLOSURE > 65 and row.L1_CROWN_CLOSURE <= 75:
				row.L1_CROWN_CLOSURE_CLASS_CD = 7
				rows.updateRow(row)
			if row.L1_CROWN_CLOSURE > 75 and row.L1_CROWN_CLOSURE <= 85:
				row.L1_CROWN_CLOSURE_CLASS_CD = 8
				rows.updateRow(row)
			if row.L1_CROWN_CLOSURE > 85 and row.L1_CROWN_CLOSURE <= 95:
				row.L1_CROWN_CLOSURE_CLASS_CD = 9
				rows.updateRow(row)
			if row.L1_CROWN_CLOSURE > 95:
				row.L1_CROWN_CLOSURE_CLASS_CD = 10
				rows.updateRow(row)
		del row
		del rows


#################################
### Calculate Age CLASS #########
#################################

def addAGE():

	for fc in layerList:

		outFeaturePath = ws + fc
		outLayer = fc + "_layer"

#		arcpy.MakeFeatureLayer_management(outFeaturePath, outLayer)

		rows = arcpy.UpdateCursor(outLayer)

		for row in rows:
			if row.L1_INV_AGE_1 == 0:
				row.L1_INV_AGE_CLASS_CD_1 = 0
				rows.updateRow(row)
			if row.L1_INV_AGE_1 > 0 and row.L1_INV_AGE_1 <= 20:
				row.L1_INV_AGE_CLASS_CD_1 = 1
				rows.updateRow(row)
			if row.L1_INV_AGE_1 > 20 and row.L1_INV_AGE_1 <= 40:
				row.L1_INV_AGE_CLASS_CD_1 = 2
				rows.updateRow(row)
			if row.L1_INV_AGE_1 > 40 and row.L1_INV_AGE_1 <= 60:
				row.L1_INV_AGE_CLASS_CD_1 = 3
				rows.updateRow(row)
			if row.L1_INV_AGE_1 > 60 and row.L1_INV_AGE_1 <= 80:
				row.L1_INV_AGE_CLASS_CD_1 = 4
				rows.updateRow(row)
			if row.L1_INV_AGE_1 > 80 and row.L1_INV_AGE_1 <= 100:
				row.L1_INV_AGE_CLASS_CD_1 = 5
				rows.updateRow(row)
			if row.L1_INV_AGE_1 > 100 and row.L1_INV_AGE_1 <= 120:
				row.L1_INV_AGE_CLASS_CD_1 = 6
				rows.updateRow(row)
			if row.L1_INV_AGE_1 > 120 and row.L1_INV_AGE_1 <= 140:
				row.L1_INV_AGE_CLASS_CD_1 = 7
				rows.updateRow(row)
			if row.L1_INV_AGE_1 > 140 and row.L1_INV_AGE_1 <= 250:
				row.L1_INV_AGE_CLASS_CD_1 = 8
				rows.updateRow(row)
			if row.L1_INV_AGE_1 > 250:
				row.L1_INV_AGE_CLASS_CD_1 = 9
				rows.updateRow(row)
		del row
		del rows


		rows = arcpy.UpdateCursor(outLayer)

		for row in rows:
			if row.L1_INV_AGE_2 == 0:
				row.L1_INV_AGE_CLASS_CD_2 = 0
				rows.updateRow(row)
			if row.L1_INV_AGE_2 > 0 and row.L1_INV_AGE_2 <= 20:
				row.L1_INV_AGE_CLASS_CD_2 = 1
				rows.updateRow(row)
			if row.L1_INV_AGE_2 > 20 and row.L1_INV_AGE_2 <= 40:
				row.L1_INV_AGE_CLASS_CD_2 = 2
				rows.updateRow(row)
			if row.L1_INV_AGE_2 > 40 and row.L1_INV_AGE_2 <= 60:
				row.L1_INV_AGE_CLASS_CD_2 = 3
				rows.updateRow(row)
			if row.L1_INV_AGE_2 > 60 and row.L1_INV_AGE_2 <= 80:
				row.L1_INV_AGE_CLASS_CD_2 = 4
				rows.updateRow(row)
			if row.L1_INV_AGE_2 > 80 and row.L1_INV_AGE_2 <= 100:
				row.L1_INV_AGE_CLASS_CD_2 = 5
				rows.updateRow(row)
			if row.L1_INV_AGE_2 > 100 and row.L1_INV_AGE_2 <= 120:
				row.L1_INV_AGE_CLASS_CD_2 = 6
				rows.updateRow(row)
			if row.L1_INV_AGE_2 > 120 and row.L1_INV_AGE_2 <= 140:
				row.L1_INV_AGE_CLASS_CD_2 = 7
				rows.updateRow(row)
			if row.L1_INV_AGE_2 > 140 and row.L1_INV_AGE_2 <= 250:
				row.L1_INV_AGE_CLASS_CD_2 = 8
				rows.updateRow(row)
			if row.L1_INV_AGE_2 > 250:
				row.L1_INV_AGE_CLASS_CD_2 = 9
				rows.updateRow(row)
		del row
		del rows


		rows = arcpy.UpdateCursor(outLayer)

		for row in rows:
			if row.L1_PROJ_AGE == 0:
				row.L1_PROJ_AGE_CLASS_CD = 0
				rows.updateRow(row)
			if row.L1_PROJ_AGE > 0 and row.L1_PROJ_AGE <= 20:
				row.L1_PROJ_AGE_CLASS_CD = 1
				rows.updateRow(row)
			if row.L1_PROJ_AGE > 20 and row.L1_PROJ_AGE <= 40:
				row.L1_PROJ_AGE_CLASS_CD = 2
				rows.updateRow(row)
			if row.L1_PROJ_AGE > 40 and row.L1_PROJ_AGE <= 60:
				row.L1_PROJ_AGE_CLASS_CD = 3
				rows.updateRow(row)
			if row.L1_PROJ_AGE > 60 and row.L1_PROJ_AGE <= 80:
				row.L1_PROJ_AGE_CLASS_CD = 4
				rows.updateRow(row)
			if row.L1_PROJ_AGE > 80 and row.L1_PROJ_AGE <= 100:
				row.L1_PROJ_AGE_CLASS_CD = 5
				rows.updateRow(row)
			if row.L1_PROJ_AGE > 100 and row.L1_PROJ_AGE <= 120:
				row.L1_PROJ_AGE_CLASS_CD = 6
				rows.updateRow(row)
			if row.L1_PROJ_AGE > 120 and row.L1_PROJ_AGE <= 140:
				row.L1_PROJ_AGE_CLASS_CD = 7
				rows.updateRow(row)
			if row.L1_PROJ_AGE > 140 and row.L1_PROJ_AGE <= 250:
				row.L1_PROJ_AGE_CLASS_CD = 8
				rows.updateRow(row)
			if row.L1_PROJ_AGE > 250:
				row.L1_PROJ_AGE_CLASS_CD = 9
				rows.updateRow(row)
		del row
		del rows


####################################
### Calculate Height Class #########
####################################


def addHEIGHT():

	for fc in layerList:

		outFeaturePath = ws + fc
		outLayer = fc + "_layer"

	#	arcpy.MakeFeatureLayer_management(outFeaturePath, outLayer)

		rows = arcpy.UpdateCursor(outLayer)

		for row in rows:

			if row.L1_INV_HEIGHT_1 == 0:
				row.L1_INV_HEIGHT_CLASS_CD_1 = 0
				rows.updateRow(row)
			if row.L1_INV_HEIGHT_1 > 0 and row.L1_INV_HEIGHT_1 <= 10.4:
				row.L1_INV_HEIGHT_CLASS_CD_1 = 1
				rows.updateRow(row)
			if row.L1_INV_HEIGHT_1 > 10.4 and row.L1_INV_HEIGHT_1 <= 19.4:
				row.L1_INV_HEIGHT_CLASS_CD_1 = 2
				rows.updateRow(row)
			if row.L1_INV_HEIGHT_1 > 19.4 and row.L1_INV_HEIGHT_1 <= 28.4:
				row.L1_INV_HEIGHT_CLASS_CD_1 = 3
				rows.updateRow(row)
			if row.L1_INV_HEIGHT_1 > 28.4 and row.L1_INV_HEIGHT_1 <= 37.4:
				row.L1_INV_HEIGHT_CLASS_CD_1 = 4
				rows.updateRow(row)
			if row.L1_INV_HEIGHT_1 > 37.4 and row.L1_INV_HEIGHT_1 <= 46.4:
				row.L1_INV_HEIGHT_CLASS_CD_1 = 5
				rows.updateRow(row)
			if row.L1_INV_HEIGHT_1 > 46.4 and row.L1_INV_HEIGHT_1 <= 55.4:
				row.L1_INV_HEIGHT_CLASS_CD_1 = 6
				rows.updateRow(row)
			if row.L1_INV_HEIGHT_1 > 55.4 and row.L1_INV_HEIGHT_1 <= 64.4:
				row.L1_INV_HEIGHT_CLASS_CD_1 = 7
				rows.updateRow(row)
			if row.L1_INV_HEIGHT_1 > 64.4:
				row.L1_INV_HEIGHT_CLASS_CD_1 = 8
				rows.updateRow(row)
		del row
		del rows

		rows = arcpy.UpdateCursor(outLayer)

		for row in rows:

			if row.L1_INV_HEIGHT_2 == 0:
				row.L1_INV_HEIGHT_CLASS_CD_2 = 0
				rows.updateRow(row)
			if row.L1_INV_HEIGHT_2 > 0 and row.L1_INV_HEIGHT_2 <= 10.4:
				row.L1_INV_HEIGHT_CLASS_CD_2 = 1
				rows.updateRow(row)
			if row.L1_INV_HEIGHT_2 > 10.4 and row.L1_INV_HEIGHT_2 <= 19.4:
				row.L1_INV_HEIGHT_CLASS_CD_2 = 2
				rows.updateRow(row)
			if row.L1_INV_HEIGHT_2 > 19.4 and row.L1_INV_HEIGHT_2 <= 28.4:
				row.L1_INV_HEIGHT_CLASS_CD_2 = 3
				rows.updateRow(row)
			if row.L1_INV_HEIGHT_2 > 28.4 and row.L1_INV_HEIGHT_2 <= 37.4:
				row.L1_INV_HEIGHT_CLASS_CD_2 = 4
				rows.updateRow(row)
			if row.L1_INV_HEIGHT_2 > 37.4 and row.L1_INV_HEIGHT_2 <= 46.4:
				row.L1_INV_HEIGHT_CLASS_CD_2 = 5
				rows.updateRow(row)
			if row.L1_INV_HEIGHT_2 > 46.4 and row.L1_INV_HEIGHT_2 <= 55.4:
				row.L1_INV_HEIGHT_CLASS_CD_2 = 6
				rows.updateRow(row)
			if row.L1_INV_HEIGHT_2 > 55.4 and row.L1_INV_HEIGHT_2 <= 64.4:
				row.L1_INV_HEIGHT_CLASS_CD_2 = 7
				rows.updateRow(row)
			if row.L1_INV_HEIGHT_2 > 64.4:
				row.L1_INV_HEIGHT_CLASS_CD_2 = 8
				rows.updateRow(row)
		del row
		del rows

		rows = arcpy.UpdateCursor(outLayer)

		for row in rows:

			if row.L1_PROJ_HEIGHT == 0:
				row.L1_PROJ_HEIGHT_CLASS_CD = 0
				rows.updateRow(row)
			if row.L1_PROJ_HEIGHT > 0 and row.L1_PROJ_HEIGHT <= 10.4:
				row.L1_PROJ_HEIGHT_CLASS_CD = 1
				rows.updateRow(row)
			if row.L1_PROJ_HEIGHT > 10.4 and row.L1_PROJ_HEIGHT <= 19.4:
				row.L1_PROJ_HEIGHT_CLASS_CD = 2
				rows.updateRow(row)
			if row.L1_PROJ_HEIGHT > 19.4 and row.L1_PROJ_HEIGHT <= 28.4:
				row.L1_PROJ_HEIGHT_CLASS_CD = 3
				rows.updateRow(row)
			if row.L1_PROJ_HEIGHT > 28.4 and row.L1_PROJ_HEIGHT <= 37.4:
				row.L1_PROJ_HEIGHT_CLASS_CD = 4
				rows.updateRow(row)
			if row.L1_PROJ_HEIGHT > 37.4 and row.L1_PROJ_HEIGHT <= 46.4:
				row.L1_PROJ_HEIGHT_CLASS_CD = 5
				rows.updateRow(row)
			if row.L1_PROJ_HEIGHT > 46.4 and row.L1_PROJ_HEIGHT <= 55.4:
				row.L1_PROJ_HEIGHT_CLASS_CD = 6
				rows.updateRow(row)
			if row.L1_PROJ_HEIGHT > 55.4 and row.L1_PROJ_HEIGHT <= 64.4:
				row.L1_PROJ_HEIGHT_CLASS_CD = 7
				rows.updateRow(row)
			if row.L1_PROJ_HEIGHT > 64.4:
				row.L1_PROJ_HEIGHT_CLASS_CD = 8
				rows.updateRow(row)
		del row
		del rows

################################################
###### CALCULATE FOREST COVER RANK CODE ########
################################################

def addRANK():

	for fc in layerList:

		outFeaturePath = ws + fc
		outLayer = fc + "_layer"

#	arcpy.MakeFeatureLayer_management(outFeaturePath, outLayer)

		rows = arcpy.UpdateCursor(outLayer)

		for row in rows:
			if row.L1_LIVE_STAND_VOLUME_125 > row.L2_LIVE_STAND_VOLUME_125:
				row.L1_FOR_COVER_RANK_CD = 1
				rows.updateRow(row)
				if row.L2_LAYER_ID == 2:
					row.L2_FOR_COVER_RANK_CD = 2
					rows.updateRow(row)
			if row.L2_LIVE_STAND_VOLUME_125 > row.L1_LIVE_STAND_VOLUME_125:
				row.L2_FOR_COVER_RANK_CD = 1
				row.L1_FOR_COVER_RANK_CD = 2
				rows.updateRow(row)
		del row
		del rows



addDeadPer()
addCC()
addAGE()
addHEIGHT()
#addRANK()
