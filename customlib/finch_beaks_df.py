"""Custom reusable code to extract Finch Beaks data"""
import pandas as pd
def draw_finch_data():
    df1 = pd.read_csv(
        "C:/Users/amlan/Documents/Git Repos/Machine Learning/Neural-Networks-DataCamp/customlib/datasets/finch_beaks_1975.csv")
    df2 = pd.read_csv(
        "C:/Users/amlan/Documents/Git Repos/Machine Learning/Neural-Networks-DataCamp/customlib\datasets/finch_beaks_2012.csv")
    df = pd.concat([df1, df2], sort=False)
    bd_1975 = df1['Beak depth, mm'].values
    bd_2012 = df2['Beak depth, mm'].values
    bl_1975 = df1['Beak length, mm'].values
    bl_2012 = df2['Beak length, mm'].values

    return bd_1975, bd_2012, bl_1975, bl_2012

def drw_finch_df():
    df1 = pd.read_csv(
        "C:/Users/amlan/Documents/Git Repos/Machine Learning/Neural-Networks-DataCamp/customlib/datasets/finch_beaks_1975.csv")
    df2 = pd.read_csv(
        "C:/Users/amlan/Documents/Git Repos/Machine Learning/Neural-Networks-DataCamp/customlib\datasets/finch_beaks_2012.csv")
    df = pd.concat([df1, df2], sort=False)
    return df1 , df2, df