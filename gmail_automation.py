#################################################################################################################################
import os
from imbox import Imbox # pip install imbox
import traceback
import PyPDF2
import re
import mysql.connector
import smtplib
#################################################################################################################################
#Host mail id to Check received mails
host = "imap.gmail.com"
username = "highflyer.2312@gmail.com"
password = 'xdsdfsdfsfsitsb'
download_folder = 'PATH//TO//THE//FILE'
#################################################################################################################################
#Login using Imbox and also connect to the mysql database to store the scraped mailID
mail = Imbox(host, username=username, password=password, ssl=True, ssl_context=None, starttls=False)
messages = mail.messages(sent_from='abc@gmail.com') 
try:
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gmail")
except error as e:
    print("error")   
mycursor = mydb.cursor()
#################################################################################################################################
if not os.path.isdir(download_folder):
    os.makedirs(download_folder, exist_ok=True)
 
for (uid, message) in messages:
    mail.mark_seen(uid) # optional, mark message as read

    for idx, attachment in enumerate(message.attachments):
        try:
            att_fn = attachment.get('filename')
            download_path = f"{download_folder}\{att_fn}"
            print(download_path)
            file_path = os.path.join(download_folder, att_fn)
            
            if att_fn.endswith('.pdf'):
                print("123")
                pdfFileObj = open(att_fn,'rb')
                pdfReader = PyPDF2.PdfReader(pdfFileObj)
                print(pdfReader)
                pages = len(pdfReader.pages)
                print(pages)
                for i in range(pages):
                    print("######################################################")
                    pageObj = pdfReader.pages[i]
                    #print("Page No: ",i)
                    text = pageObj.extract_text()
                    #print(text)
                    gmail_regex = r'\b[A-Za-z0-9._%+-]+@gmail\.com\b'
                    gmailid= re.findall(gmail_regex,text)
                    print(gmailid)
                    gmail =str(gmailid)[2:-2]
                    print(gmail)
                    query = "INSERT INTO mail (mailid) VALUES (%s)"
                    data = (gmail,)
                    mycursor.execute(query, data)
                    print("Inserted sussessfully")
                    #mycursor.execute("INSERT INTO mail(mailid) VALUES (%s)" )
                pdfFileObj.close()
                if os.path.isfile(file_path):
                    # Delete the file
                    os.remove(file_path)
                    print(f"The file {file_path} has been deleted.")
                else:
                    print(f"The file {file_path} does not exist.")
            with open(download_path, "wb") as fp:
                fp.write(attachment.get('content').read())
        except:
            print(" ")
#################################################################################################################################
#Send the Registered subject to the scrape mail id
#emails = mycursor.fetchall()
smtp_server = "smtp.gmail.com"
smtp_port = 587
subject = "Test Mail"
body = "This is a test email."
message = f"Subject: {subject}\n\n{body}"
smtp_server = smtplib.SMTP(smtp_server, smtp_port)
smtp_server.starttls()
smtp_server.login(username, password)
smtp_server.sendmail(username, gmail, message)
print("mail sented ")
#mycursor.execute("TRUNCATE TABLE mail")
#################################################################################################################################
#close all the connections
mail.logout()
mydb.commit()
mydb.close()
smtp_server.quit()
