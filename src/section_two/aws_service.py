
import datetime
import json

import requests
import pandas as pd
import boto3


def get_covid_data(url: str):
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()

def convert_to_csv(data: json):
    f_timestamp = f"""{datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")}.csv"""
    if data is not None:
        df = pd.Series(data['data']).to_frame()
        file = df.to_csv(f_timestamp)
        return f_timestamp

def upload_to_s3(file):
    s3 = boto3.resource('s3')
    
    data = open(file, 'rb')
    uploaded_file = s3.Bucket('covidtestbucket1').put_object(Key=file, Body=data)

    data.close()
    return uploaded_file


if __name__ == "__main__":

    json_data = get_covid_data(url="https://covidnigeria.herokuapp.com/api")
    csv = convert_to_csv(json_data)
    obj = upload_to_s3(csv)

    url = f"https://{obj.bucket_name}.s3.amazonaws.com/{obj.key}"
    print("Public URL:", url)