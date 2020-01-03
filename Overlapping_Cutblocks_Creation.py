import arcpy
import os
from arcpy import env

#########################################################################################################
# Set workspace 
#########################################################################################################
arcpy.env.workspace = r"C:\Working_Files\CANFOR_Cutblocks_Coded\FTEN_Cutblocks_CODED.gdb" 	# ENTER THE LOCATION OF THE CUTBLOCKS GDB
print "workspace is C:\Working_Files\CANFOR_Cutblocks_Coded\FTEN_Cutblocks_CODED.gdb"		# ENTER THE LOCATION OF THE CUTBLOCKS GDB
prefix = "FTEN_"																			# ENTER THE PREFIX ID FOR THE TYPE OF BLOCKS (EX FTEN, CANFOR, CFP,..)


#########################################################################################################
# Delete the existing layers in the GDB
#########################################################################################################
print "Deleting existing layers"
layerlist = [prefix+"cutblocks_valid", prefix+"cutblocks_union", prefix+"cutblocks_singlepart", prefix+"cutblocks_elim1", prefix+"cutblocks_elim2", prefix+"cutblocks_overlap", prefix+"cutblocks_overlap_identical", "cutblocks_overlap_table"]

for fc in layerlist:
	if arcpy.Exists(fc):
		arcpy.Delete_management(fc,"")


#########################################################################################################
# This section allows you to limit the cutblocks to only valid ones if you wish to (ex.. ones with dates)
# There are 3 lines showing examples of selections
#########################################################################################################
print "Selecting only valid cutblocks"
arcpy.MakeFeatureLayer_management("FTEN_Blocks","cutblock_temp")																	# ENTER THE NAME OF THE CUTBLOCKS LAYER
#arcpy.SelectLayerByAttribute_management("cutblock_temp", "NEW_SELECTION", "DISTURBANCE_END_DATE IS NOT NULL")   					
#arcpy.SelectLayerByAttribute_management("cutblock_temp", "NEW_SELECTION", "DENUDATION_1_COMPLETION_DATE IS NOT NULL")				
#arcpy.SelectLayerByAttribute_management("cutblock_temp", "NEW_SELECTION", "CFP_HC_DATE IS NOT NULL")								
arcpy.CopyFeatures_management("cutblock_temp", prefix+"cutblocks_valid")



#########################################################################################################
# Run a self union on the cutblocks 
# This cuts in the overlapping linework of the cutblocks
#########################################################################################################
print "Running self union"
arcpy.Union_analysis(prefix+"cutblocks_valid", prefix+"cutblocks_union")


#########################################################################################################
# Run multipart to singlepart on the self unioned cutblocks
# This is done so that small sections of multipart polygons are caught in the upcoming eliminates
#########################################################################################################
print "Converting to singlepart"
arcpy.MultipartToSinglepart_management(prefix+"cutblocks_union", prefix+"cutblocks_singlepart")
# arcpy.RepairGeometry_management(prefix+"cutblocks_singlepart")


#########################################################################################################
# Run an eliminate <100 
# Sometimes there are geometry errors produced with the govt cutblock layers so a repair geometry
# can be run after
#########################################################################################################
print "Running 1st Eliminate"
arcpy.MakeFeatureLayer_management(prefix+"cutblocks_singlepart","cutblocks_elim1_temp")
arcpy.SelectLayerByAttribute_management("cutblocks_elim1_temp", "NEW_SELECTION", '"Shape_Area" < 100')
arcpy.Eliminate_management("cutblocks_elim1_temp", prefix+"cutblocks_elim1", "LENGTH")
# arcpy.RepairGeometry_management(prefix+"cutblocks_elim1")

#########################################################################################################
# Run an eliminate <500 
# Sometimes there are geometry errors produced with the govt cutblock layers so a repair geometry
# can be run after
#########################################################################################################
print "Running 2nd Eliminate"
arcpy.MakeFeatureLayer_management(prefix+"cutblocks_elim1","cutblocks_elim2_temp")
arcpy.SelectLayerByAttribute_management("cutblocks_elim2_temp", "NEW_SELECTION", '"Shape_Area" < 500')
arcpy.Eliminate_management("cutblocks_elim2_temp", prefix+"cutblocks_elim2", "LENGTH")
# arcpy.RepairGeometry_management(prefix+"cutblocks_elim2")

#########################################################################################################
# Run Topology Checks
# Check if the topology GDB exists and delete
#########################################################################################################
if arcpy.Exists("P:\\canfor\\ke14033cfp_provincial_fibre_flow\\gis\\seamless\\winter2020\\CANFOR_Cutblocks\\CANFOR_Cutblocks_topology.gdb"):		# ENTER THE LOCATION OF THE CUTBLOCKS GDB
	arcpy.Delete_management("P:\\canfor\\ke14033cfp_provincial_fibre_flow\\gis\\seamless\\winter2020\\CANFOR_Cutblocks\\CANFOR_Cutblocks_topology.gdb","")		# ENTER THE LOCATION OF THE CUTBLOCKS GDB

topo_input = prefix+"cutblocks_elim2"
topo_name = "topology"
cluster_tol = 0.001
print "Creating and Validating Topology"

#########################################################################################################
# Create GDB and feature dataset for checking topology of the cutblocks
#########################################################################################################
print "Create Topology GDB"
gdb = arcpy.CreateFileGDB_management("P:\\canfor\\ke14033cfp_provincial_fibre_flow\\gis\\seamless\\winter2020\\CANFOR_Cutblocks\\", "CANFOR_Cutblocks_topology.gdb")   # ENTER THE LOCATION OF THE CUTBLOCKS GDB
print "Create Feature Dataset within Topology"
fdataset = arcpy.CreateFeatureDataset_management(gdb, "topo", arcpy.Describe(topo_input).spatialReference)

#########################################################################################################
# Import the cutblocks to the feature dataset
#########################################################################################################
print "Copy Feature Class to Topology"
fclass = arcpy.FeatureClassToFeatureClass_conversion(topo_input, fdataset, "cutblocks")

#########################################################################################################
# Set up the topology rules and create the topology
#########################################################################################################
print "Create Topology and Rules"
topology = arcpy.CreateTopology_management(fdataset, topo_name, cluster_tol)
arcpy.AddFeatureClassToTopology_management(topology, fclass, "1", "1")
arcpy.AddRuleToTopology_management(topology,"Must Not Overlap (Area)",fclass,"","","")

#########################################################################################################
# Validate topology
#########################################################################################################
print "Validate Topology"
arcpy.ValidateTopology_management(topology, "Full_Extent")

#########################################################################################################
# Export topology errors
#########################################################################################################
print "Exporting Topology Errors"
arcpy.ExportTopologyErrors_management(topology, gdb, "cutblocks_topo")

#########################################################################################################
# Select only Must Not Overlap Topology Errors (cutblocks_overlap)
# Due to very small slivers which did not eliminate it created errors for Cluster Tolerance which are not needed
#########################################################################################################
print "Creating Must Not Overlap Subset"
# ENTER THE LOCATION OF THE CUTBLOCKS GDB
arcpy.MakeFeatureLayer_management("P:\\canfor\\ke14033cfp_provincial_fibre_flow\\gis\\seamless\\winter2020\\CANFOR_Cutblocks\\CANFOR_Cutblocks_topology.gdb\\cutblocks_topo_poly","cutblocks_topo_subset")
arcpy.SelectLayerByAttribute_management("cutblocks_topo_subset", "NEW_SELECTION", "RuleDescription = 'Must Not Overlap'")
arcpy.CopyFeatures_management("cutblocks_topo_subset",prefix+"cutblocks_overlap")

#########################################################################################################
# Run Find Identical on the Overlapping Cutblock Topology Layer (cutblocks_overlap)
# This is used to identify overlapping polygons which overlap more than 2 polygons
# Each group of overlapping polygons needs to have an ID assigned to the group
#########################################################################################################
print "Finding Identical Topology"
arcpy.FindIdentical_management(prefix+"cutblocks_overlap", prefix+"cutblocks_overlap_identical", "Shape", output_record_option="ONLY_DUPLICATES")


#########################################################################################################
# Add ID field to the Overlapping Cutblock Topology layer (cutblocks_overlap)
# It will assign IDs to each group of overlapping polygons so that overlapping polygons can be identified 
# by having the same ID and then can be compared as to which one to keep 
#########################################################################################################
print "Adding OVERLAP_ID Field"
arcpy.AddField_management(prefix+"cutblocks_overlap", "OVERLAP_ID", "LONG")


#########################################################################################################
# This section creates a data dictionary and update cursor 
# It joins the Identical table to the cutblocks_overlap layer and assigns the Identical table ID to the added field OVERLAP_ID
# This allows overlapping polygons to be identified by having the same ID and can be compared as to which one to keep 
# Join Criteria [prefix+"cutblocks_overlap_identical"]![IN_FID] = [prefix+"cutblocks_overlap"]![OBJECTID]
# Where they join then OVERLAP_ID = [prefix+"cutblocks_overlap_identical"]![FEAT_SEQ], otherwise OVERLAP_ID = ObjectID+10000
#########################################################################################################

print "Joining IDs to Overlapping Polygons"

#feature class to update
pointFc = prefix+"cutblocks_overlap"
#update field
updateFld = "OVERLAP_ID"
#update fc key field
IdFld = "OBJECTID"

#join feature class containing the update values
joinFc = prefix+"cutblocks_overlap_identical"
#join value field to be transferred
joinValFld = "FEAT_SEQ"
#join key field
joinIdFld = "IN_FID"

#create dictionary
#Key: join field
#Value: field with value to be transferred
valueDi = dict ([(key, val) for key, val in
                 arcpy.da.SearchCursor
                 (joinFc, [joinIdFld, joinValFld])])

#update feature class
with arcpy.da.UpdateCursor (pointFc, [updateFld, IdFld]) as cursor:
    for update, key in cursor:
        #skip if key value is not in dictionary
        if not key in valueDi:
        	row = (key+10000, key)
        	#continue
        #create row tuple
        else:
        	row = (valueDi [key], key)
       

        #update row
        cursor.updateRow (row)

del cursor

#########################################################################################################
# Next is to transfer the data from the cutblocks_overlap layer back to the source cutblock layer 
# The cutblocks_overlap is converted to a table for the join
#########################################################################################################
print "Joining the IDs from the Overlapping Topology layer to the full Cutblock Layer"
arcpy.AddField_management(prefix+"cutblocks_elim2", "OVERLAP_KEEP", "TEXT")
arcpy.AddField_management(prefix+"cutblocks_elim2", "OVERLAP_UN_ID", "LONG")


arcpy.TableToTable_conversion(prefix+"cutblocks_overlap", "P:\\canfor\\ke14033cfp_provincial_fibre_flow\\gis\\seamless\\winter2020\\CANFOR_Cutblocks\\CANFOR_Cutblocks.gdb", "cutblocks_overlap_table")

print "Joining IDs from Overlapping Polygons Back to Source Cutblocks Layer"

#########################################################################################################
# This section creates a data dictionary and update cursor 
# It joins the cutblocks_overlap table to the elim2 layer and assigns the OVERLAP_KEEP and OVERLAP_UN_ID
# Two joins must be done
#########################################################################################################

# 1st Join
# Join Criteria [prefix+"cutblocks_elim2"]![OBJECTID] = [cutblocks_overlap_table]![OriginObjectID]
# Where they join then OVERLAP_UN_ID = [cutblocks_overlap_table]![OVERLAP_ID]
#feature class to update
pointFc = prefix+"cutblocks_elim2"
#update field
updateFld = "OVERLAP_UN_ID"
#update fc key field
IdFld = "OBJECTID"

#join feature class
joinFc = "cutblocks_overlap_table"
#join value field to be transferred
joinValFld = "OVERLAP_ID"
#join key field
joinIdFld = "OriginObjectID"

#create dictionary
#Key: join field
#Value: field with value to be transferred
valueDi = dict ([(key, val) for key, val in
                 arcpy.da.SearchCursor
                 (joinFc, [joinIdFld, joinValFld])])

#update feature class
with arcpy.da.UpdateCursor (pointFc, [updateFld, IdFld]) as cursor:
    for update, key in cursor:
        #skip if key value is not in dictionary
        if not key in valueDi:
        	continue
        #create row tuple
      
        row = (valueDi [key], key)

        #update row
        cursor.updateRow (row)

del cursor


# 2nd Join
# Join Criteria [prefix+"cutblocks_elim2"]![OBJECTID] = [cutblocks_overlap_table]![DestinationObjectID]
# Where they join then OVERLAP_UN_ID = [cutblocks_overlap_table]![OVERLAP_ID]


#feature class to update
pointFc = prefix+"cutblocks_elim2"
#update field
updateFld = "OVERLAP_UN_ID"
#update fc key field
IdFld = "OBJECTID"

#join feature class
joinFc = "cutblocks_overlap_table"
#join value field to be transferred
joinValFld = "OVERLAP_ID"
#join key field
joinIdFld = "DestinationObjectID"

#create dictionary
#Key: join field
#Value: field with value to be transferred
valueDi = dict ([(key, val) for key, val in
                 arcpy.da.SearchCursor
                 (joinFc, [joinIdFld, joinValFld])])

#update feature class
with arcpy.da.UpdateCursor (pointFc, [updateFld, IdFld]) as cursor:
    for update, key in cursor:
        #skip if key value is not in dictionary
        if not key in valueDi:
        	continue
        #create row tuple
        
        row = (valueDi [key], key)

        #update row
        cursor.updateRow (row)

del cursor

#########################################################################################################
# Update the OVERLAP_KEEP field
#########################################################################################################

outlayer = "CANFOR_cutblocks_elim2"
rows = arcpy.UpdateCursor(outlayer)  #this updates the output feature class
											 
for row in rows:
	if row.OVERLAP_UN_ID >0:
		row.OVERLAP_KEEP = "N"
		rows.updateRow(row)

del row
del rows


# #  ADD GRACE"S CODE TO CHOOSE WHICH CUTBLOCK TO KEEP IN CANFOR_CUTBLOCKS_ELIM2
# #  LOCATION OF CODE:  "P:\canfor\KE-13-053-CFP_Morice_TSR_Review\analysis\py\15nov2019\fix_overlap_cutblocks.py"



