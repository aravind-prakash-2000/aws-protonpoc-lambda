import json

def lambda_handler(event, context):
    records= event['Records']
    print(records[0]['body'])
    print("Hello")
