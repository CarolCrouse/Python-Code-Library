#Import geoprocessing
import arcpy

#Set local variables
fc = "P:\\kib\\fk_19_201_kib_dri_aac_update\\gis\\seamless\\Alter_Field_Test.gdb\\vri_2018_fields_to_keep_v2" 

#Alter the properties of a non nullable, short data type field to become a text field

arcpy.AlterField_management(fc, 'PROJECTED_DATE', 'VRI18_PROJECTED_DATE', 'VRI18_PROJECTED_DATE')
arcpy.AlterField_management(fc, 'EARLIEST_NONLOGGING_DIST_TYPE', 'VRI18_EARLIEST_NONLOGGING_TYPE', 'VRI18_EARLIEST_NONLOGGING_TYPE')
arcpy.AlterField_management(fc, 'EARLIEST_NONLOGGING_DIST_DATE', 'VRI18_EARLIEST_NONLOGGING_DATE', 'VRI18_EARLIEST_NONLOGGING_DATE')
arcpy.AlterField_management(fc, 'HARVEST_DATE', 'VRI18_HARVEST_DATE', 'VRI18_HARVEST_DATE')
arcpy.AlterField_management(fc, 'CROWN_CLOSURE', 'VRI18_CROWN_CLOSURE', 'VRI18_CROWN_CLOSURE')
arcpy.AlterField_management(fc, 'SITE_INDEX', 'VRI18_SITE_INDEX', 'VRI18_SITE_INDEX')
arcpy.AlterField_management(fc, 'BASAL_AREA', 'VRI18_BASAL_AREA', 'VRI18_BASAL_AREA')
arcpy.AlterField_management(fc, 'VRI_LIVE_STEMS_PER_HA', 'VRI18_VRI_LIVE_STEMS_PER_HA', 'VRI18_VRI_LIVE_STEMS_PER_HA')
arcpy.AlterField_management(fc, 'VRI_DEAD_STEMS_PER_HA', 'VRI18_VRI_DEAD_STEMS_PER_HA', 'VRI18_VRI_DEAD_STEMS_PER_HA')
arcpy.AlterField_management(fc, 'SPECIES_CD_1', 'VRI18_SPECIES_CD_1', 'VRI18_SPECIES_CD_1')
arcpy.AlterField_management(fc, 'SPECIES_PCT_1', 'VRI18_SPECIES_PCT_1', 'VRI18_SPECIES_PCT_1')
arcpy.AlterField_management(fc, 'SPECIES_CD_2', 'VRI18_SPECIES_CD_2', 'VRI18_SPECIES_CD_2')
arcpy.AlterField_management(fc, 'SPECIES_PCT_2', 'VRI18_SPECIES_PCT_2', 'VRI18_SPECIES_PCT_2')
arcpy.AlterField_management(fc, 'SPECIES_CD_3', 'VRI18_SPECIES_CD_3', 'VRI18_SPECIES_CD_3')
arcpy.AlterField_management(fc, 'SPECIES_PCT_3', 'VRI18_SPECIES_PCT_3', 'VRI18_SPECIES_PCT_3')
arcpy.AlterField_management(fc, 'SPECIES_CD_4', 'VRI18_SPECIES_CD_4', 'VRI18_SPECIES_CD_4')
arcpy.AlterField_management(fc, 'SPECIES_PCT_4', 'VRI18_SPECIES_PCT_4', 'VRI18_SPECIES_PCT_4')
arcpy.AlterField_management(fc, 'SPECIES_CD_5', 'VRI18_SPECIES_CD_5', 'VRI18_SPECIES_CD_5')
arcpy.AlterField_management(fc, 'SPECIES_PCT_5', 'VRI18_SPECIES_PCT_5', 'VRI18_SPECIES_PCT_5')
arcpy.AlterField_management(fc, 'SPECIES_CD_6', 'VRI18_SPECIES_CD_6', 'VRI18_SPECIES_CD_6')
arcpy.AlterField_management(fc, 'SPECIES_PCT_6', 'VRI18_SPECIES_PCT_6', 'VRI18_SPECIES_PCT_6')
arcpy.AlterField_management(fc, 'PROJ_AGE_1', 'VRI18_PROJ_AGE_1', 'VRI18_PROJ_AGE_1')
arcpy.AlterField_management(fc, 'PROJ_HEIGHT_1', 'VRI18_HEIGHT_AGE_1', 'VRI18_PROJ_HEIGHT_1')
arcpy.AlterField_management(fc, 'LIVE_VOL_PER_HA_SPP1_125', 'VRI18_LIVE_VOL_PER_HA_SPP1_125', 'VRI18_LIVE_VOL_PER_HA_SPP1_125')
arcpy.AlterField_management(fc, 'LIVE_VOL_PER_HA_SPP2_125', 'VRI18_LIVE_VOL_PER_HA_SPP2_125', 'VRI18_LIVE_VOL_PER_HA_SPP2_125')
arcpy.AlterField_management(fc, 'LIVE_VOL_PER_HA_SPP3_125', 'VRI18_LIVE_VOL_PER_HA_SPP3_125', 'VRI18_LIVE_VOL_PER_HA_SPP3_125')
arcpy.AlterField_management(fc, 'LIVE_VOL_PER_HA_SPP4_125', 'VRI18_LIVE_VOL_PER_HA_SPP4_125', 'VRI18_LIVE_VOL_PER_HA_SPP4_125')
arcpy.AlterField_management(fc, 'LIVE_VOL_PER_HA_SPP5_125', 'VRI18_LIVE_VOL_PER_HA_SPP5_125', 'VRI18_LIVE_VOL_PER_HA_SPP5_125')
arcpy.AlterField_management(fc, 'LIVE_VOL_PER_HA_SPP6_125', 'VRI18_LIVE_VOL_PER_HA_SPP6_125', 'VRI18_LIVE_VOL_PER_HA_SPP6_125')
arcpy.AlterField_management(fc, 'DEAD_VOL_PER_HA_SPP1_125', 'VRI18_DEAD_VOL_PER_HA_SPP1_125', 'VRI18_DEAD_VOL_PER_HA_SPP1_125')
arcpy.AlterField_management(fc, 'DEAD_VOL_PER_HA_SPP2_125', 'VRI18_DEAD_VOL_PER_HA_SPP2_125', 'VRI18_DEAD_VOL_PER_HA_SPP2_125')
arcpy.AlterField_management(fc, 'DEAD_VOL_PER_HA_SPP3_125', 'VRI18_DEAD_VOL_PER_HA_SPP3_125', 'VRI18_DEAD_VOL_PER_HA_SPP3_125')
arcpy.AlterField_management(fc, 'DEAD_VOL_PER_HA_SPP4_125', 'VRI18_DEAD_VOL_PER_HA_SPP4_125', 'VRI18_DEAD_VOL_PER_HA_SPP4_125')
arcpy.AlterField_management(fc, 'DEAD_VOL_PER_HA_SPP5_125', 'VRI18_DEAD_VOL_PER_HA_SPP5_125', 'VRI18_DEAD_VOL_PER_HA_SPP5_125')
arcpy.AlterField_management(fc, 'DEAD_VOL_PER_HA_SPP6_125', 'VRI18_DEAD_VOL_PER_HA_SPP6_125', 'VRI18_DEAD_VOL_PER_HA_SPP6_125')

print"Rename Fields Done"