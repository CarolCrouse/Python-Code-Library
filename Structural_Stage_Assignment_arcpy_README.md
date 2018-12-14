Dec 14, 2018

This code uses python and arcpy.
This code operates on a feature class table (BC VRI) within a file geodatabase.
Note:  It is currently running with the blank STRUC_CODE field being added by the user prior to running.

This code opens the gdb and runs through various if statements (decision matrix) to assign a structural stage code
and assigns it to the field STRUC_CODE.  Every record is searched and either assigned a valid code or assigned
an XXX code (to indicate it did not fall within the if statements).
