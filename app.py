import os
from dotenv import load_dotenv, find_dotenv
import yfinance as yf
import smtplib
import email.message

load_dotenv(find_dotenv())
def get_current_price_ticker(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]

def send_email(btc_brl, btc_doll, doll):
    email_body = f"""\
    <h1>Bitcoin is below R$100.000,00.</h1>
    <br>
    <h3>Current Quote: R${btc_brl:,.2f}</h3>
    <h3>Bitcoin in dollar: R${btc_doll:,.2f}</h3>
    <h3> US dollar value: R${doll:,.2f}</h3>
    """

    msg = email.message.Message()
    msg['Subject'] = "Bitcoin is now below R$100.000,00"
    msg['From'] = 'bragab2b.digital@gmail.com'
    msg['To'] = 'bragab2b.digital@gmail.com'
    password = os.environ.get("PASSWORD_EMAIL")

    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_body)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email sent')

price_btc_doll = (get_current_price_ticker('BTC-USD'))
price_doll = (get_current_price_ticker('BRL=X'))
price_btc_brl = (price_doll*price_btc_doll)


if price_btc_brl < 100000:
    send_email(price_btc_brl, price_btc_doll, price_doll)