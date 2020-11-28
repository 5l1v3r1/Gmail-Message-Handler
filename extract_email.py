import os
import sys
import pandas

def extract():
    print("< EXCEL/CSV EMAIL ID EXTRACTER >")
    print("*"*60)
    filepath=input("[+] Enter path for your Excel/CSV File : ")
    if os.path.isfile(filepath):
        print("[+] Valid file..Checking extension") 
    else:
        print("[+] Invalid File/Path")
        sys.exit()
    if filepath.lower().endswith('.csv'):
        print("[+] CSV type found")
        data=pandas.read_csv(filepath)
    if filepath.lower().endswith(('.xls','.xlsx','.xlsm','.xlsb')):
        print("[+] Excel type found")
        data=pandas.read_excel(filepath)
    else:
        print("[+] Valid file extension not found ")
        sys.exit()
    #print(list(data.columns))
    print("*"*60)
    print("[+] Columns in the dataframe :")
    count=1
    column_data=list(data.columns)
    for x in column_data:
        print("(%s)%s"%(count,x))
        count+=1
    choice=int(input("[+] Enter the column number to extract Email ID : "))
    x = data[column_data[choice-1]].tolist() 
    email_ids=set(x)
    email_ids=list(email_ids)
    print("*"*60)
    print("[+] Email ID's Extracted")
    filename=input("[+] Enter your file name to store Email ID's in email_list directory (No Extension):\n")
    f=open("email_list/"+filename+".txt",'w')
    for x in email_ids:
        f.write(str(x)+'\n')
    f.close()
    print("[+] File created successfully (%s)"%("email_list/"+filename+".txt"))

if __name__ == "__main__":
    try:
        extract()
    except KeyboardInterrupt:
        print("\n[+] Process Interrupted...")
        sys.exit()