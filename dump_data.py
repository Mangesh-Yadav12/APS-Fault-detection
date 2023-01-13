import pymongo
import pandas as pd
import json
# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")


data_file_path = "/config/workspace/aps_failure_training_set1.csv"
Database="aps"
Collection_Name="sensor"

if __name__=="__main__":
    df = pd.read_csv(data_file_path)
    print(f"Rows and column : {df.shape}")


#convert dataframe into json so that we can dump this record into mongodb
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads( df.T.to_json()).values())
    print(json_record[0])

    #insert convert json record into mongodb