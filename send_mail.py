import getpass
import sys,time,os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from verify_email import verify_email

smtp_host='smtp.gmail.com'
smtp_port=587

def send_mail(sender,password,receiver):
    mb=MIMEMultipart()
    subject=input("[+] Enter your Subject : ")
    mb['Subject']=subject
    print("*"*60)
    choice=input("(A)Text\t(B)HTML\n[+] Enter your message type : ")
    print("*"*60)
    message=input("[+] Enter your message below :\n")
    if choice=='A' or choice=='a':
        text=MIMEText('text','plain')
        text.set_payload(message)
        mb.attach(text)
    elif choice=='B' or choice=='b':
        text=MIMEText('text','html')
        text.set_payload(message)
        mb.attach(text)
    else:
        print("[+] Enter correct choice..")
        print("[+] Exiting..")
        sys.exit()
    
    session=smtplib.SMTP(smtp_host,smtp_port)
    session.ehlo()
    session.starttls()
    session.ehlo()
    session.login(sender,password)
    session.sendmail(sender,receiver,mb.as_string())
    print("[+] Email sent successfully...")
    session.quit()

if __name__ == "__main__":
    print("< Gmail-Python Script >")
    print("Allow Less Secure Apps In Google To Authenticate Successfully !!")
    print("If haven't done visit this url --> https://myaccount.google.com/u/1/lesssecureapps?pli=1&pageId=none")
    print("*"*60)
    print("LOGIN :")
    sender=input("[+] Enter your Gmail username : ")
    password=getpass.getpass(prompt="[+] Enter your Gmail password : ")
    print("*"*60)
    receiver=input("[+] Enter your recipient mail ID : ")
    print("*"*60)
    valid=verify_email(receiver)
    if valid:
        print("[+] Email verified successfully")
        send_mail(sender,password,receiver)
    else:
        print("[+] Cannot process recipient email id")
    