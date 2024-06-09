import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Environment, FileSystemLoader


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

    # Define the environment and load the template
    env = Environment(loader=FileSystemLoader(
        searchpath=f"/opt/src/templates"))

    template = env.get_template('report.html')

    # Render the template with the provided variables
    html_content = template.render(
        formatted_address=formatted_address,
        report_url=f"{base_domain}/report/{report_id}")

    msgText = MIMEText(html_content, 'html')
    msgAlternative.attach(msgText)

    # Send the email
    smtp = smtplib.SMTP(config.EMAIL_IP, config.EMAIL_PORT)
    # smtp.login(strFrom, '')
    smtp.sendmail(strFrom, strTo, msgRoot.as_string())
    smtp.quit()
