from __future__ import print_function
import boto3

client = boto3.client('dynamodb')
try :
    response = client.create_table(
        TableName = 'link',
        AttributeDefinitions = [
            {
            'AttributeName' : 'url',
            'AttributeType' : 'S'
            },
        ],
        KeySchema = [
            {
            'AttributeName' : 'url',
            'KeyType' : 'HASH'
            },
        ],
        ProvisionedThroughput = {
            'ReadCapacityUnits' : 1,
            'WriteCapacityUnits' : 1
        }
    )
    print("Create Table Link Status :", response['TableDescription']['TableStatus'])
except dynamodb.exceptions.ResourceInUseException:
    print("Skipping Create Table Link")
    pass


try:
    response = client.create_table(
        TableName = 'article',
        AttributeDefinitions = [
            {
            'AttributeName' : 'url',
            'AttributeType' : 'S'
            },
        ],
        KeySchema = [
            {
            'AttributeName' : 'url',
            'KeyType' : 'HASH'
            },
        ],
        ProvisionedThroughput = {
            'ReadCapacityUnits' : 1,
            'WriteCapacityUnits' : 1
        }
    )
    print("Create Table Article Status :",  response['TableDescription']['TableStatus'])
except dynamodb.exceptions.ResourceInUseException:
    print("Skipping Create Table Article")
    pass