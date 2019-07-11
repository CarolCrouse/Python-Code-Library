#######################################################################################
# This code clips various layers from GDBs to a defined clip layer
#######################################################################################

import arcpy

# identify the output geodatabase
dir = "P:\\HRFN\\nk_17_571_hrf_rsea_srmp_pilot\\gis\\seamless\\resultants\\res1\\seamless"
gdb = dir + "\\seamless.gdb"


# identify the clip layer
fds = gdb
ClipCover = fds + "\\FSJ_TSA_BOUNDARY"

# The following section specifies the each layer being clipped, it's clipped output name 
# and checks whether it already exists in the output GDB.  If it already exists, then
# nothing happens.

# FADM-COMPARTMENTS - clip from basedata
layer = "P:\\basedata\\basedata.gdb\\ADMIN_BOUNDARIES_FADM_REGION_COMPARTMENT" 
name = "compart"
output = fds + "\\" + name
if not arcpy.Exists(fds + "\\" + name):
	arcpy.Clip_analysis(layer,ClipCover,output)


# Sample Plots - clip from basedata
layer = "P:\\basedata\\basedata.gdb\\FOREST_VEGETATION_GRY_PSP_STATUS_ACTIVE" 
name = "samples"
output = fds + "\\" + name
if not arcpy.Exists(fds + "\\" + name):
	arcpy.Clip_analysis(layer,ClipCover,output)

# Ownership - clip from basedata
layer = "P:\\basedata\\basedata.gdb\\FOREST_VEGETATION_F_OWN" 
name = "own"
output = fds + "\\" + name
if not arcpy.Exists(fds + "\\" + name):
	arcpy.Clip_analysis(layer,ClipCover,output)
	
# Rec polygons - clip from basedata
layer = "P:\\basedata\\basedata.gdb\\FTEN_RECREATION_POLY_SVW" 
name = "rec_areas"
output = fds + "\\" + name
if not arcpy.Exists(fds + "\\" + name):
	arcpy.Clip_analysis(layer,ClipCover,output)
	
# Rec lines - clip from basedata
layer = "P:\\basedata\\basedata.gdb\\FTEN_RECREATION_LINES_SVW" 
name = "rec_trails"
output = fds + "\\" + name
if not arcpy.Exists(fds + "\\" + name):
	arcpy.Clip_analysis(layer,ClipCover,output)
	
# Lakes - clip from basedata
layer = "P:\\basedata\\basedata.gdb\\BASEMAPPING_FWA_LAKES_POLY" 
name = "lakes"
output = fds + "\\" + name
if not arcpy.Exists(fds + "\\" + name):
	arcpy.Clip_analysis(layer,ClipCover,output)
	
# Wetlands - clip from basedata
layer = "P:\\basedata\\basedata.gdb\\BASEMAPPING_FWA_WETLANDS_POLY" 
name = "wetlands"
output = fds + "\\" + name
if not arcpy.Exists(fds + "\\" + name):
	arcpy.Clip_analysis(layer,ClipCover,output)