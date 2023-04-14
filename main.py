import smtplib
import ssl
from email.message import EmailMessage

#the email sender is your email
email_sender = 'Your email'

#Get the 16 digit special password for your gmail 
email_password = 'Enter your details'

#write the person's email who you are sending the email to
email_receiver = 'you can use this or the array'



#Now we go into actually formatting the email
subject = 'Enter subject here'

body = """
    
Enter body of the email

"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

#The next step is to add SSL, security 
context = ssl.create_default_context()

#Log in and send the email

arrayEmails = ["email1", "email2", "email3", "email4"]

for email in arrayEmails:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email, em.as_string())
