
import twitter

# os.environ.get('')を利用してキーを設定する
auth = twitter.OAuth(consumer_key="",
consumer_secret="",
token="",
token_secret="")

def lambda_handler(event, context):
    t = twitter.Twitter(auth=auth)
    status="Hello,World" #投稿するツイート
    t.statuses.update(status=status) #Twitterに投稿
