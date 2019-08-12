import json

def lambda_handler(event, context):
    print('## event---------')
    print('event')
    return {
        'statusCode': 200,
        'body': json.dumps('hello from lambda')
    }
