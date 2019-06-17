'''
This python code creates average site productivity values for all VRI Feature ID
polygons for a given input VRI layer

Taylor J Mckeeman 2019
'''

#Import libraries and set workspaces
import arcpy
arcpy.env.workspace = "P:\\canfor\\fg_19_170_cfp_cf_k1n_tsr\\gis\\seamless\\data.gdb"
sprod_layer = "P:\\basedata\\site_index\\PSPL6.1\\Site_Prod_with_Approved_PEM_TEM\\Site_Prod_Point_FGDBs\\Site_Prod_Prince_George\\Site_Prod_Prince_George.gdb\\Site_Prod_Prince_George"

vri_layer = "P:\\canfor\\fg_19_170_cfp_cf_k1n_tsr\\gis\\seamless\\data.gdb\\clean\\vri_1"
#vri_layer = ""


'''
************************************************
******* BEGIN FUNCTION SPACE *******************
************************************************
'''
def processTSA(vri_layer, sprod_layer):

    #Generate field map
    print "GENERATING FIELD MAP"
    field_keep_list = ["POLYGON_NUMBER", "AT_SI", "BA_SI", "BG_SI", "BL_SI", "CW_SI", "DR_SI", "EP_SI", "FD_SI", "HM_SI", "HW_SI", "LT_SI", "LW_SI", "PA_SI", "PL_SI", "PW_SI", "PY_SI", "SB_SI", "SE_SI", "SS_SI", "SW_SI", "SX_SI", "YC_SI", "BGC_LABEL", "PEM_SPP"]
	#field_keep_list = ["FEATURE_ID", "AT_SI", "BA_SI", "BG_SI", "BL_SI", "CW_SI", "DR_SI", "EP_SI", "FD_SI", "HM_SI", "HW_SI", "LT_SI", "LW_SI", "PA_SI", "PL_SI", "PW_SI", "PY_SI", "SB_SI", "SE_SI", "SS_SI", "SW_SI", "SX_SI", "YC_SI", "BGC_LABEL", "PEM_SPP"]
    fieldmappings = arcpy.FieldMappings()
    fieldmappings.addTable(vri_layer)
    fieldmappings.addTable(sprod_layer)

    #Change the merge rule to MEAN for all Site prod fields
    print "UPDATING MERGE RULES"
    for item in field_keep_list:
        if item == "POLYGON_NUMBER" or item == "BGC_LABEL" or item == "PEM_SPP":
            pass
        else:
            tempindex = fieldmappings.findFieldMapIndex(item)
            tempfmap = fieldmappings.getFieldMap(tempindex)
            tempfmap.mergeRule = "mean"
            fieldmappings.replaceFieldMap(tempindex, tempfmap)

    #Delete fields that are not desired
    print "DELETING UNWANTED FIELDS"
    for field in fieldmappings.fields:
        if field.name not in field_keep_list:
            fieldmappings.removeFieldMap(fieldmappings.findFieldMapIndex(field.name))

    #Execute the spatial join
    print "EXECUTING SPATIAL JOIN"
    arcpy.SpatialJoin_analysis(vri_layer, sprod_layer, vri_layer + "_joined", field_mapping = fieldmappings)

    print "EXPORTING TABLE"
    arcpy.TableToTable_conversion(vri_layer + "_joined", arcpy.env.workspace, vri_layer + "_table")

'''
************************************************
******* END FUNCTION SPACE *******************
************************************************
'''

#Execute code
print "\n\nBEGINNING PROCESSING..."
print "VRI Input layer: "+vri_layer
print "Site Productivity Source: "+sprod_layer

processTSA(vri_layer, sprod_layer)

print "\n\n*** PROCESSING COMPLETE ***"
print "Output table name is <" + vri_layer+"_table" + ">"
