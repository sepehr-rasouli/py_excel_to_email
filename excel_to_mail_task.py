# Python code to send email to a list of
# emails from a spreadsheet

# import the required libraries
import pandas as pd
import smtplib

# change these as per use
your_email = "XYZ@gmail.com"
your_password = "YOUR_PASSWORD"

# establishing connection with gmail
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(your_email, your_password)

# reading the spreadsheet
email_list = pd.read_excel('path/comment_sheet.xlsx',
     engine='openpyxl',
                           )
# getting the names and the emails
names = email_list['NAME']
emails = email_list['EMAIL']
comments = email_list['COMMENT']
# change the subject if neccassary
subject = 'PCBS FEEDBACK'
# iterate through the records
for i in range(len(emails)):
    # for every record get the name and the email addresses
    name = names[i]
    email = emails[i]
    # the message to be emailed
    message = "To: %s\r\n" % email +\
              'Subject: {}\n\n{}'.format(subject, comments[i])
    # sending the email
    server.sendmail(your_email, [email], message)

# close the smtp server
server.quit()

