import arcpy
import os
from arcpy import env

##################################################################################################
# This code clips the Canfor, Results and FTEN cutblocks for each area.
# Carol Ann Crouse
# Jan 8, 2020
##################################################################################################

########################################
# READ THE SOURCE CUTBLOCK LAYERS
########################################

cfp = "P:\\canfor\\ke14033cfp_provincial_fibre_flow\\gis\\seamless\\winter2020\\Cutblocks_2020\\Canfor_Cutblocks\\CANFOR_Cutblocks.gdb\\CANFOR_cutblocks_elim2"
ften = "P:\\canfor\\ke14033cfp_provincial_fibre_flow\\gis\\seamless\\winter2020\\Cutblocks_2020\\FTEN_Cutblocks\\FTEN_Cutblocks.gdb\\FTEN_Blocks_elim2"
rslt = "P:\\canfor\\ke14033cfp_provincial_fibre_flow\\gis\\seamless\\winter2020\\Cutblocks_2020\\Results_Cutblocks_North\\RESULTS_Cutblocks_N.gdb\\RESULTS_Blocks_N_elim2"


#############################################################################
# THIS EXAMPLE DELETES ALL THE EXISTING CLIPPED LAYERS AND PRODUCES NEW ONES
#############################################################################
def t18():

	print "t18"
	arcpy.env.workspace = "C:\\Working_Files\\CANFOR_TEST\\t18\\seamless\\t18.gdb"

	bdy = "P:\\canfor\\ke14033cfp_provincial_fibre_flow\\gis\\seamless\\winter2020\\t18\\seamless\\t18.gdb\\t18"
	
	layerList = ["cfp_blks", "ften_blks", "rslt_blks"]
	for fc in layerList:
		if arcpy.Exists(fc):
			arcpy.Delete_management(fc)
	
	arcpy.Clip_analysis(cfp, bdy, "cfp_blks")
	arcpy.Clip_analysis(ften, bdy, "ften_blks")
	arcpy.Clip_analysis(rslt, bdy, "rslt_blks")
	
	print "Clipped Cutblocks T18"


#########################################################################
# THESE EXAMPLES ONLY PERFORM THE CLIP IF THE LAYER DOESN"T ALREADY EXIST
#########################################################################
def t18v2():

	print "t18"
	arcpy.env.workspace = "C:\\Working_Files\\CANFOR_TEST\\t18\\seamless\\t18.gdb"

	bdy = "P:\\canfor\\ke14033cfp_provincial_fibre_flow\\gis\\seamless\\winter2020\\t18\\seamless\\t18.gdb\\t18"
	
	layerList = ["cfp_blks", "ften_blks", "rslt_blks"]
	
	if not arcpy.Exists(layerList[0]):
		arcpy.Clip_analysis(cfp, bdy, "cfp_blks")
	elif not arcpy.Exists(layerList[1]):
		arcpy.Clip_analysis(ften, bdy, "ften_blks")
	elif not arcpy.Exists(layerList[2]):
		arcpy.Clip_analysis(rslt, bdy, "rslt_blks")
	
	print "Clipped Cutblocks T18"


def t48():
	print "t48"
	arcpy.env.workspace = "C:\\Working_Files\\CANFOR_TEST\\t48\\seamless\\t48.gdb"

	bdy = "P:\\canfor\\ke14033cfp_provincial_fibre_flow\\gis\\seamless\\winter2020\\t48\\seamless\\t48.gdb\\t48"
	
	layerList = ["cfp_blks", "ften_blks", "rslt_blks"]
	
	if not arcpy.Exists(layerList[0]):
		arcpy.Clip_analysis(cfp, bdy, "cfp_blks")
	elif not arcpy.Exists(layerList[1]):
		arcpy.Clip_analysis(ften, bdy, "ften_blks")
	elif not arcpy.Exists(layerList[2]):
		arcpy.Clip_analysis(rslt, bdy, "rslt_blks")
	
	print "Clipped Cutblocks T48"



t18()
#t18v2()
t48()



