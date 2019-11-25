###########################################################################################
# Resultant_GRID_CODE.py
# This code calcualates the percent slope based on the BC DEM for a defined study area.
# It then calculates the MEAN slope for each UNIQUE_ID in a defined resultant and outputs
# the results to a table using Zonal Statistics.  The table is then updated with GRID_CODE 
# which defines 10% slope classes.
# Author:  Carol Ann Crouse
# Date: Nov 2019
###########################################################################################


import arcpy
import os
from arcpy import env
from arcpy.sa import *


# set workspace
arcpy.env.workspace = r"C:\\Working_Files\\SLOPE_CLASS_TESTING\\"  # ENTER THE WORKSPACE
print "workspace is C:\\Working_Files\\SLOPE_CLASS_TESTING\\"		


bcdem = "P:\\basedata\\dem\\dembc.gdb\\bc_dem"		# ENTER THE LOCATION OF THE DEM
clp = "P:\\canfor\\KE-13-053-CFP_Morice_TSR_Review\\gis\\resultant_2019\\seamless\\Data.gdb\\bdy\\"		# ENTER THE LOCATION OF THE STUDY AREA


# CLIP THE DEM
print "Clipping the DEM"
arcpy.Clip_management(bcdem, "#", "dem", clp, "0", "ClippingGeometry", "#")


# RUN THE SLOPE TOOL
# Check out the ArcGIS Spatial Analyst extension license
print "Running SLOPE Tool"
arcpy.CheckOutExtension("Spatial")
# Execute Slope
outSlope = Slope("dem", "PERCENT_RISE", "#")
# Save the output 
outSlope.save("slp_pct")


# RUN THE ZONAL STATISTICS TOOL
# Set local variables
print "Running ZONAL STATISTICS Tool"
resultant = "P:\\canfor\\KE-13-053-CFP_Morice_TSR_Review\\gis\\resultant_2019\\overlays\\Resultant.gdb\\res_21nov2019_elim_lt1000"
zoneField = "UNIQUE_ID"
# Execute ZonalStatistics
outZSaT = ZonalStatisticsAsTable(resultant, zoneField, "slp_pct", "slp_pct_mean_table", "DATA", "MEAN")


# ADD THE FIELD GRID_CODE
print "Adding Field GRID_CODE"
arcpy.AddField_management("slp_pct_mean_table", "GRID_CODE", "SHORT", 5)


# UPDATE THE GRID_CODE CLASSES
print "Updating the Slope Classes"
outlayer = "slp_pct_mean_table"


rows = arcpy.UpdateCursor(outlayer)  #this updates the output feature class
											 
for row in rows:
	if row.MEAN <=10:
		row.GRID_CODE = 1
		rows.updateRow(row)
	elif row.MEAN >10 and row.MEAN <=20:
		row.GRID_CODE = 2
		rows.updateRow(row)
	elif row.MEAN >20 and row.MEAN <=30:
		row.GRID_CODE = 3
		rows.updateRow(row)
	elif row.MEAN >30 and row.MEAN <=40:
		row.GRID_CODE = 4
		rows.updateRow(row)
	elif row.MEAN >40 and row.MEAN <=50:
		row.GRID_CODE = 5
		rows.updateRow(row)
	elif row.MEAN >50 and row.MEAN <=60:
		row.GRID_CODE = 6
		rows.updateRow(row)
	elif row.MEAN >60 and row.MEAN <=70:
		row.GRID_CODE = 7
		rows.updateRow(row)
	elif row.MEAN >70 and row.MEAN <=80:
		row.GRID_CODE = 8
		rows.updateRow(row)
	elif row.MEAN >80 and row.MEAN <=90:
		row.GRID_CODE = 9
		rows.updateRow(row)
	elif row.MEAN >90:
		row.GRID_CODE = 10
		rows.updateRow(row)

	
del row
del rows