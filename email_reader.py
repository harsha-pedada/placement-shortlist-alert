from imapclient import IMAPClient
import pyzmail
import os

from detector import is_me_present
from notifier import trigger_alerts
from excel_parser import scan_excel
from pdf_parser import scan_pdf
from config import EMAIL, APP_PASSWORD

ATTACH_DIR = "attachments"
os.makedirs(ATTACH_DIR, exist_ok=True)

def check_inbox():
    with IMAPClient("imap.gmail.com") as server:
        server.login(EMAIL, APP_PASSWORD)
        server.select_folder("INBOX")

        messages = server.search(["UNSEEN"])

        for uid in messages:
            raw = server.fetch([uid], ["BODY[]"])
            msg = pyzmail.PyzMessage.factory(raw[uid][b"BODY[]"])

            subject = msg.get_subject()
            body = ""

            if msg.text_part:
                body = msg.text_part.get_payload().decode(
                    msg.text_part.charset or "utf-8", errors="replace"
                )
            elif msg.html_part:
                body = msg.html_part.get_payload().decode(
                    msg.html_part.charset or "utf-8", errors="replace"
                )

            print("Checking:", subject)

            alert_sent = False

            # 1️⃣ Email body check
            if is_me_present(body):
                trigger_alerts(subject)
                alert_sent = True

            # 2️⃣ Attachment checks (Excel + PDF)
            for part in msg.mailparts:
                filename = part.filename
                if not filename:
                    continue

                file_path = os.path.join(ATTACH_DIR, filename)

                with open(file_path, "wb") as f:
                    f.write(part.get_payload())

                # Excel
                if filename.endswith((".xlsx", ".xls", ".csv")):
                    print("Scanning Excel:", filename)
                    if scan_excel(file_path) and not alert_sent:
                        trigger_alerts(subject)
                        alert_sent = True

                # PDF
                elif filename.endswith(".pdf"):
                    print("Scanning PDF:", filename)
                    if scan_pdf(file_path) and not alert_sent:
                        trigger_alerts(subject)
                        alert_sent = True

            server.add_flags(uid, ["\\Seen"])
