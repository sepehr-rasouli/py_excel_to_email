# excel_to_mail_task
a python script that sends emails from a xlsx file

## **Package Requirements**
`python v3, pandas, smtplib`

## **Dependencies**
`pip install openpyxl`<br/>
`pip install xlrd`

## **SETUP**
* Google blocks sign-in attempts from apps which do not use modern security standards (mentioned on their support page). You should temporarily, turn on/off this safety feature by going to the link below:
Go to this link and select Turn On
[https://www.google.com/settings/security/lesssecureapps](https://www.google.com/settings/security/lesssecureapps)
(Make sure you click turn on, and not turn off!)

* if it still fails, you might need to clear Captcha: visit 
[https://accounts.google.com/DisplayUnlockCaptcha](https://accounts.google.com/DisplayUnlockCaptcha) and sign in with the Gmail username and password.  If necessary (it's usually not), enter the letters in the distorted picture then press Continue. This will allow ten minutes for the python code to register as an approved connection.  Note that you must use the account you are using in your code - if the browser is already signed into another account, you must sign out first.

* Preferably disable 2 factor authentication. If you insist on using a 2 factor authentication, you must create a password for this application to access your Google account without the 2 factor auth.
Perform all the steps on the Google support page to generate an application password, and then update the `your_password` to use that, rather than your regular account password. <br/>
On this page: [support.google.com/accounts/answer/185833]([support.google.com/accounts/answer/185833) follow the steps under the heading "How to generate an App password". After you generate it, you need to use that password in your configuration.

