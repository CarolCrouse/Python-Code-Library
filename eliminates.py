import arcpy
from datetime import datetime
input_res = 'res_29Nov19_elim_sp'
arcpy.env.workspace = 'P:\\canfor\\fg_19_539_cfp_bulkey_fnwl_licence\\gis\\overlays\\res.gdb'
for level in [10, 100, 1000]:
	print "Working on level %d" % (level)
	start = datetime.now()
	if level == 10:
		infile = input_res
		outfile = "tmp_10"
	else:
		infile = "tmp_"+str(level/10)
		outfile = "tmp_"+str(level)
	
	print "Creating Layer..."
	if arcpy.Exists("tmp"):
		arcpy.Delete_management("tmp")
	arcpy.MakeFeatureLayer_management(infile, "tmp")
	print "Performing Selection..."
	arcpy.SelectLayerByAttribute_management("tmp", where_clause='"SHAPE_Area" < %d' % (level))
	print "Eliminating..."
	arcpy.Eliminate_management("tmp", outfile)
	print "Runtime = %s" % (datetime.now()-start)
	
print "Complete."