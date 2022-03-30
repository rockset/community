# Write CSV Files to Amazon Kinesis

This project contains Python code designed to write data from CSV files to Kinesis Data Stream (KDS) in AWS.If you are building example Rockset collections you can populate the KDS with these csv files to better understand ingestion strategies, SQL Transformations, Rollups, and SQL Queries for data access.


# Files

1) <b>producer.py</b> This file is what writes data to Amazon Kinesis
2) <b> generator.py</b> This file is what actually processes the csv files into KDS
3) <b>airports.py</b> This file is used as an entry point to produce the airports_list.csv
4) <b>coordinates.py</b> This file is used as an entry point to produce the AIRPORT_COORDINATES.csv
5) <b>raw_data/</b> This folder stores the raw data from [2019-airline-delays-and-cancellations](https://www.kaggle.com/datasets/threnjen/2019-airline-delays-and-cancellations)

## Prereqs
1) Python3 installed
2) boto3 library installed

## Using the Project

To use this product first you have to have the AWS cli installed and configured with the appropriate credentials. Then you need to create your Kinesis data streams called: <b>blog_airport_coordinates</b> and <b>blog_airport_list</b>. Once you have the CLI configured and the streams created you can run the scripts using `python3 airports.csv` and `python3 coordinates.py` from the downloaded directory. This will produce the data from the csv files stored in the <b>raw_data.</b> directory to KDS.

## Getting the data to Rockset

Once the data is in KDS, you can create an integration in Rockset for Kinesis. Then create collections using the specific stream names. 
