import requests
import smtplib
import json

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "AL2FIV280Y7HX0H5"
API_KEY_NEWSAPI = "66f779cd689a4903870ae11cab84ed06"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={API_KEY}")
response.raise_for_status()
daily_data  = response.json()['Time Series (Daily)']
dates = list(response.json()['Time Series (Daily)'])
yesterday_close = float(daily_data[dates[0]]['4. close'])
day_before_yesterday_close = float(daily_data[dates[1]]['4. close'])
#print(daily_data)
#print(yesterday_close)
#print(day_before_yesterday_close)
change_percent = ((yesterday_close-day_before_yesterday_close)/(day_before_yesterday_close))*100
if abs(change_percent) >= 5:
    print("Get news")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
response = requests.get(f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&from={dates[0]}&sortBy=publishedAt&apiKey={API_KEY_NEWSAPI}")
print(response.json()['articles'][:1])
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this:
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
with open("../../emails.json", 'r') as f:
    data = json.load(f)
EMAIL = 'abhishekbishnoi693@gmail.com'
PASSWORD = data[EMAIL]['password']
if change >
subject = f"Subject: {STOCK} {if change>0 }"

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

