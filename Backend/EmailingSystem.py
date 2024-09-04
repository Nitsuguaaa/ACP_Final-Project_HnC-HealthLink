from email.message import EmailMessage
import ssl
import smtplib
from MySQL03 import sqldir

def getEmailList():
    file = open(r"rsc\Lists\emailList\emailList.txt", "rt")
    listing = []

    for email in file:
        listing.append(email.strip('\n'))
    return listing

def sendEmail(email=None, sendType="all"):
    sql = sqldir.SqlCommands()

    topAddress = sql.select("topaddresstbl", fetchOne=True)
    topDisease = sql.select("topdiseasetbl", fetchOne=True)

    file = open(rf"rsc\Lists\diseaseList\{topDisease[0].lower()}.txt", "rt")
    message = ""
    for line in file:
        message += line

    print("Email System Working")
    email_sender = 'healthlinkhnc@gmail.com'
    email_password = 'REDACTED FOR SECURITY REASONS :/'

    email_reciever = 'redacted :3'

    subject = "---------H&C HealthLink Quarterly Report---------"
    body = rf"""
    Below is the quarterly report of H&C Healthlink.
    We've prepared for you the most common disease
    of the most common barangay in Batangas City.
    
    ＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
    Barangay with the most hospitalized residents:
        {topAddress[0]} with {topAddress[1]} patients in the past 4 months
    
    Most common disease recorded in {topAddress[0]}:
        Most of the residents got {topDisease[0]} in the past 4 months
        
    recommended action taken:
        {message}

   ＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
   
   with the information that the HealthLink Team has provided. You
   are now equipped with better information to take necessary action
   and increase efficiency of our city's resources.

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
            if email is not None and sendType == "one":
                print("sending to one")
                smtp.sendmail(email_sender, email, em.as_string())
            else:
                print("sending to list")
                emailList = getEmailList()
                for user in emailList:
                    print("sent to", user)
                    smtp.sendmail(email_sender, user, em.as_string())
