import requests
import smtplib
from email.message import EmailMessage
from config import BOT_TOKEN, CHAT_ID, EMAIL, APP_PASSWORD

def send_telegram(company):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    r = requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": f"🎉 SHORTLIST ALERT\nCompany: {company}"
    })
    print("Telegram:", r.status_code)

def send_email(company):
    msg = EmailMessage()
    msg["Subject"] = f"URGENT: Shortlisted – {company}"
    msg["From"] = EMAIL
    msg["To"] = EMAIL
    msg.set_content(f"You are shortlisted for {company}")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as s:
        s.login(EMAIL, APP_PASSWORD)
        s.send_message(msg)

def trigger_alerts(company):
    send_telegram(company)
    send_email(company)
