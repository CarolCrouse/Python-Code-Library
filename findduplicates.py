import arcpy

def backOut(gdbPath):
    char = ''
    while char != '\\':
        gdbPath = gdbPath[:-2]
        char = gdbPath[-1]
    return gdbPath+"Field_Duplicates.txt"


fp = raw_input("Please provide the path to the geodatabase you wish to analyze: ")

if arcpy.Exists(fp):
    arcpy.env.workspace = fp

else:
    print("The geodatabase could not be found")
    exit()

standardFields = ['objectid','shape','shape_length','shape_area']
print "Ignoring the following fields: ", standardFields

fcs = arcpy.ListFeatureClasses()
masterList = []

for fclass in fcs:
    subList = []
    for field in arcpy.ListFields(fclass):
        subList.append(field.name)
    masterList.append([fclass]+subList)

with open(backOut(fp), 'w') as Fout:

    for x in range(0,len(masterList)):
        for y in range(x+1,len(masterList)):
            for z in range(1,len(masterList[x])):
                if (masterList[x][z].lower() not in standardFields) and (masterList[x][z] in masterList[y]):
                    print "Duplicate %s found between %s and %s" % (masterList[x][z], masterList[x][0], masterList[y][0])
                    Fout.write("Duplicate %s found between %s and %s\n" % (masterList[x][z], masterList[x][0], masterList[y][0]))
