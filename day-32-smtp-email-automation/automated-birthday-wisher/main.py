import pandas
import datetime as dt
import smtplib
import json


# Send birthday mail to name on given mail_id
def send_mail_to(name, mail_id):
    print(f'Sending mail to {name} on {mail_id} to wish him/her Happy Birthday!')
    with open("letter.txt", 'r') as letter:
        bday_msg = letter.read()
        bday_msg = bday_msg.replace('[name]', name)
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=mail_id,
                            msg=f'Subject: Happy Birthday\n\n{bday_msg}')

# Get Email Credentials
with open("../emails.json", 'r') as f:
    data = json.load(f)
EMAIL = 'abhishekbishnoi693@gmail.com'
PASSWORD = data[EMAIL]['password']

# Run through all the birthdays of your friends/family
bd_df = pandas.read_csv("birthdays.csv")
bd_list = bd_df.to_dict(orient='records')

# If someone has birthday today, send a mail to him/her
for bday in bd_list:
    now = dt.datetime.now()
    if now.month == bday['month'] and now.day == bday['day']:
        send_mail_to(bday['name'], bday['email'])

# TODO Make a cron job to be run on your computer everyday at 10 AM
# Many ways to do this

# 1. Create a docker image and run it as a cron jon in kubernetes
# 2. Schedule it daily in your local system using crontab
# For example-

## Open crontab in vim
# export VISUAL=vim; crontab -e
## Run the script at 12 PM every day using this below cron schedule
# 0 12 * * * cd ~/abhishek/100-days-of-python/day-32-smtp-email-automation/automated-birthday-wisher && python3 main.py
## Save and exit form vim
## Check and verify the crontab
# crontab -l
