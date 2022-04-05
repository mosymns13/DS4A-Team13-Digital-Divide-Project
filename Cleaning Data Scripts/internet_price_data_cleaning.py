#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 19:10:17 2022

@author: milliesymns
"""

# PACKAGES IMPORT
import pandas as pd


#DATA IMPORT

"""
Process done below
- Pulling in the csv files
- Triming white spaces in the "state" columns
- Merging the datasets to make one data frame with all prices
- Saving a complete csv file with all prices 

Information about the data
- This is the cost per MBPS
- Recommended MBPS is 25 or higher as a starting point
- For households with 4 or more around 100 or more is recommended
"""

cable = pd.read_csv("Raw Data/Internet Prices/cable_price.csv")
cable["state"] = cable["state"].str.strip()


fiber_optic = pd.read_csv("Raw Data/Internet Prices/fiber_optic_price.csv")
fiber_optic["state"] = fiber_optic["state"].str.strip()


dsl = pd.read_csv("Raw Data/Internet Prices/dsl_price.csv")
dsl["state"] = dsl["state"].str.strip()

#merge datasets 
set1 = cable.merge(fiber_optic, on = "state", how = "outer")
set2 = set1.merge(dsl, on = "state", how = "outer")

#cleaning column names
set2.columns = set2.columns.str.replace(' ', '')

#NOTE: Clean up later to make a loop function to write these columns
set2["cable25"] = set2["cable_price"] * 25
set2["fiber_optic25"] = set2["fiber_optic_price"] * 25
set2["dsl25"] = set2["dsl_price"] * 25

set2["cable100"] = set2["cable_price"] * 100
set2["fiber_optic100"] = set2["fiber_optic_price"] * 100
set2["dsl100"] = set2["dsl_price"] * 100


#Exporting csv file
set2.to_csv(r"Initial Clean Data/internet_price_data.csv", index = False)
