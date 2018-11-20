import os, sys
#import xl
import pandas as pd


#########################################
# Nov 20, 2018
# This program searches for excel files within directories, captures columns B and C,
# transposes the data and saves the results within output_data.csv
#########################################

# 1. Loop through each folder below the root directory
# 2. Open any excel in there
# 3. read the data and transpose it
# 4. print to a single text file


# open an output csv file for writing and store as variable named OUTFILE
outfile = open('output_data.csv','w')   

# set a counter = 0 for the first record
counter = 0

#  os.walk iterates through all files in the identified diretory including child directories
for root, dirs, files in os.walk("P:\HRFN\nk_18_346_hrf_rsea_environmental_livelihoods\env_science\1_Data 2018\Data_by HRFN_mapsheet"):
    #  for each filename found within the looping process
    for file in files:
        #  if the filename ends with xlsx 
        if file.endswith(".xlsx"):
            #  This prints the directory path and filename that is opened to the command console window
            print(os.path.join(root, file))


            #  df = pd.read_excel   This reads the excel file
            #  (os.path.join(root, file)   This is the full directory path name.  Without this it only reads the excel filename
            #  usecols="B,C",skiprows=4)   Extract only the columns B and C and skip the 1st four rows within which are a header in the excel file
            df = pd.read_excel(os.path.join(root, file), usecols="B,C",skiprows=4)
                            
            
            #  This transposes the data and saves it in a dataframe called df_trans
            df_trans = df.transpose()
            
            #  If the counter is >0 then this is every transposed row after the first one.
            #  It then drops the first row which is the tranposed column B
            #  This ensures that only the first transposed row keeps the column names and the rest only keep the data
            if counter > 0:
                #print df_trans.index[0]
                df_trans = df_trans.drop(df_trans.index[0])
                
            counter = counter + 1
             
            #  This outputs the transposed file to a csv file with no index or header added (these are internal to python)
            df_trans.to_csv(outfile, header=False, index=False)
            

outfile.close()




