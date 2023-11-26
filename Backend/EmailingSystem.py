from email.message import EmailMessage
import ssl
import smtplib

def sendEmail():
    print("Email System Working")
    email_sender = 'healthlinkhnc@gmail.com'
    email_password = 'vncb rday dlwg ctjh'

    email_reciever = '22-03849@g.batstate-u.edu.ph'

    subject = "H&C HealthLink Monthly Report"
    body = """
    <p style="font-size:30px;font-family:arial"><b>This is the monthly report</b></p>
    ---------------------------

    Test

    ---------------------------

            - HealthLink Team
    """

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_reciever
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    print("Email Sending")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciever, em.as_string())

