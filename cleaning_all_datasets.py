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
df = pd.read_csv("broadband_long2000-2018rev.csv")


df["state"] = df["statenam"]
del df["statenam"]
df["broadband_pct"] = df["broadband"]
del df["broadband"]

df.set_index(["state"])

#Save new data to CSV
df.to_csv(r"broadband_clean.csv", index = False)


######################### SECONDARY DATASETS #################################

########################## School Enrollment #################################


##Open saved csv from downloaded census data
file = open("Raw Data/School Enrollment/School_Enrollment2018.csv","r")
df = pd.read_csv("School_Enrollment2018.csv")
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
clean_data.to_csv(r"school_enrollment_clean.csv", index = False)


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
formating_employment.to_csv(r'clean_employment_data.csv', index = False)

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

formating_income.to_csv(r'clean_income_data.csv', index = False)
