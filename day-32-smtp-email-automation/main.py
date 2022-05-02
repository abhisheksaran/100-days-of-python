import smtplib
import json

with open("emails.json",'r') as f:
    data=json.load(f)

my_email = 'abhishekbishnoi693@gmail.com'
password = data[my_email]['password']
print(my_email)
print(password)
# Location of provided email server has to be given
# While creating SMTP object
# For example gmail, the host is "smtp.gmail.com'
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="abhishekbishnoi693@gmail.com", msg=
    "Subject:Hello\n\n"
    "Hello Abhishek!, How are you?? Hope this day goes productive for you!!"
                        )
    connection.close()
