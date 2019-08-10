'''
allways faild

Response:
{
  "errorMessage": "failed!!!",
  "errorType": "Exception",
  "stackTrace": [
    "  File \"/var/task/lambda_function.py\", line 2, in lambda_handler\n    raise Exception('failed!!!')\n"
  ]
}

'''
def lambda_handler(event, context):
    raise Exception('failed!!!')
