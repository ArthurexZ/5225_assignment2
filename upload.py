import json
import base64
import boto3
import time
def lambda_handler(event, context):
    s3_base_url = "https://image-trigger.s3.amazonaws.com/"
    s3 = boto3.client("s3")

    body = json.loads(event['body'])
    image = body.get('image')

    decode_image = base64.b64decode(image)

    file_name = int(round(time.time() * 1000))
    s3_upload = s3.put_object(Bucket="image-trigger", Body=decode_image, Key=str(file_name) + '.jpg')
    response = {
        "message": "Image uploaded successfully",
        "url":s3_base_url+str(file_name)+".jpg"
    }
    return {
        'statusCode': 200,
        'body': json.dumps(response),
        'headers': {
            'Access-Control-Allow-Headers': '*'
        },
        
    }

