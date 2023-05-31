# import smtplib
# from email.message import EmailMessage

# SENDER_EMAIL = "omkar.musale19@pccoepune.org"
# APP_PASSWORD = "72026480E"


# print("Mail Start")
# msg = EmailMessage()
# msg['Subject'] = "Accident Event Detection"
# msg['From'] = SENDER_EMAIL
# msg['To'] = "omkarmusaleich@gmail.com"
# msg.set_content('Accident Event Detected')


# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#         smtp.login(SENDER_EMAIL, APP_PASSWORD)
#         smtp.send_message(msg)
#         print("Mail send successfully")



import smtplib

# Set up sender and recipient email addresses
sender_email = 'omkarmusaleich@gmail.com'
recipient_email = 'omkarmusaleich@gmail.com'

# Create the email message
message = '''Subject: College project\n\nAccident Event Detection.'''

# Log in to SMTP server and send email
password = 'nnqviygbmbfnjbur'
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login(sender_email, password)
    smtp.sendmail(sender_email, recipient_email, message)

print('Email sent!')
