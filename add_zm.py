'''
A Python code to collect all of the shapefiles in a directory and copy them to an existing
directory called 'zm' - the zm folder must be created in the operating directory to work

Taylor J Mckeeman 2019

'''

# Set environments and import libraries
import arcpy
arcpy.env.workspace = env = "P:\\Saskatchewan_Min_of_Environment\\PG191037_ENVFS_2019_NFI\\gis\\seamless\\zm_code_test"
arcpy.env.outputZFlag = "Enabled"
arcpy.env.outputMFlag = "Enabled"

#Get list of shapefiles in current directory
fclass_list = arcpy.ListFeatureClasses()

#Iterate over feature classes in list
for shp in fclass_list:
	#Get the projection of the shp
	prjfile = shp.split(".")[0]+".prj"
	#Create a shell of it in the zm directory using the projection and schema from existing
	arcpy.CreateFeatureclass_management(env+"\\zm", shp, "POLYLINE", shp, "ENABLED", "ENABLED", prjfile)
	#Copy Features into the shell
	arcpy.Append_management(shp, env+"\\zm\\"+shp)
	