from verify_email import verify_email
import os
import sys
def check(filename):
    filepath="email_list/"+filename
    verifiedname=input("[+] Enter your filename to be saved in verified_emails ( No Extension ) : ")
    f=open(filepath,'r')
    g=open("verified_emails/"+verifiedname+".txt",'w')
    print("[+] This may take some time...")
    for x in f:
        print("[+] Processing %s"%x.strip('\n'))
        if verify_email(x.strip('\n')) is True:
            g.write(x)
    f.close()
    g.close()
    print("[+] Verified Emails Successfully")
if __name__ == "__main__":
    filename=input("[+] Enter the file name in the email_list directory : ")
    if os.path.isfile(filename):
        print("[+] Valid file..Checking extension") 
    else:
        print("[+] Invalid File/Path")
        sys.exit()
    check(filename)