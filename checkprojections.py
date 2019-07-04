##############################################################################################################
#  This program checks the projections of feature classes within a geodatabase.
#  It asks to whether to check against the NAD 1983 BC Environment Albers or you can specifiy another projection.
#  It also asks if you want to reproject any feature classes that don't match the projection you selected.
#  If you choose Y to reproject, a new feature class is made and named *_projected
#  July 4, 2019
#  Carol Ann Crouse
################################################################################################################

import arcpy

fp = raw_input("\nPlease provide the path to the geodatabase you wish to analyze: ")

if arcpy.Exists(fp):
    arcpy.env.workspace = fp

else:
    print("The geodatabase could not be found")
    exit()

while True:
    prjType = raw_input("\nWhat projection would you like to test against?\nEnter a WKID code or hit enter to use NAD 1983 BC Environment Albers: ")
    if prjType == "":
        print "\nAssuming a desired projection of NAD 1983 BC Environment Albers, WKID code = 3005"
        prjCode = 3005
        break
    else:
        print "\n*****NOTE: Custom projections will not be verified properly by this code."
        try:
            otherPrj = arcpy.SpatialReference(int(prjType))
            prjCode = int(prjType)
            print "\nUsing a desired projection of %s" % (otherPrj.name)
            break
        except Exception as e:
            print "\n**********\nINVALID WKID CODE\n**********"

autoCorrect = raw_input("\nWould you like to turn on Auto Projecting to solve conflicts? (y or n)")
projectify = False
if autoCorrect.lower() in ['y', 'n']:
	if autoCorrect.lower() == 'y':
		projectify = True
else:
	print "\nIncorrect entry, defaulting to no Auto Projection"

wrongproj = 0
errors = 0
	
fclasses = arcpy.ListFeatureClasses()
allClear = True
for fclass in fclasses:
    if arcpy.Describe(fclass).spatialReference.factoryCode == prjCode:
        pass
    else:
        print "\n**WARNING** Feature class %s is not in the correct projection" % (fclass)
        wrongproj += 1
        allClear = False
        if projectify:
			print"\n Creating projected version..."
			try:
				arcpy.Project_management(fclass, fclass+"_projected", arcpy.SpatialReference(prjCode))
				print "\nProjecting Successful"
			except:
				print "\n**AN ERROR OCCURRED** Could not project file"
				errors += 1

print "\nVerification complete"
print "\n%d layers were analyzed" % (len(fclasses))
print "\n%d layers found in the wrong projection. %d errors occurred in reprojecting" % (wrongproj, errors)
if allClear:
    print "\nNo foreign projections found"
