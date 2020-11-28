import getpass
import sys,time,os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_host='smtp.gmail.com'
smtp_port=587

def send_mail(sender,password,receiver,choice):
    mb=MIMEMultipart()
    mb['Subject']=subject
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
    subject=input("[+] Enter your Subject : ")
    print("*"*60)
    choice=input("(A)Text\t(B)HTML\n[+] Enter your message type : ")
    print("*"*60)
    message=input("[+] Enter your message below :\n")
    print("*"*60)
    print("[+] Process your emails to verify so that we can avoid errors")
    print("[+] Use check_mail.py to verify and store email addresses")
    filename=input("[+] Enter your filename in verified email folder : ")
    if os.path.isfile(filename):
        print("[+] Valid file..Checking extension") 
    else:
        print("[+] Invalid File/Path")
        sys.exit()
    print("[+] Mass Mailer ....")
    print("[+] Sending emails from %s"%filename)
    print("*"*60)
    f = open("verified_emails/"+filename, "r")
    failed_emails=[]
    for x in f:
        receiver=x
        try:
            send_mail(sender,password,receiver,choice)
            print("[+] Sent email to %s"%receiver)
        except:
            failed_emails.append(x)
            print("[+] Failed to send email for %s"%receiver)
    print("*"*60)
    if len(failed_emails)==0:
        print("[+] Emails sent successfully ")
    else:
        print("[+] Emails for %s ID's Failed"%len(failed_emails))
    f.close()