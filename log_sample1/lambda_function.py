import json
import os

def lambda_handler(event, context):
#    print('## env-----------')
#    print(os.version)
    print('## event---------')
    print('event')
    return {
        'statusCode': 200,
        'body': json.dumps('hello from lambda')
    }