import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

from src import config


class NewDocSqs(object):
    def __init__(self, body):
        print("doing some stuff", flush=True)
        send_email(body['email'], body['formatted address'], body['report_id'])
        print("ok finished now", flush=True)


def send_email(recipient, formatted_address, report_id):
    base_domain = config.BASE_DOMAIN
    # Define these once; use them twice!
    strFrom = 'noreply@ukpropertyreport.co.uk'
    strTo = recipient

    # Create the root message and fill in the from, to, and subject headers
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = f'Your property report for {formatted_address}'
    msgRoot['From'] = strFrom
    msgRoot['To'] = strTo
    msgRoot.preamble = 'This is a multi-part message in MIME format.'

    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    # We reference the image in the IMG SRC attribute by the ID we give it below
    msgText = MIMEText(
        f'<b>Here is your property report</b><br><br><a href="{base_domain}/report/{report_id}" style="background-color: #4CAF50; border: none; color: white; padding: 15px 32px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer;">Download Report</a>', 'html')
    msgAlternative.attach(msgText)

    # Send the email
    smtp = smtplib.SMTP('217.160.185.253', 2500)
    # smtp.login(strFrom, '')
    smtp.sendmail(strFrom, strTo, msgRoot.as_string())
    smtp.quit()
