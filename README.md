# Simple-IDS-QRD-INT

A lightweight, real-time Intrusion Detection System built using Python, Scapy, and Flask, developed as part of my internship at Quantumard. This project captures live packets, detects suspicious activity (e.g., port scans), logs events, and displays them in a dynamic web dashboard.

☼ Features
• Live Packet Capture using Scapy
• Rule-Based Detection for common network threats like SYN Floods / Port Scans
• Real-time Dashboard with Flask and SocketIO
• Log Management
Automatic logging to detector.log
• Dashboard options to download or clear logs

☼ Auto-refresh every 5 seconds to reflect the latest threats

☼ Tech Stack
 • Layer	Technology
 • Programming	Python 3.10+
 • Packet Capture	Scapy
 • Backend	Flask, SocketIO
 • Frontend	HTML, CSS

☼ Dashboard Preview

Real-time alerts, auto-refresh, and log download options.

☼ Getting Started
1. Clone the Repository
bash
git clone https://github.com/your-username/simple-ids-quantumard.git
cd simple-ids-quantumard
2. Install Dependencies
bash
pip install -r requirements.txt

Ensure nmap is installed and available in system PATH (for testing with scans).

4. Run the IDS System
bash
python app.py
The Flask app will run on http://127.0.0.1:5000.

☼ Testing the IDS
To simulate suspicious traffic:
bash
nmap -sS 127.0.0.1
Replace 127.0.0.1 with your local or target IP to generate SYN packets.

○ Project Structure
simple-ids/
├── app.py              # Flask + SocketIO app
├── ids.py              # Intrusion detection logic with Scapy
├── templates/
│   └── dashboard.html  # Live dashboard UI
├── detector.log        # Auto-generated log file
├── requirements.txt    # Python dependencies
└── README.md           # This file

○ Learning Outcomes
 • Understood TCP/IP fundamentals and attack signatures
 • Implemented live packet capture and event-driven detection logic
 • Designed a full-stack Flask dashboard with log handling
 • Explored real-world security practices under internship mentorship at Quantumard

○ Acknowledgments
Grateful to the team at Quantumard for their guidance and support during the internship.

○ Connect With Me
🔗 www.linkedin.com/in/ashwin-karthikeyan-49a4b632b
📧 ashwinkarthikeyan496@gmail.com

• Disclaimer
This IDS is built for educational purposes only. Do not use it for unauthorized network scanning or surveillance.
