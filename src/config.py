import os

try:
    LOCALSQS = os.environ['LOCALSQS']
except:
    LOCALSQS = "false"


SQS_QUEUE_NAME = os.environ['SQS_QUEUE_NAME']
AWS_ACCESS_KEY = os.environ['AWS_ACCESS_KEY']
AWS_SECRET_KEY = os.environ['AWS_SECRET_KEY']
BASE_DOMAIN = os.environ['BASE_DOMAIN']
