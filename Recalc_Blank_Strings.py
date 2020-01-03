import arcpy
import os
from arcpy import env

##################################################################################################
# This code reads a feature class within a GDB, identifies the string fields and changes 
# spaces (" ") and nulls to blanks ("").
# Carol Ann Crouse
# Jan 3, 2020
##################################################################################################
																																			

fc = "C:\\Working_Files\\NULLS_TESTING\\dc.gdb\\test_set_blank"
print fc
print "Processing"

fieldList = [f.name for f in arcpy.ListFields(fc) if f.type == "String"]

for f in fieldList:
    with arcpy.da.UpdateCursor(fc, f) as cursor:
        for row in cursor:
            if row[0] == " ":
                row[0] = ""
            elif row[0] == None:
                row[0] = ""

            cursor.updateRow(row)


