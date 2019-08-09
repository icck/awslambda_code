import json
import os
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

'''
ログレベル、タイムスタンプおよびリクエスト ID が含まれる
'''
def lambda_handler(event, context):
    logger.info('## event---------')
    logger.info('event')
    return {
        'statusCode': 200,
        'body': json.dumps('hello from lambda')
    }