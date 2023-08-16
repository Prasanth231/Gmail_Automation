
# Gmail Automation
It is mainly useful for HR when they receive a set of Resumes in the mail it will read the file then scrape the Email ID from each of the files and store it in the MySQL database. Then it will send registered messages to the scraped mailed.     
By using the **Imbox** package it can access the received mail and can download the file.     
Then use **PyPDF2** to scrape the EmailId from the received set of PDFs and store it in the MySQL database. At last by using the **Smtplib** it sends the Registered Messages to the particular Scarped mailId's.
 

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

![Gmailautomation](https://github.com/Prasanth231/Gmail_Automation/assets/128634760/693b89c4-65d3-486d-b36f-eafbc0dfa961)


