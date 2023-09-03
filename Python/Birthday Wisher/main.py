import pandas as pd
import datetime
import smtplib
import os
os.chdir(r"C:\Users\Admin\OneDrive\Pictures\Desktop\Python\Birthday Wisher")

GMAIL_ID = "ENTER YOU EMAIL"
GMAIL_PSWD = "ENTER YOU PASSWORD"

def sendemail(to, sub, msg):
    print(f"Email to {to} sent with subject: {sub} and message {msg}")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(GMAIL_ID, GMAIL_PSWD)
    s.sendmail(GMAIL_ID, to, f"Subject: {sub}\n\n{msg}")

    s.quit()


if __name__ == "__main__":
    df = pd.read_excel("Book.xlsx")
    today = datetime.datetime.now().strftime("%d-%m")
    yearNow = datetime.datetime.now().strftime("%Y")
    writeInd = []

    for index, item in df.iterrows():
        bday = item['Birthday'].strftime("%d-%m")
        if(today == bday) and yearNow not in str(item['Year']):
            writeInd.append(index)

    for i in writeInd:
        yr = df.loc[i, 'Year']
        df.loc[i, 'Year'] = str(yr) +","+ str(yearNow)

    df.to_excel('Book.xlsx', index=False)