import arcpy
import os
from arcpy import env


# set workspace
arcpy.env.workspace = r"P:\\canfor\\KE-13-053-CFP_Morice_TSR_Review\\gis\\resultant_2019\\seamless\\SBA watersheds_labelled\\SBA.gdb"


#Create list of geodatabase layers

layerList = ['Bergeland_Creek', 'Big_Loon_Creek', 'Boucher_Creek', 'Buck_Creek', 'Burnie_River', 'Bymac_Creek', 'Byron_Creek', 'Canyon_Creek','Caribou_Creek', 'Caribou_Mountain_Creek', 'Carl_Borden_Creek', 'Cedric_Creek', 'Cesford_Creek', 'Char_Creek','Chickamin_Creek', 'Clore_River', 'Coffin_Creek', 'Coles_Creek', 'Coles_Lake', 'Covert_Creek', 'Crona_Creek', 'Crow_Creek', 'Crystal_Creek', 'Cummins_Creek', 'Deasy_Creek', 'Deep_Creek', 'Denys_Creek', 'Desdemona_Creek', 'Dockrill_Creek', 'DuBose_Creek', 'Dungate_Creek', 'East_Caribou_Creek', 'East_Gates_Creek', 'East_Hautete_Lake', 'East_Kasalka_Creek', 'East_Mosquito_Creek', 'East_Nakinilerak_Creek', 'East_Old_Fort_Creek', 'Elliot_Creek', 'Elwin_Creek', 'Emerson_Creek', 'False_Chelaslie_Creek', 'False_Tagit_Creek', 'Fenton_Creek', 'Fenton_Nanika_Creek', 'Fenton_Nanika_Creek_South', 'Findlay_Lake', 'Five_Mile_Creek', 'Fleming_Creek', 'Fort_Babine_Creek', 'Francois_Lake', 'Friday_Creek', 'Frypan_Creek', 'Fulton_above_Chapman_Lake', 'Fulton_River', 'Gabriel_Creek', 'Gloyazikut_Creek', 'Goathorn_Creek', 'Gold_Creek', 'Gosnell_Creek', 'Guess_Creek', 'Hagarty_Creek', 'Hagman_Creek', 'Haul_Creek', 'Hautete_Creek', 'Haymeadow_Creek', 'Henkel_Creek', 'Herb_Dome_Creek', 'Holland_Creek', 'Holmes_Creek', 'Houston_Tommy_Creek', 'Houston_Tommy_Trib_1', 'Houston_Tommy_Trib_2', 'Howson_Creek', 'Jinx_Creek', 'Johnny_David_Creek', 'Joshua_Creek', 'Kasalka_Creek', 'Kew_Creek', 'Kidprice_Lake', 'Kivi_Creek', 'Klo_Creek', 'Knapper_Creek', 'Lamprey_Creek', 'Laventie_Creek', 'Lemieux_Creek', 'Lindquist_Creek', 'Little_Bulkley', 'Little_Cumulus_Creek', 'Little_Loon_Creek', 'Long_Island_Creek', 'Lower_Talho', 'Matzehtzel_Creek', 'Mcbride_Creek', 'Mccuish_Creek', 'McQuarrie_Creek', 'Moose_Flats_Creek', 'Moose_Skin_Creek', 'Morice_River', 'Morice_Trib_1', 'Morice_Trib_2', 'Morrison_Creek', 'Nadina_River', 'Nado_Creek', 'Nanika_River', 'Nanika_Trib_1', 'Nanika_Trib_2', 'Nanika_Trib_3', 'Nanika_Trib_4', 'Nata_Creek', 'Natowite_Creek', 'Ney_Creek', 'Nicholson_Creek', 'Nikun_Creek', 'Nizik_Creek', 'No_Mans_Creek', 'North_Spit_Creek', 'Nugget_Creek', 'Objective_Creek', 'One_Mile_Creek', 'Ootsa_Lake', 'Othello_Creek', 'Owen_Creek', 'Owen_Trib_1', 'Parrott_Creek', 'Pass_Creek', 'Pat_Creek', 'Peacock_Creek', 'Perow_Creek', 'Peter_Aleck_Creek', 'Picket_Creek', 'Pierre_Creek', 'Pillar_Creek', 'Pimpernel_Creek', 'Puport_Creek', 'Ramsay_Creek', 'Redtop_Creek', 'Richfield_Creek', 'Robert_Hatch_Creek', 'Robin_Creek', 'Sakeniche_River', 'Sandpiper_Creek', 'Scallon_Creek', 'Shadow_Creek', 'Shea_Creek', 'Shelford_Creek', 'Shelford_Lake', 'Shoulder_Creek', 'Star_Creek', 'Stepp_Creek', 'Sunset_Creek', 'Sweeney_Creek', 'Tachek_Creek', 'Tagetochlain_Creek', 'Tagit_Creek', 'Tahtsa_Creek', 'Tahtsa_Reach', 'Tahtsa_Trib_1', 'Tahtsa_Trib_2', 'Tahtsa_Trib_3', 'Tahtsa_Trib_4', 'Tea_Billy_Creek', 'Telkwa_River', 'Thautil_River', 'Thompson_Creek', 'Tidesley_Creek', 'Tom_George_Creek', 'Troitsa_Creek', 'Tsah_Creek', 'Two_Mile_Creek', 'Upper_Bulkley', 'Upper_Gosnell_Creek', 'Upper_Guess_Creek', 'Upper_Hautete_Creek', 'Upper_Houston_Tommy', 'Upper_Morice_River', 'Upper_Nadina', 'Upper_Owen_Creek', 'Upper_Tahlo', 'Upper_Thautil_River', 'Utem_Creek', 'Vallee_Creek', 'Vivian_Creek', 'Wallcott_Creek', 'Watson_Creek', 'Webster_Creek', 'Wells_Creek', 'West_Caribou_Creek', 'West_Francois_Lake', 'West_Morrison_1', 'West_Morrison_2', 'West_Morrison_3', 'West_Mosquito_Creek', 'West_No_Mans_Creek', 'West_Old_Fort_Creek', 'Whitesail', 'Whitesail_Trib_1', 'Whitesail_Trib_2', 'Whitesail_Trib_3', 'Whitesail_Trib_4','Whiting_Creek']

# Drop and rename fields from layers
for fc in layerList:

	# if fc == "Bergeland_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'bergeland', 'bergeland')

	# if fc == "Big_Loon_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'bigloon', 'bigloon')
		
	# if fc == "Boucher_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'boucher', 'boucher')

	# if fc == "Buck_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'buck', 'buck')
		
	# if fc == "Burnie_River":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'burnie', 'burnie')

	# if fc == "Bymac_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'bymac', 'bymac')
		
	# if fc == "Byron_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'byron', 'byron')

	# if fc == "Canyon_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'canyon', 'canyon')

	# if fc == "Caribou_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'caribou', 'caribou')
		
	# if fc == "Caribou_Mountain_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'cariboumtn', 'cariboumtn')

	# if fc == "Carl_Borden_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'carl', 'carl')
		
	# if fc == "Cedric_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'cedric', 'cedric')

	# if fc == "Cesford_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'cesford', 'cesford')

	# if fc == "Char_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'char', 'char')
		
	if fc == "Chickamin_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'chickamin', 'chickamin')

	# if fc == "Clore_River":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'clore', 'clore')
		
	# if fc == "Coffin_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'coffin', 'coffin')
		
	# if fc == "Coles_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'coles', 'coles')

	# if fc == "Coles_Lake":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'coleslk', 'coleslk')
		
	# if fc == "Covert_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'covert', 'covert')

	# if fc == "Crona_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'crona', 'crona')
		
	# if fc == "Crow_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'crow', 'crow')
		
	# if fc == "Crystal_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'crystal', 'crystal')

	# if fc == "Cummins_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'cummins', 'cummins')
		
	# if fc == "Deasy_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'deasy', 'deasy')

	# if fc == "Deep_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'deep', 'deep')
		
	# if fc == "Denys_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'denys', 'denys')
	
	# if fc == "Desdemona_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'desdemona', 'desdemona')

	# if fc == "Dockrill_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'dockrill', 'dockrill')
		
	# if fc == "DuBose_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'dubose', 'dubose')

	# if fc == "Dungate_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'dungate', 'dungate')
		
	# if fc == "East_Caribou_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'eastcaribou', 'eastcaribou')

	# if fc == "East_Gates_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'eastgates', 'eastgates')

	# if fc == "East_Hautete_Lake":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'easthautete', 'easthautete')
		
	# if fc == "East_Kasalka_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'eastkasalka', 'eastkasalka')

	# if fc == "East_Mosquito_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'eastmosquito', 'eastmosquito')
		
	# if fc == "East_Nakinilerak_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'eastnakini', 'eastnakini')
		
	# if fc == "East_Old_Fort_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'eastoldfort', 'eastoldfort')

	# if fc == "Elliot_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'elliot', 'elliot')
		
	# if fc == "Elwin_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'elwin', 'elwin')

	# if fc == "Emerson_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'emerson', 'emerson')
		
	# if fc == "False_Chelaslie_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'falseches', 'falseches')
		
	# if fc == "False_Tagit_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'falsetagit', 'falsetagit')

	# if fc == "Fenton_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'fenton', 'fenton')
		
	# if fc == "Fenton_Nanika_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'fentonnanika', 'fentonnanika')

	# if fc == "Fenton_Nanika_Creek_South":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'fentonnanikas', 'fentonnanikas')
		
	# if fc == "Findlay_Lake":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'findlay', 'findlay')
		
	# if fc == "Five_Mile_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'fivemile', 'fivemile')

	# if fc == "Fleming_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'fleming', 'fleming')
		
	# if fc == "Fort_Babine_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'fortbabine', 'fortbabine')

	# if fc == "Foxy_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'foxy', 'foxy')
		
	# if fc == "Francois_Lake":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'francois', 'francois')
		
	# if fc == "Friday_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'friday', 'friday')

	# if fc == "Frypan_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'frypan', 'frypan')
		
	# if fc == "Fulton_above_Chapman_Lake":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'fultonchap', 'fultonchap')

	# if fc == "Fulton_River":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'fultonriv', 'fultonriv')
		
	# if fc == "Gabriel_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'gabriel', 'gabriel')
		
	# if fc == "Gloyazikut_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'gloyazikut', 'gloyazikut')

	# if fc == "Goathorn_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'goathorn', 'goathorn')
		
	# if fc == "Gold_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'gold', 'gold')

	# if fc == "Gosnell_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'gosnell', 'gosnell')
		
	# if fc == "Guess_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'guess', 'guess')
		
	# if fc == "Hagarty_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'hagarty', 'hagarty')

	# if fc == "Hagman_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'hagman', 'hagman')
		
	# if fc == "Haul_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'haul', 'haul')

	# if fc == "Hautete_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'hautete', 'hautete')
		
	# if fc == "Haymeadow_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'haymeadow', 'haymeadow')
		
	# if fc == "Henkel_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'henkel', 'henkel')

	# if fc == "Herb_Dome_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'herbdome', 'herbdome')
		
	# if fc == "Holland_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'holland', 'holland')

	# if fc == "Holmes_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'holmes', 'holmes')
		
	# if fc == "Houston_Tommy_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'houstommy', 'houstommy')
		
	# if fc == "Houston_Tommy_Trib_1":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'houstrib1', 'houstrib1')

	# if fc == "Houston_Tommy_Trib_2":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'houstrib2', 'houstrib2')
		
	# if fc == "Howson_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'howson', 'howson')

	# if fc == "Jinx_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'jinx', 'jinx')
		
	# if fc == "Johnny_David_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'johnnydavid', 'johnnydavid')
		
	# if fc == "Joshua_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'joshua', 'joshua')

	# if fc == "Kasalka_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'kasalka', 'kasalka')
		
	# if fc == "Kew_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'kew', 'kew')

	# if fc == "Kidprice_Lake":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'kidprice', 'kidprice')
		
	# if fc == "Kivi_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'kivi', 'kivi')
		
	# if fc == "Klo_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'klo', 'klo')

	# if fc == "Knapper_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'knapper', 'knapper')
		
	# if fc == "Lamprey_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'lamprey', 'lamprey')

	# if fc == "Laventie_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'laventie', 'laventie')
		
	# if fc == "Lemieux_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'lemieux', 'lemieux')
		
	# if fc == "Lindquist_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'lindquist', 'lindquist')

	# if fc == "Little_Bulkley":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'littlebulkley', 'littlebulkley')
		
	# if fc == "Little_Cumulus_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'littlecumulus', 'littlecumulus')

	# if fc == "Little_Loon_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'littleloon', 'littleloon')
		
	# if fc == "Long_Island_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'longisland', 'longisland')
		
	# if fc == "Lower_Talho":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'lowertalho', 'lowertalho')

	# if fc == "Matzehtzel_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'matzehtzel', 'matzenhtzel')
		
	# if fc == "Mcbride_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'mcbride', 'mcbride')

	# if fc == "Mccuish_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'mccuish', 'mccuish')
		
	# if fc == "McQuarrie_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'mcquarrie', 'mcquarrie')
		
	# if fc == "Moose_Flats_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'mooseflats', 'mooseflats')

	# if fc == "Moose_Skin_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'mooseskin', 'mooseskin')
		
	# if fc == "Morice_River":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'moriceriv', 'moriceriv')

	# if fc == "Morice_Trib_1":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'moricetrib1', 'moricetrib1')
		
	# if fc == "Morice_Trib_2":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'moricetrib2', 'moricetrib2')
		
	# if fc == "Morrison_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'morrison', 'morrison')

	# if fc == "Nadina_River":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'nadina', 'nadina')
		
	# if fc == "Nado_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'nado', 'nado')

	# if fc == "Nanika_River":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'nanikariv', 'nanikariv')
		
	# if fc == "Nanika_Trib_1":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'nanikatrib1', 'nanikatrib1')
		
	# if fc == "Nanika_Trib_2":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'nanikatrib2', 'nanikatrib2')

	# if fc == "Nanika_Trib_3":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'nanikatrib3', 'nanikatrib3')
		
	# if fc == "Nanika_Trib_4":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'nanikatrib4', 'nanikatrib4')

	# if fc == "Nata_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'nata', 'nata')
		
	# if fc == "Natowite_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'natowite', 'natowite')
		
	# if fc == "Ney_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'ney', 'ney')

	# if fc == "Nicholson_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'nicholson', 'nicholson')
		
	# if fc == "Nikun_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'nikun', 'nikun')

	# if fc == "Nizik_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'nizik', 'nizik')
		
	# if fc == "No_Mans_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'nomans', 'nomans')
		
	# if fc == "North_Spit_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'northspit', 'northspit')

	# if fc == "Nugget_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'nugget', 'nugget')
		
	# if fc == "Objective_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'objective', 'objective')

	# if fc == "One_Mile_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'onemile', 'onemile')
		
	# if fc == "Ootsa_Lake":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'ootsa', 'ootsa')
		
	# if fc == "Othello_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'othello', 'othello')

	# if fc == "Owen_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'owen', 'owen')
		
	# if fc == "Owen_Trib_1":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'owentrib1', 'owentrib1')

	# if fc == "Parrott_Creek":
		# print "Deleting fields from " + fc
		# dropFields = "SUB_BASIN"
		# arcpy.DeleteField_management(fc, dropFields)
		# print "Renaming fields from " + fc
		# arcpy.AlterField_management(fc, 'Label', 'parrott', 'parrott')
		
	if fc == "Pass_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'pass', 'pass')
		
	if fc == "Pat_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'pat', 'pat')

	if fc == "Peacock_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'peacock', 'peacock')
		
	if fc == "Perow_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'perow', 'perow')

	if fc == "Peter_Aleck_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'peter', 'peter')
		
	if fc == "Picket_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'picket', 'picket')
		
	if fc == "Pierre_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'pierre', 'pierre')

	if fc == "Pillar_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'pillar', 'pillar')
		
	if fc == "Pimpernel_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'pimpernel', 'pimpernel')

	if fc == "Puport_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'puport', 'puport')
		
	if fc == "Ramsay_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'ramsay', 'ramsay')
		
	if fc == "Redtop_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'redtop', 'redtop')

	if fc == "Richfield_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'richfield', 'richfield')
		
	if fc == "Robert_Hatch_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'robert', 'robert')

	if fc == "Robin_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'robin', 'robin')
		
	if fc == "Sakeniche_River":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'sakeniche', 'sakeniche')
		
	if fc == "Sandpiper_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'sandpiper', 'sandpiper')

	if fc == "Scallon_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'scallon', 'scallon')
		
	if fc == "Shadow_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'shadow', 'shadow')

	if fc == "Shea_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'shea', 'shea')
		
	if fc == "Shelford_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'shelford', 'shelford')
		
	if fc == "Shelford_Lake":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'shelfordlk', 'shelfordlk')

	if fc == "Shoulder_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'shoulder', 'shoulder')
		
	if fc == "Star_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'star', 'star')

	if fc == "Stepp_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'stepp', 'stepp')
		
	if fc == "Sunset_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'sunset', 'sunset')
		
	if fc == "Sweeney_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'sweeney', 'sweeney')

	if fc == "Tachek_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'tachek', 'tachek')
		
	if fc == "Tagetochlain_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'tageto', 'tageto')

	if fc == "Tagit_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'tagit', 'tagit')
		
	if fc == "Tahtsa_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'tahtsa', 'tahtsa')
		
	if fc == "Tahtsa_Reach":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'tahtsar', 'tahtsar')

	if fc == "Tahtsa_Trib_1":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'tahtsatrib1', 'tahtsatrib1')
		
	if fc == "Tahtsa_Trib_2":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'tahtsatrib2', 'tahtsatrib2')

	if fc == "Tahtsa_Trib_3":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'tahtsatrib3', 'tahtsatrib3')
		
	if fc == "Tahtsa_Trib_4":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'tahtsatrib4', 'tahtsatrib4')
		
	if fc == "Tea_Billy_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'teabilly', 'teabilly')

	if fc == "Telkwa_River":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'telkwa', 'telkwa')
		
	if fc == "Thautil_River":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'thautil', 'thautil')

	if fc == "Thompson_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'thompson', 'thompson')
		
	if fc == "Tidesley_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'tidesley', 'tidesley')
		
	if fc == "Tom_George_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'tomgeorge', 'tomgeorge')

	if fc == "Troitsa_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'troitsa', 'troitsa')
		
	if fc == "Tsah_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'tsah', 'tsah')

	if fc == "Two_Mile_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'twomile', 'twomile')
		
	if fc == "Upper_Bulkley":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'upperbulkley', 'upperbulkley')
		
	if fc == "Upper_Gosnell_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'ugosnell', 'ugosnell')

	if fc == "Upper_Guess_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'uguess', 'uguess')
		
	if fc == "Upper_Hautete_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'uhautete', 'uhautete')

	if fc == "Upper_Houston_Tommy":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'uhouston', 'uhouston')
		
	if fc == "Upper_Morice_River":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'uppermorice', 'uppermorice')
		
	if fc == "Upper_Nadina":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'unadina', 'unadina')

	if fc == "Upper_Owen_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'uowen', 'uowen')
		
	if fc == "Upper_Tahlo":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'utahlo', 'utahlo')

	if fc == "Upper_Thautil_River":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'uthautil', 'uthautil')
		
	if fc == "Utem_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'utem', 'utem')
		
	if fc == "Vallee_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'vallee', 'vallee')

	if fc == "Vivian_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'vivian', 'vivian')
		
	if fc == "Wallcott_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'wallcott', 'wallcott')

	if fc == "Watson_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'watson', 'watson')
		
	if fc == "Webster_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'webster', 'webster')
		
	if fc == "Wells_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'wells', 'wells')

	if fc == "West_Caribou_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'wcaribou', 'wcaribou')
		
	if fc == "West_Francois_Lake":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'wfrancois', 'wfrancois')

	if fc == "West_Morrison_1":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'wmorrison1', 'wmorrison1')
		
	if fc == "West_Morrison_2":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'wmorrison2', 'wmorrison2')
		
	if fc == "West_Morrison_3":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'wmorrison3', 'wmorrison3')

	if fc == "West_Mosquito_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'wmosquito', 'wmosquito')
		
	if fc == "West_No_Mans_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'wnomans', 'wnomans')

	if fc == "West_Old_Fort_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'woldfort', 'woldfort')
		
	if fc == "Whitesail":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'whitesail', 'whitesail')
		
	if fc == "Whitesail_Trib_1":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'whitestrib1', 'whitestrib1')

	if fc == "Whitesail_Trib_2":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'whitestrib2', 'whitestrib2')
		
	if fc == "Whitesail_Trib_3":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'whitestrib3', 'whitestrib3')

	if fc == "Whitesail_Trib_4":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'whitestrib4', 'whitestrib4')
		
	if fc == "Whiting_Creek":
		print "Deleting fields from " + fc
		dropFields = "SUB_BASIN"
		arcpy.DeleteField_management(fc, dropFields)
		print "Renaming fields from " + fc
		arcpy.AlterField_management(fc, 'Label', 'whiting', 'whiting')





