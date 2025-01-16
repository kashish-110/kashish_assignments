import json
import boto3
import csv
import io

s3 = boto3.client('s3')

def lambda_handler(event, context):
    buckets = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    print(bucket)
    print(key)

    # Get the object from S3
    response = s3.get_object(Bucket=bucket, Key=key)

    #process 
    data = response['Body'].read().decode('utf-8')
    reader = csv.DictReader(io.StringIO(data))
    next(reader) # Skip header row
    for row in reader:
        print(str.format("sepal_length={}, petal_length={}, species={}"))
