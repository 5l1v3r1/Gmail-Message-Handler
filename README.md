# Gmail-Message-Handler

## Description
This repo is a collection of scripts in which you can send mail or mass mail using a gmail account through SMTP server

## Installation
```
git clone https://github.com/monishmonish/Gmail-Message-Handler/
cd Gmail-Message-Handler/
pip3 install -r requirements.txt
```
## Scripts In This Repo

### (1)Send mail to single ID
### (2)Send mass mail from a .txt file
### (3)Extract email IDs from a Excel/CSV file
### (4)Verify email IDs from the extracted email data

## Mail ID Settings

Some apps and devices use less secure sign-in technology.
To send emails using this script, you must follow 2 conditions
(1) Allow Less Secure Apps
(2) Disable 2 Step Verification

Check this page to modify the [Gmail](https://myaccount.google.com/u/0/security) settings

## API used to verify email ID

I used an API and checked its JSON data to verify an email address
API used : [isitarealemail](https://isitarealemail.com/api/email/validate)

