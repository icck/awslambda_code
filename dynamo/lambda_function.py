import boto3
import json

dynamodb = boto3.resource('dynamodb')
# table_name:icck-person pk:person_id sk: Other: name
# dynamodb 作ってから実行2
table = dynamodb.Table('icck-person')

def get_person(id):
    respose = table.get_item(
            Key={
                'person_id':id
            }
        )
    return respose['Item']

def get_persons():
    response = table.scan()
    return response['Items']

def lambda_handler(event, context):
    return get_persons() if event['person_id'] == '' else get_person(event['person_id'])
