import json
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('icck-person')

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

        return json.dumps(response, indent=4, cls=DecimalEncoder)

    except Exception as e:
        # キーが存在しない場合などの、例外処理
        logger.error(e)
        raise e


def lambda_handler(event, context):

    return put_person(event['person_id'], event['name'])
