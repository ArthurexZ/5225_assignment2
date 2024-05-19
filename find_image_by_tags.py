import json

import boto3

# Function for 3.2.1 ( Find images based on the tags)

dynamodb = boto3.client('dynamodb')
s3 = boto3.client('s3')
TABLE_NAME = 'ass2-image-tags'
image_bucket = 'image-trigger'
yolo_bucket = 'yolo-configs-test'


def handle_postimage(event):
    body = json.loads(event['body'])
    search_tags = body.get('tags')
    # return list(search_tags)
    response = dynamodb.scan(TableName=TABLE_NAME)
    items = response.get('Items')
    urls = []
    for i in items:
        item_tags = i.get('tags').get('L')
        for d in item_tags or []:
            tag = d.get('S')
            if tag in search_tags:
                url = i.get('s3-url').get('S')
                new_url = 'https://image-trigger.s3.amazonaws.com/' + url
                urls.append(new_url)

    return {"urls": urls}


def lambda_handler(event, context):
    # TODO implement
    httpMethod = event.get('httpMethod')
    print(httpMethod)
    response_image = handle_postimage(event)
    return {
        'statusCode': 200,
        'headers': {
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*"
        },
        'body': json.dumps(response_image)
    }
