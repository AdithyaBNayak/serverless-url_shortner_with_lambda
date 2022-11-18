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
    body = event['pathParameters']
    logger.info(body)

    get_record = table.get_item(
        Key= {'short_url': body['id']}
    )

    if 'Item' in get_record:
        record = get_record['Item']
        logger.info("Record got from DB")
        logger.info(record)

        response = {
            "statusCode": 302,
            "headers": {"Location": record['long_url']}
        }

    else:
        response = {
            "statusCode": 502,
            "body": "No url found for the given id"
        }

    return response 