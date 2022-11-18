import json
import os
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
dynamodb = boto3.resource('dynamodb')
dbName = os.environ['ddbName']
table = dynamodb.Table(dbName)

def handler(event, context):
    logger.info(event)
    body = json.loads(event['body'])
    logger.info(body)

    item = {
        'short_url': body['id'],
        'long_url': body['long_url'],
        'owner': body['owner']
    }

    table.put_item(Item=item)
    logger.info("Record inserted into the DB")

    return {
        "statusCode": 200,
        "body": json.dumps(item)
    }  