
# Gmail Automation
It mainly usefull for the HR when they recieve an set of Resumes in mail it will read the file then scrape the EmailID from each of the file and store it in the mysql database. Then it will send an registerd messages to the scraped mailid.     
By Using **Imbox** package it can access the recieved mails and can download the file.     
Then by using **PyPDF2** to scrape the EmailId from the received set of PDF and store it the mySql database. Atlast by using the **Smtplib** it send the Registered Messages to the particular Scarped mailId's.
 

## Installation

Install Gmail_Automation with npm

```bash
  npm install Gmail_Automation
  cd Gmail_Automation
```
    
## Deployment

To deploy this Gmail Automation Project to run firt install all the necessary packages

```bash
  pip3 install os
```
```bash
  pip3 install imbox
```
```bash
  pip3 install traceback
```
```bash
  pip3 install pypdf2
```
```bash
  pip3 install re
```
```bash
  pip3 install mysql.connector
```
```bash
  pip3 install smtplib
```
Then Run the project by using
```bash
  python gmail_automation.py 
```

## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

