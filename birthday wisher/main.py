import smtplib
import datetime
import random
import pandas

date = datetime.datetime.now()
DAY = date.day
MONTH = date.month
PATHS = [f"./day_32_birthday_wisher/letter_templates/letter_{x}.txt" for x in range(1,4)]

data = pandas.read_csv("./day_32_birthday_wisher/birthdays.csv")

for index, row in data.iterrows():
    if row.day == DAY and row.month == MONTH:
       choice = random.choice(PATHS)
       with open(choice, mode="r") as file:
           LETTER = file.read().replace("[NAME]", f"{row.names}")
       with smtplib.SMTP("smtp.email.com") as sender:
           sender.starttls()
           sender.login(user="USER", password="PASSWORD")
           sender.sendmail(
           from_addr="EXAMPLE", to_addrs="EXAMPLE2",
           msg=f"Subject:SUBJECT\n\TEXT"
           )