import arcpy
import os
from arcpy import env


# set workspace
arcpy.env.workspace = r"P:\\canfor\\KE-13-053-CFP_Morice_TSR_Review\\gis\\resultant_2019\\seamless\\SBA watersheds_labelled\\SBA.gdb"


#Create list of geodatabase layers

inFeatures = ["Ailport_Creek", "Allin_Creek", "Andrew_Creek", "Atiken_Creek", "Atna_River", "Babine_Lake", "Barge_Creek", "Bell_Creek", "Bergeland_Creek", "Big_Loon_Creek", "Boucher_Creek", "Buck_Creek", "Burnie_River", "Bymac_Creek", "Byron_Creek", "Canyon_Creek","Caribou_Creek", "Caribou_Mountain_Creek", "Carl_Borden_Creek", "Cedric_Creek", "Cesford_Creek", "Char_Creek","Chickamin_Creek", "Clore_River", "Coffin_Creek", "Coles_Creek", "Coles_Lake", "Covert_Creek", "Crona_Creek", "Crow_Creek", "Crystal_Creek", "Cummins_Creek", "Deasy_Creek", "Deep_Creek", "Denys_Creek", "Desdemona_Creek", "Dockrill_Creek", "DuBose_Creek", "Dungate_Creek", "East_Caribou_Creek", "East_Gates_Creek", "East_Hautete_Lake", "East_Kasalka_Creek", "East_Mosquito_Creek", "East_Nakinilerak_Creek", "East_Old_Fort_Creek", "Elliot_Creek", "Elwin_Creek", "Emerson_Creek", "False_Chelaslie_Creek", "False_Tagit_Creek", "Fenton_Creek", "Fenton_Nanika_Creek", "Fenton_Nanika_Creek_South", "Findlay_Lake", "Five_Mile_Creek", "Fleming_Creek", "Fort_Babine_Creek", "Francois_Lake", "Friday_Creek", "Frypan_Creek", "Fulton_above_Chapman_Lake", "Fulton_River", "Gabriel_Creek", "Gloyazikut_Creek", "Goathorn_Creek", "Gold_Creek", "Gosnell_Creek", "Guess_Creek", "Hagarty_Creek", "Hagman_Creek", "Haul_Creek", "Hautete_Creek", "Haymeadow_Creek", "Henkel_Creek", "Herb_Dome_Creek", "Holland_Creek", "Holmes_Creek", "Houston_Tommy_Creek", "Houston_Tommy_Trib_1", "Houston_Tommy_Trib_2", "Howson_Creek", "Jinx_Creek", "Johnny_David_Creek", "Joshua_Creek", "Kasalka_Creek", "Kew_Creek", "Kidprice_Lake", "Kivi_Creek", "Klo_Creek", "Knapper_Creek", "Lamprey_Creek", "Laventie_Creek", "Lemieux_Creek", "Lindquist_Creek", "Little_Bulkley", "Little_Cumulus_Creek", "Little_Loon_Creek", "Long_Island_Creek", "Lower_Talho", "Matzehtzel_Creek", "Mcbride_Creek", "Mccuish_Creek", "McQuarrie_Creek", "Moose_Flats_Creek", "Moose_Skin_Creek", "Morice_River", "Morice_Trib_1", "Morice_Trib_2", "Morrison_Creek", "Nadina_River", "Nado_Creek", "Nanika_River", "Nanika_Trib_1", "Nanika_Trib_2", "Nanika_Trib_3", "Nanika_Trib_4", "Nata_Creek", "Natowite_Creek", "Ney_Creek", "Nicholson_Creek", "Nikun_Creek", "Nizik_Creek", "No_Mans_Creek", "North_Spit_Creek", "Nugget_Creek", "Objective_Creek", "One_Mile_Creek", "Ootsa_Lake", "Othello_Creek", "Owen_Creek", "Owen_Trib_1", "Parrott_Creek", "Pass_Creek", "Pat_Creek", "Peacock_Creek", "Perow_Creek", "Peter_Aleck_Creek", "Picket_Creek", "Pierre_Creek", "Pillar_Creek", "Pimpernel_Creek", "Puport_Creek", "Ramsay_Creek", "Redtop_Creek", "Richfield_Creek", "Robert_Hatch_Creek", "Robin_Creek", "Sakeniche_River", "Sandpiper_Creek", "Scallon_Creek", "Shadow_Creek", "Shea_Creek", "Shelford_Creek", "Shelford_Lake", "Shoulder_Creek", "Star_Creek", "Stepp_Creek", "Sunset_Creek", "Sweeney_Creek", "Tachek_Creek", "Tagetochlain_Creek", "Tagit_Creek", "Tahtsa_Creek", "Tahtsa_Reach", "Tahtsa_Trib_1", "Tahtsa_Trib_2", "Tahtsa_Trib_3", "Tahtsa_Trib_4", "Tea_Billy_Creek", "Telkwa_River", "Thautil_River", "Thompson_Creek", "Tidesley_Creek", "Tom_George_Creek", "Troitsa_Creek", "Tsah_Creek", "Two_Mile_Creek", "Upper_Bulkley", "Upper_Gosnell_Creek", "Upper_Guess_Creek", "Upper_Hautete_Creek", "Upper_Houston_Tommy", "Upper_Morice_River", "Upper_Nadina", "Upper_Owen_Creek", "Upper_Tahlo", "Upper_Thautil_River", "Utem_Creek", "Vallee_Creek", "Vivian_Creek", "Wallcott_Creek", "Watson_Creek", "Webster_Creek", "Wells_Creek", "West_Caribou_Creek", "West_Francois_Lake", "West_Morrison_1", "West_Morrison_2", "West_Morrison_3", "West_Mosquito_Creek", "West_No_Mans_Creek", "West_Old_Fort_Creek", "Whitesail", "Whitesail_Trib_1", "Whitesail_Trib_2", "Whitesail_Trib_3", "Whitesail_Trib_4","Whiting_Creek"]

outFeatures = "watersheds_union"

arcpy.Union_analysis (inFeatures, outFeatures, "NO_FID")





