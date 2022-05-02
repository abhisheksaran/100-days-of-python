import smtplib
import json
import random
import datetime as dt

# Get email password
with open("emails.json", 'r') as f:
    data = json.load(f)
my_email = 'abhishekbishnoi693@gmail.com'
password = data[my_email]['password']

# Read quotes
with open("quotes.txt", "r") as f:
    quotes = f.readlines()
random_quote = random.choice(quotes)

# Send the mail on the current weekday
now = dt.datetime.now()

if now.weekday() == 0:
    # Location of provided email server has to be given
    # While creating SMTP object
    # For example gmail, the host is "smtp.gmail.com'
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="abhishekbishnoi693@gmail.com",
            msg=f"Subject:Quote for the week\n\n{random_quote}")
        connection.close()
