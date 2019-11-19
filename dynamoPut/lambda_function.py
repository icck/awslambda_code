import json
import boto3
import logging
import decimal

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('icck-person')

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

def get_person(id):
    respose = table.get_item(
            Key={
                'person_id':id
            }
        )
    return respose['Item']

def put_person(id, name):
    try:
        additional_item = {
            'person_id':id,
            'name':name
        }

        response = table.put_item(
            Item=additional_item,
            ConditionExpression='attribute_not_exists(person_id)'
        )

        logger.info('PutItem succeeded:')
        logger.info(json.dumps(response, indent=4, cls=DecimalEncoder))
        return json.dumps(response, indent=4, cls=DecimalEncoder)

    except Exception as e:
        # キーが存在しない場合などの、例外処理
        logger.error(e)
        raise e

def lambda_handler(event, context):
    put_person(event['person_id'], event['name'])

    return get_person(event['person_id']) 
