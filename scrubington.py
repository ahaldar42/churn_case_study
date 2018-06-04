#----------------------------------------------------------
#   Include All Imports Below:
#----------------------------------------------------------
import pandas as pd


#----------------------------------------------------------
#   Set Global Switches Below:
#----------------------------------------------------------
read_og_data = 1
get_dummies = 1
 

if read_og_data:
    data_path = "./data/churn_train.csv"
else:
    data_path = "./data/churn_train_churn.csv"


#----------------------------------------------------------
#   Read In Data (add target based on switch)
#----------------------------------------------------------
if read_og_data:
    churn_orig = pd.read_csv(data_path, parse_dates=['last_trip_date'])
    churn_orig['churn'] = churn_orig.last_trip_date.apply(lambda x: x.month)<6
else:
    churn_orig = pd.read_csv(data_path)

churn = churn_orig.copy()


#----------------------------------------------------------
#   Dropping First/Last Dates (strings) 
#----------------------------------------------------------
churn = churn.drop(['signup_date', 'last_trip_date'], axis=1)
    

#----------------------------------------------------------
#   Fill Values
#----------------------------------------------------------
churn['avg_rating_by_driver'] .fillna(churn['avg_rating_by_driver'].median(), inplace=True)
churn['avg_rating_of_driver'] .fillna(churn['avg_rating_of_driver'].median(), inplace=True)
churn['phone'].fillna("iPhone", inplace=True)


#----------------------------------------------------------
#   Get Dummies (Phone and City)
#----------------------------------------------------------
if get_dummies:
    churn = pd.get_dummies(churn)
    churn = churn.drop(["city_King's Landing",'phone_Android'], axis =1)



#----------------------------------------------------------
#   Output Scrubbed CSV
#----------------------------------------------------------
churn.to_csv('data/scrubbed.csv', index=False)