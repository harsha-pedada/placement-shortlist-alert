import time
from email_reader import check_inbox
from config import CHECK_INTERVAL

print("📡 Placement Alert System Started...")

while True:
    try:
        check_inbox()
        time.sleep(CHECK_INTERVAL)
    except Exception as e:
        print("Error:", e)
        time.sleep(30)
