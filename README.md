
# Placement Shortlist Alert System 🚀

A production-style background automation system that continuously monitors placement emails and **instantly alerts the student when they are shortlisted**, even if the shortlist is sent in different formats such as email tables, Excel sheets, or PDFs.

This project is built to solve a **real and recurring problem during campus placements**, where missing a shortlist email can cost an opportunity.

---

## 🔍 Problem Statement

During campus placements:
- Shortlist emails can arrive **at any time**
- Formats are inconsistent:
  - Plain text emails
  - HTML emails with tables
  - Excel attachments
  - PDF attachments
- Manual inbox checking is unreliable and stressful

There is no single standardized format, making automation difficult.

---

## ✅ Solution

This system runs as a **continuous background service** that:

1. Monitors the Gmail inbox using IMAP
2. Reads and parses new emails automatically
3. Scans:
   - Email body (text & HTML tables)
   - Excel / CSV attachments
   - Text-based PDF attachments
4. Detects the student’s **name or roll number**
5. Sends **instant alerts** via:
   - Telegram
   - Email (backup)

Alerts are triggered **automatically**, without manual interaction.

---

## ✨ Key Features

- 📬 Continuous Gmail inbox monitoring (IMAP)
- 🔎 Identity-based detection (Name / Roll Number)
- 🧾 Supports multiple shortlist formats:
  - Plain text emails
  - HTML emails (tables included)
  - Excel files (`.xlsx`, `.xls`)
  - CSV files
  - Text-based PDF files
- 📱 Instant Telegram notifications
- 📧 Email alerts as fallback
- ⏱️ Configurable polling interval
- ♻️ Duplicate alert prevention (emails marked as read)
- 🔐 Secure credential handling (secrets excluded from Git)

---

## 🧠 System Architecture

Background Python Service
|
├── IMAP Email Reader
│ ├── Email Body Parser
│ ├── Excel / CSV Parser
│ └── PDF Parser
|
├── Identity Detection Engine
|
└── Notification Service
├── Telegram Alerts
└── Email Alerts

yaml
Copy code

---

## 📁 Project Structure

placement-shortlist-alert/
│
├── main.py # Entry point (background runner)
├── email_reader.py # IMAP handling & attachment extraction
├── detector.py # Name / roll number detection logic
├── notifier.py # Telegram & Email notifications
├── excel_parser.py # Excel & CSV shortlist parsing
├── pdf_parser.py # PDF shortlist parsing
├── config.example.py # Configuration template (safe for Git)
├── requirements.txt # Python dependencies
├── README.md
└── .gitignore

yaml
Copy code

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/placement-shortlist-alert.git
cd placement-shortlist-alert
2️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
3️⃣ Configure the Application
Create a config.py file using the provided template:

bash
Copy code
cp config.example.py config.py
Edit config.py and add:

Your full name

Your roll number (optional but recommended)

Gmail email address

Gmail App Password

Telegram Bot Token

Telegram Chat ID

Polling interval (seconds)

⚠️ config.py is intentionally excluded from Git to prevent credential leaks.

4️⃣ Enable Gmail IMAP
Gmail → Settings → Forwarding & POP/IMAP

Enable IMAP

Generate a Gmail App Password

Use the App Password (not your Gmail password)

5️⃣ Run the Service
bash
Copy code
python main.py
Leave the process running to receive real-time alerts.

📊 Supported Shortlist Formats
Format	Supported
Plain text emails	✅
HTML emails (tables)	✅
Excel attachments (.xlsx, .xls)	✅
CSV files	✅
Text-based PDF files	✅
Scanned PDFs (images)	❌ (OCR not implemented)

🔐 Security Considerations
Sensitive credentials are never committed to GitHub

Configuration is isolated in config.py

Attachments are processed locally

System and temporary files are ignored via .gitignore

🚀 Future Enhancements
OCR support for scanned PDFs

Cloud deployment for 24/7 availability

Multi-user support

Alert history & logging

Web dashboard

Retry & fault tolerance improvements

👤 Author
Harsha Vardhan Pedada
Computer Science & Engineering Student

📜 License
This project is intended for educational and personal use.
