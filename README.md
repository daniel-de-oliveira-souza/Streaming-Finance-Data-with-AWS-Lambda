# Streaming-Finance-Data-with-AWS-Lambda
Provisioning a Lambda function to generate near real time finance data records for interactive querying

This project consists of three major infrastructure elements:

A lambda function that gathers our data (DataTransformer)
A Kinesis stream that holds our data (DataCollector)
A serverless process that allows us to query our S3 data (DataAnalyzer)

![STA9760F2020_ Project 3 Diagram](/Users/danisouza/Downloads/STA9760F2020_ Project 3 Diagram.jpg)

First, I have created a AWS Lambda function called Data Collector, to collect one full day's worth of stock HIGH and LOW prices for each of the companies listed below, on Tuesday, May 11th, 2021. This function transforms the stock data into a JSON format. Once transformed, the data is streamlined into a S3 bucket.

1. Facebook (FB)
2. Shopify (SHOP)
3. Beyond Meat (BYND)
4. Netflix (NFLX)
5. Pinterest (PINS)
6. Square (SQ)
7. The Trade Desk (TTD)
8. Okta (OKTA)
9. Snap (SNAP)
10. Datadog (DDOG)

Later, I took advantage of AWS Glue and AWS Athena to create a serverless process to query the stock data that was in the S3 bucket. These queries result in a csv file that contains the highest hourly stock HIGH per company from the list previously mentioned.

Lastly, but not least, I took advantage of a Jupyter Notebook to create a few visualizations to further understand the stock data.

## Data Collector Lambda Configuration

![Screen Shot 2021-05-20 at 9.36.37 PM](/Users/danisouza/Library/Application Support/typora-user-images/Screen Shot 2021-05-20 at 9.36.37 PM.png)

## Kinesis Firehose Delivery Stream Monitoring

![Screen Shot 2021-05-20 at 9.36.07 PM](/Users/danisouza/Library/Application Support/typora-user-images/Screen Shot 2021-05-20 at 9.36.07 PM.png)
