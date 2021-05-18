#! /usr/bin/env python

"""Usage: bulk_email.py [-s SMTP_SERVER] [-p SMTP_PORT] CSV_FILE

-h              show this
-s SMTP_SERVER  [default: smtp.gmail.com]
-p SMTP_PORT    [default: 465]

Send emails to a bunch of people. CSV_FILE should contain 3 columns: "name", "email", "message". 
"""

from docopt import docopt
from getpass import getpass
import pandas
import smtplib

args = docopt(__doc__)
spreadsheet = args['CSV_FILE']
smtp_server = args['-s']
smtp_port = args['-p']

# Get the names, email_addresses and messages from the spreadsheet
df = pandas.read_csv(spreadsheet)

# Establishes the connection with the SMTP server
sender_email = input(f"Connection to {smtp_server}:{smtp_port}...\nlogin: ")
sender_password = getpass()

server = smtplib.SMTP_SSL(smtp_server, smtp_port)  # TODO: should catch exceptions
server.ehlo()
server.login(sender_email, sender_password)

# Send the emails
topic = 'PCBS FEEDBACK'

for name, email_address, message in zip(df.name, df.email, df.message):
    server.sendmail(sender_email, [email_address], 
                   """To: {email_address}\r\n
                      Subject: {topic}\n\n{message}""")

# close the smtp server
server.quit()
