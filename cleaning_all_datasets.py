#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 09:17:57 2022

@author: milliesymns
"""
# PACKAGES IMPORT
import pandas as pd
import numpy as np

############################# MAIN DATASETS #################################

################################# Broadband #################################
#opened from csv from downloaded 
file = open("Raw Data/Broadband/broadband_long2000-2018rev.csv","r")
df = pd.read_csv("Raw Data/Broadband/broadband_long2000-2018rev.csv")


df["state"] = df["statenam"]
del df["statenam"]
df["broadband_pct"] = df["broadband"]
del df["broadband"]

df.set_index(["state"])

#Save new data to CSV
df.to_csv(r"Initial Clean Data/broadband_clean.csv", index = False)


################### Computer Type and Internet ################################

# importing raw data
df = pd.read_csv('Raw Data/Computer Type and Internet/ACSST1Y2018.S2301_data_with_overlays_2022-01-19T094603.csv')

#Formatting columns
Subs_formatted = df
Subs_formatted = Subs_formatted.iloc[1: , :]
Subs_formatted[['county', 'state']] = Subs_formatted['NAME'].str.split(',', expand=True)
Subs_formatted = Subs_formatted.drop('NAME', 1)


overall_pop_EST_data_Subs = Subs_formatted[["GEO_ID", "county", "state",'S2301_C01_001E', 'S2301_C01_002E', 'S2301_C01_003E',
       'S2301_C01_004E', 'S2301_C01_005E', 'S2301_C01_006E', 'S2301_C01_007E',
       'S2301_C01_008E', 'S2301_C01_009E', 'S2301_C01_010E', 'S2301_C01_011E',
       'S2301_C01_012E', 'S2301_C01_013E', 'S2301_C01_014E', 'S2301_C01_015E',
       'S2301_C01_016E', 'S2301_C01_017E', 'S2301_C01_018E', 'S2301_C01_019E',
       'S2301_C01_020E', 'S2301_C01_021E', 'S2301_C01_022E', 'S2301_C01_023E',
       'S2301_C01_024E', 'S2301_C01_025E', 'S2301_C01_026E', 'S2301_C01_027E',
       'S2301_C01_028E', 'S2301_C01_029E', 'S2301_C01_030E', 'S2301_C01_031E',
       'S2301_C02_001E', 'S2301_C02_002E', 'S2301_C02_003E', 'S2301_C02_004E',
       'S2301_C02_005E', 'S2301_C02_006E', 'S2301_C02_007E', 'S2301_C02_008E',
       'S2301_C02_009E', 'S2301_C02_010E', 'S2301_C02_011E', 'S2301_C02_012E',
       'S2301_C02_013E', 'S2301_C02_014E', 'S2301_C02_015E', 'S2301_C02_016E',
       'S2301_C02_017E', 'S2301_C02_018E', 'S2301_C02_019E', 'S2301_C02_020E',
       'S2301_C02_021E', 'S2301_C02_022E', 'S2301_C02_023E', 'S2301_C02_024E',
       'S2301_C02_025E', 'S2301_C02_026E', 'S2301_C02_027E', 'S2301_C02_028E',
       'S2301_C02_029E', 'S2301_C02_030E', 'S2301_C02_031E']]



overall_pop_EST_dict = {
                "S2301_C01_001E":"est_total_households", 
                "S2301_C01_002E":"est_total_households_with_Device", 
                "S2301_C01_003E":"est_total_households_with_Desktop", 
                "S2301_C01_004E":"est_total_households_with_NO",
                "S2301_C01_005E":"est_total_households_with_Smartphone",
                "S2301_C01_006E":"est_total_households_with_NO2",
                "S2301_C01_007E":"est_total_households_with_Portable", 
                "S2301_C01_008E":"est_total_households_with_NO3", 
                "S2301_C01_009E":"est_total_households_with_Other",
                "S2301_C01_010E":"est_total_households_with_NO4", 
                "S2301_C01_011E":"est_total_households_None", 
                "S2301_C01_012E":"est_total_households_with_SUB", 
                'S2301_C01_013E':"est_total_households_with_DU",
                'S2301_C01_014E': "est_total_households_with_Broadband",
                'S2301_C01_015E':"est_total_households_with_Cellular",
                'S2301_C01_016E':"est_total_households_with_Cell_NO",
                'S2301_C01_017E':"est_total_households_with_Cable",
                'S2301_C01_018E':"est_total_households_with_SAT",
                'S2301_C01_019E':"est_total_households_without_SUB",
                'S2301_C01_020E':"est_total_20k_households",
                'S2301_C01_021E':"est_total_20k_households_with_DU",
                'S2301_C01_022E':"est_total_20k_households_with_Broadband",
                'S2301_C01_023E':"est_total_20k_households_without_SUB",
                'S2301_C01_024E':"est_total_under75k_households",
                'S2301_C01_025E':"est_total_under75k_households_with_DU",
                'S2301_C01_026E':"est_total_under75k_households_with_BB",
                'S2301_C01_027E':"est_total_under75k_households_without_SUB",
                'S2301_C01_028E':"est_total_75k_households",
                'S2301_C01_029E':"est_total_75k_households_with_DU",
                'S2301_C01_030E':"est_total_75k_households_with_BB",
                'S2301_C01_031E':"est_total_75k_households_without_SUB",
                "S2301_C02_001E":"PCT_total_households", 
                "S2301_C02_002E":"PCT_total_households_with_Device", 
                "S2301_C02_003E":"PCT_total_households_with_Desktop", 
                "S2301_C02_004E":"PCT_total_households_with_NO",
                "S2301_C02_005E":"PCT_total_households_with_Smartphone",
                "S2301_C02_006E":"PCT_total_households_with_NO2",
                "S2301_C02_007E":"PCT_total_households_with_Portable", 
                "S2301_C02_008E":"PCT_total_households_with_NO3", 
                "S2301_C02_009E":"PCT_total_households_with_Other",
                "S2301_C02_010E":"PCT_total_households_with_NO4", 
                "S2301_C02_011E":"PCT_total_households_None", 
                "S2301_C02_012E":"PCT_total_households_with_SUB", 
                'S2301_C02_013E':"PCT_total_households_with_DU",
                'S2301_C02_014E':"PCT_total_households_with_Broadband",
                'S2301_C02_015E':"PCT_total_households_with_Cellular",
                'S2301_C02_016E':"PCT_total_households_with_Cell_NO",
                'S2301_C02_017E':"PCT_total_households_with_Cable",
                'S2301_C02_018E':"PCT_total_households_with_SAT",
                'S2301_C02_019E':"PCT_total_households_without_SUB",
                'S2301_C02_020E':"PCT_total_20k_households",
                'S2301_C02_021E':"PCT_total_20k_households_with_DU",
                'S2301_C02_022E':"PCT_total_20k_households_with_Broadband",
                'S2301_C02_023E':"PCT_total_20k_households_without_SUB",
                'S2301_C02_024E':"PCT_total_under75k_households",
                'S2301_C02_025E':"PCT_total_under75k_households_with_DU",
                'S2301_C02_026E':"PCT_total_under75k_households_with_BB",
                'S2301_C02_027E':"PCT_total_under75k_households_without_SUB",
                'S2301_C02_028E':"PCT_total_75k_households",
                'S2301_C02_029E':"PCT_total_75k_households_with_DU",
                'S2301_C02_030E':"PCT_total_75k_households_with_BB",
                'S2301_C02_031E':"PCT_total_75k_households_without_SUB",
                          }

overall_pop_EST_data_Subs.rename(columns=overall_pop_EST_dict, inplace=True)

# Creating an estimates df
EST_df = overall_pop_EST_data_Subs.copy()
EST_df = EST_df.drop(columns = EST_df.columns.astype(str)[EST_df.columns.str.contains("PCT")], axis =1, inplace = False)
#EST_df = EST_df.set_index('GEO_ID')

# Creating a percents df
PCT_df = overall_pop_EST_data_Subs.copy()
PCT_df = PCT_df.drop(columns = PCT_df.columns.astype(str)[PCT_df.columns.str.contains("est")], axis =1, inplace = False)
#PCT_df = PCT_df.set_index('GEO_ID')


#Saving to new csv for seprate estimates and percents
EST_df.to_csv(r"Initial Clean Data/est_computer_internet_data_clean.csv", index = False)
PCT_df.to_csv(r"Initial Clean Data/pct_computer_internet_data_clean.csv", index = False)


########################## Population Data #################################

#Open saved csv from downloaded census data
file = open("Raw Data/Population/pop_data.csv","r")
df = pd.read_csv("Raw Data/Population/pop_data.csv")
pd.set_option('display.max_columns', None)

#Remove header row to get row 1 as headers 
df.columns = df.iloc[0]
data = df.drop(labels=0, axis=0)

#Dropping all irrelevant columns by creating a new dataframe with usable data
clean_data = data[["id", "Geographic Area Name"," !!Total:"]]
clean_data = clean_data.rename(columns = {" !!Total:":"pop_total"})

#Split county and state name columns to be compatible with other data
clean_data[["county", "state"]] = clean_data["Geographic Area Name"].str.split(',', expand=True)
clean_data = clean_data.drop("Geographic Area Name", 1)

#reformating state
clean_data["state"] = clean_data["state"].astype(str)
clean_data["state"] = clean_data["state"].str.lstrip()

#reformating pop
clean_data["pop_total"] = clean_data["pop_total"].astype(int)

#creating urban vs rural population classification
def pop_type(pop_total):
    """Assign labels to county according to their population size
    """
    if pop_total < 10000:
        label = "Rural Area"
    elif pop_total < 49999: #Between 10,000 to 49,999
        label = "Micro Area"
    else: #Greater than 50k
        label = "Metro Area"
    return label

#applying the labels
clean_data["pop_class"] = clean_data["pop_total"].apply(pop_type)

#Save new data to CSV
clean_data.to_csv(r"Initial Clean Data/pop_data_clean.csv", index = False)

######################### SECONDARY DATASETS #################################

########################## School Enrollment #################################


##Open saved csv from downloaded census data
file = open("Raw Data/School Enrollment/School_Enrollment2018.csv","r")
df = pd.read_csv("Raw Data/School Enrollment/School_Enrollment2018.csv")
pd.set_option('display.max_columns', None)

##Remove header row to get row 1 as headers 
df.columns = df.iloc[0]
data = df.drop(labels=0, axis=0)

##Dropping all irrelevant columns by creating a new dataframe with usable data
clean_data = data[["id", "Geographic Area Name",'Estimate!!Total!!Population 3 years and over enrolled in school!!Kindergarten to 12th grade',
                       "Estimate!!Percent!!Population 3 years and over enrolled in school!!Kindergarten to 12th grade",
                  "Margin of Error!!Total MOE!!Population 3 years and over enrolled in school!!Kindergarten to 12th grade"]]

clean_data = clean_data.rename(columns = {"Estimate!!Total!!Population 3 years and over enrolled in school!!Kindergarten to 12th grade":"Total Pop Enrolled",
                                        "Estimate!!Percent!!Population 3 years and over enrolled in school!!Kindergarten to 12th grade": "Percent Total Pop Enrolled",
                                         "Margin of Error!!Total MOE!!Population 3 years and over enrolled in school!!Kindergarten to 12th grade": "Margin Total Pop"
                                        })

##Split county and state name columns to be compatible with other data
clean_data[["County", "State"]] = clean_data["Geographic Area Name"].str.split(',', expand=True)
clean_data = clean_data.drop("Geographic Area Name", 1)

##Save new data to CSV
clean_data.to_csv(r"Initial Clean Data/school_enrollment_clean.csv", index = False)


################################ Employment #################################

### open employment csv files
with open('Raw Data/Employment/ACSST1Y2018.S2301_data_with_overlays_2022-01-19T094603.csv') as f:
    raw_employment =  pd.read_csv(f, delimiter=',')
    
#with open('Employment Data/ACSST1Y2019.S2301_metadata_2021-12-15T185326.csv') as f:  
    #raw_employment_ids = pd.read_csv(f, delimiter=',')
    

### Cleaning employment data    
formating_employment = raw_employment

#dropping the first row with the ID information 
formating_employment = formating_employment.iloc[1: , :]

#dropping US total data for now 
formating_employment = formating_employment[formating_employment['NAME'] != 'United States']

#spliting county and state into separate columns and dropping 'NAME' column
formating_employment[['county', 'state']] = formating_employment['NAME'].str.split(',', expand=True)
formating_employment = formating_employment.drop('NAME', 1)

#Replacing all the 'N' with NAN
formating_employment = formating_employment.replace('N', np.NaN)
formating_employment = formating_employment.replace('*****', np.NaN)

#Converting all true numeric variables to float NOTE: RUNNING INTO ISSUE HERE
formating_employment = pd.DataFrame(formating_employment)
formating_employment = formating_employment.infer_objects()

#Explorting inital clean employment data
formating_employment.to_csv(r'Initial Clean Data/clean_employment_data.csv', index = False)

###################################### Income #################################

### open income csv files
with open('Raw Data/Income/ACSST1Y2018.S1901_data_with_overlays_2022-01-19T095723.csv') as f:
    raw_income =  pd.read_csv(f, delimiter=',')
    
#with open('Income Data/ACSST1Y2019.S1901_metadata_2021-11-04T144153.csv') as f:  
    #income_ids = pd.read_csv(f, delimiter=',')
    
    
formating_income = raw_income

#dropping the first row with the ID information 
formating_income = formating_income.iloc[1: , :]

#dropping US total data for now 
#formating_income = formating_income[formating_income['NAME'] != 'United States']

#spliting county and state into separate columns and dropping 'NAME' column
formating_income[['county', 'state']] = formating_income['NAME'].str.split(',', expand=True)
formating_income = formating_income.drop('NAME', 1)

#Replacing all the 'N' with NAN
formating_income = formating_income.replace('N', np.NaN)
formating_income = formating_income.replace('*****', np.NaN)

#Converting all true numeric variables to float NOTE: RUNNING INTO ISSUE HERE

formating_income = pd.DataFrame(formating_income)
formating_income = formating_income.infer_objects()

#Explorting inital clean income data

formating_income.to_csv(r'Initial Clean Data/clean_income_data.csv', index = False)


###################################### Income #################################

### open households csv files
with open('Raw Data/Households and Families/ACSST1Y2018.S1101_data_with_overlays_2022-01-27T105511.csv') as f:
    raw_households =  pd.read_csv(f, delimiter=',')

### Cleaning households data    
formating_households = raw_households

#dropping the first row with the ID information 
formating_households = formating_households.iloc[1: , :]

#dropping US total data for now 
formating_households = formating_households[formating_households['NAME'] != 'United States']

#splitting county and state into separate columns and dropping 'NAME' column
formating_households[['county', 'state']] = formating_households['NAME'].str.split(',', expand=True)
formating_households = formating_households.drop('NAME', 1)

#Replacing all the 'N' with NAN
formating_households = formating_households.replace('N', np.NaN)
formating_households = formating_households.replace('*****', np.NaN)

#Converting all true numeric variables to float NOTE: RUNNING INTO ISSUE HERE
formating_households = pd.DataFrame(formating_households)
formating_households = formating_households.infer_objects()

#Extracting only necessary columns
household_cols = formating_households[['GEO_ID', 'S1101_C01_001E', 'S1101_C01_002E', 
                                       'S1101_C01_003E', 'S1101_C01_004E']]

household_dict = {"GEO_ID": "geo_id",
                  "S1101_C01_001E":"est_total_households_official",
                  "S1101_C01_002E":"est_avg_household_size",
                  "S1101_C01_003E":"est_total_families_official",
                  "S1101_C01_004E":"est_avg_families_size"
                          }

household_cols.rename(columns=household_dict, inplace=True)

#Exporting initial clean households data
household_cols.to_csv(r'Initial Clean Data/clean_households_data.csv', index = False)
