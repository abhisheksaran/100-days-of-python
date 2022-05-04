import requests
import smtplib
import json
from datetime import datetime

MY_LAT = 28.704060  # Your latitude
MY_LONG = 77.102493  # Your longitude
MY_EMAIL = "abhishekbishnoi693@gmail.com"

# Get Email Credentials
with open("../../emails.json", 'r') as f:
    data = json.load(f)
EMAIL = 'abhishekbishnoi693@gmail.com'
PASSWORD = data[EMAIL]['password']

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.
def is_iss_overhead(iss_latitude, iss_longitude):
    if abs(iss_latitude - MY_LAT) <= 5 and abs(iss_longitude - MY_LONG) <= 5:
        return True
    else:
        return False


def send_mail_to(mail_id):
    print(f'Sending mail on {mail_id} to look up for ISS overhead!')
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=mail_id,
                            msg=f'Subject: Happy Abhishek\n\n Look up for ISS. It\'s over your head tonight')


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 5.30
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 5.30

time_now = datetime.now()
hour_now = time_now.hour

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
if is_iss_overhead(iss_latitude, iss_longitude) and sunset <= hour_now <= sunrise:
    send_mail_to(MY_EMAIL)

# BONUS: run the code every 60 seconds.

