# bulk_email

Sends emails from a csv file with columns: "name", "email", "subject", "message". 

```
Usage: bulk_email [-h] [-v | -vv ] [-s SMTP_SERVER] [-p SMTP_PORT] SPREADSHEET

-h                   show this
-s SMTP_SERVER       [default: smtp.gmail.com]
-p SMTP_PORT         [default: 465]
-v                   verbosity level

Send emails to a bunch of people.
SPREADSHEET is the name or URL of a csv, xlsx or odf file containing four columns: "name", "email", "subject" and message".
```

Examples:

    bulk_email -v emails.csv   # local file
    bulk_email -vv https://docs.google.com/spreadsheets/d/1_J3z4RkSk5yWTUU9d91J9ZOA8eZsd_slVqyPGOK0Y1U/export?format=csv


Note: To use the gmail smtp server, you have to check the (un)safe feature at <https://www.google.com/settings/security/lesssecureapps>


## Requirements:

    pandas
    docopt
    odfpy # for ods files
