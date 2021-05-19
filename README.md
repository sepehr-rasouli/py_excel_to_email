# bulk_email

Sends emails from a spreadsheet file with columns: `name`, `email`, `subject`, `message`, e.g.

```
"name","email","subject","message"
"pallier1","christophe.pallier@gmail.com","test1","excellent"
"pallier2","christophe.pallier@inserm.fr","test2","very good"
```

## Usage:

```
bulk_email [-h] [-v | -vv ] [-s SMTP_SERVER] [-p SMTP_PORT] SPREADSHEET

-h                   show this
-s SMTP_SERVER       [default: smtp.gmail.com]
-p SMTP_PORT         [default: 465]
-v                   verbosity level

Send emails to a bunch of people.
SPREADSHEET is the name or URL of a csv, xlsx or odf file containing four columns: "name", "email", "subject" and message".
```

Examples:


    python bulk_email -h
    python bulk_email -vv emails.csv
    python bulk_email -v emails.xlsx
    python bulk_email  emails.ods
    python bulk_email -vv "https://docs.google.com/spreadsheets/d/1_J3z4RkSk5yWTUU9d91J9ZOA8eZsd_slVqyPGOK0Y1U/export?format=csv"



Note: To use the gmail smtp server, you have to check the (un)safe feature at <https://www.google.com/settings/security/lesssecureapps>


## Requirements:

    pandas
    docopt
    odfpy # only needed for ods files
