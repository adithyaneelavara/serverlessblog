import boto3
import os
import uuid
import time
import datetime
import simplejson as json
def lambda_handler(event, context):
    
    print(f'Event:::{event}')
    requestBody = event['body'];
    bodyObject = json.loads(requestBody);
    recordId = str(uuid.uuid4())
    title = bodyObject["title"]
    text = bodyObject["text"]

    print('Generating new DynamoDB record, with ID: ' + recordId)
    print('Input Text: ' + text)
    print('Selected title: ' + title)
    print('Selected published: ' + datetime.date.today().strftime("%B %Y"))
    
    #Creating new record in DynamoDB table
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['DB_TABLE_NAME'])
    table.put_item(
        Item={
            'id' : recordId,
            'content' : text,
            'title' : title,
            'sortOrder' : int(time.time()),
            'published':datetime.date.today().strftime("%B %Y"),
        }
    )
    
    return {
        "statusCode": 200,
        "headers":{"X-Requested-With":"*",
        "Access-Control-Allow-Origin":"*",
        "Access-Control-Allow-Methods":"POST,GET,OPTIONS",
        "Access-Control-Allow-Headers":"Content-Type,X-Amz-Date,Authorization,X-Api-Key,x-requested-with"},
        "body": json.dumps(recordId),
     }