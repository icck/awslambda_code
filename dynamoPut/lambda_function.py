import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('icck-person')

def get_person(id):
    respose = table.get_item(
            Key={
                'person_id':id
            }
        )
    return respose['Item']

def put_person(id, name)
    try:
        additional_item = {
            'person_id':id,
            'name':name
        }

        response = table.put_item(
            Item=additional_item,
            ConditionExpression='attribute_not_exists(person_id) AND attribute_not_exists(name)'
        )

    except Exception:


def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

