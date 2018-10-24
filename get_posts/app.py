import boto3
import os
import json
from boto3.dynamodb.conditions import Key, Attr
def runs_on_aws_lambda():
    """
        Returns True if this function is executed on AWS Lambda service.
    """
    return 'AWS_SAM_LOCAL' not in os.environ and 'LAMBDA_TASK_ROOT' in os.environ
# Patch all supported libraries for X-Ray - More info: https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-python-patching.html
if runs_on_aws_lambda():
    from aws_xray_sdk.core import xray_recorder    
    from aws_xray_sdk.core import patch_all
    patch_all()

session = boto3.Session()


def lambda_handler(event, context):
    print(f'Event::{event}')
   
    postId = event["queryStringParameters"]["postId"]
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['DB_TABLE_NAME'])

    if postId=="*":
        items = table.scan(
            Limit=10,
            Select='ALL_ATTRIBUTES'
    )
    
    else:
        items = table.query(
            KeyConditionExpression=Key('id').eq(postId)
        )
    return {
        "statusCode": 200,
        "body": items["Items"]
    }
  


# Decorator for xray
@xray_recorder.capture('## get_message_segment')
def get_message():
    """
        You can create a sub-segment specifically to a function
        then capture what sub-segment that is inside your code
        and you can add annotations that will be indexed by X-Ray
        for example: put_annotation("operation", "query_db")
    """
    # Only run xray in the AWS Lambda environment
    if runs_on_aws_lambda():
        xray_subsegment = xray_recorder.current_subsegment()
        xray_subsegment.put_annotation("key", "value")
        # Sample metadata
        # subsegment.put_metadata("operation", "metadata", "python object/json")
        xray_recorder.end_subsegment()