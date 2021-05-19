#! /bin/sh

python bulk_email -h
python bulk_email -vv emails.csv
python bulk_email -v emails.xlsx
python bulk_email  emails.ods
python bulk_email -vv https://docs.google.com/spreadsheets/d/1_J3z4RkSk5yWTUU9d91J9ZOA8eZsd_slVqyPGOK0Y1U/export?format=csv
