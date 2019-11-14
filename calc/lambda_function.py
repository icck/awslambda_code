import json

def lambda_handler(event, context):
    
    x = event['x']
    y = event['y']
    print('x = ' + str(x))
    print('y = ' + str(y))
    rlt = int(x) / int(y)
    
    return {
        'statusCode': 200,
        'body': json.dumps('result: ' + str(rlt) )
    }
