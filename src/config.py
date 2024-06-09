import os

try:
    LOCALSQS = os.environ['LOCALSQS']
except:
    LOCALSQS = "false"


SQS_QUEUE_NAME = os.environ['SQS_QUEUE_NAME']
AWS_ACCESS_KEY = os.environ['AWS_ACCESS_KEY']
AWS_SECRET_KEY = os.environ['AWS_SECRET_KEY']
BASE_DOMAIN = os.environ['BASE_DOMAIN']

EMAIL_IP = os.environ['EMAIL_IP']
# should default to 25 if not set
EMAIL_PORT = os.environ.get('EMAIL_PORT', 25)
