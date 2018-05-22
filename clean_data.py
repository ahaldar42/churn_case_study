# -*- coding: utf-8 -*-
"""
Created on Tue May 22 2018

v0.4

"""

def create_bool_update_columns(df):
    """
    Input : Dataframe
    Output: None
    Description:  create new bool columns to track null values of following columns

    avg_rating_by_driver
    avg_rating_of_driver
    phone

    """

    df['IsModified_avg_rating_by_driver'] =  df['avg_rating_by_driver'].isnull()
    df['IsModified_avg_rating_of_driver'] =  df['avg_rating_of_driver'].isnull()
    df['IsModified_phone'] =  df['phone'].isnull()

    return


def clean_data(df):
    """
    Input : Dataframe
    Output: None
    Description:  Updates null values of following columns
    avg_rating_by_driver
    avg_rating_of_driver
    phone

    """

    print("Null values count before cleaning....")
    print(df.isnull().sum())



    df['avg_rating_by_driver'] .fillna(df['avg_rating_by_driver'].median(), inplace=True)
    df['avg_rating_of_driver'] .fillna(df['avg_rating_of_driver'].median(), inplace=True)
    df['phone'].fillna("iPhone", inplace=True)


    print("Null values count after cleaning....")
    print(df.isnull().sum())




    return


def dummy_data(df):
    """
    Input : Dataframe
    Output: None
    Description:  Updates and creates dummies

    """
    
    df.drop(['last_trip_date','signup_date'], axis =1, inplace=True)
    df = pd.get_dummies(df)
    df.drop(["city_King's Landing",'phone_Android'], axis =1, inplace=True)
    

    return
















