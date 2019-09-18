# to be inserted in field calculator

##############################################################
# this section to be inserted into the pre-logic script code #
##############################################################
def calc_pine_per(SPECIES_CD_1 , SPECIES_CD_2 , SPECIES_CD_3 , SPECIES_CD_4 , SPECIES_CD_5 , SPECIES_CD_6, SPECIES_PCT_1 , SPECIES_PCT_2 , SPECIES_PCT_3 , SPECIES_PCT_4 , SPECIES_PCT_5 , SPECIES_PCT_6):
	tp = 0
	spLIST = [SPECIES_CD_1 , SPECIES_CD_2 , SPECIES_CD_3 , SPECIES_CD_4 , SPECIES_CD_5 , SPECIES_CD_6]
	spPER = [SPECIES_PCT_1 , SPECIES_PCT_2 , SPECIES_PCT_3 , SPECIES_PCT_4 , SPECIES_PCT_5 , SPECIES_PCT_6]
	x = 0
	while x < 6:
		sp = spLIST[x]
		spper = spPER[x]
		if sp in ['Pl', 'Pli', 'PL', 'PLI']:
			tp += spper
		x += 1
                            
	return tp

###################################################
# this section to be inserted into the bottom box #
###################################################

calc_pine_per(!SPECIES_CD_1! , !SPECIES_CD_2! , !SPECIES_CD_3! , !SPECIES_CD_4! , !SPECIES_CD_5! , !SPECIES_CD_6!, !SPECIES_PCT_1! , !SPECIES_PCT_2! , !SPECIES_PCT_3! , !SPECIES_PCT_4! , !SPECIES_PCT_5! , !SPECIES_PCT_6!)
