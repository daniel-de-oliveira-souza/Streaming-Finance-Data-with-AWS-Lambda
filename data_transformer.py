import json
import boto3
import random
import os
import subprocess
import sys

import yfinance as yf

def lambda_handler(event, context):

    stocks = ['FB','SHOP','BYND','NFLX','PINS','SQ','TTD','OKTA','SNAP','DDOG']
    start_date = '2021-05-11'
    end_date = '2021-05-12'
    interval = '5m'
    
    kinesis = boto3.client("kinesis", "us-east-2")
    data = []

    for stock in stocks:
        download = yf.Ticker(stock).history(start=start_date, end=end_date, interval=interval)
    
        for index, row in download.iterrows():
            dic = {"high":row["High"], "low":row["Low"], "ts":index.strftime('%Y-%m-%d %X'), "name":stock}
            as_jsonstr = json.dumps(dic)+"\n"
            print(as_jsonstr)
            kinesis.put_record(
                StreamName="daniel_data_stream",
                PartitionKey="partitionkey",
                Data=as_jsonstr
                )

    return {
        'statusCode': 200,
        'body': json.dumps(f'Done! Recorded')
    }

'''
while True:
    data = 
        
        kinesis.put_record(
            StreamName="DataCollector_DanielSouza", 
            Data=as_jsonstr_row,
            PartitionKey="partitionkey"
'''