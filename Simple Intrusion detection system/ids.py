from scapy.all import sniff, IP, TCP
from datetime import datetime
import threading

LOG_FILE = "detector.log"
socketio = None  # Will be set by app.py

def log_event(event):
    print(f"[DEBUG] Logging event: {event}")
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {event}\n")
    if socketio:
        socketio.emit('new_log', {'log': event})

def detect(packet):
    if TCP in packet and IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        flags = packet[TCP].flags

        if flags == 0x02:  # SYN flag
            event = f"Possible Port Scan detected from {src_ip}"
            log_event(event)

def start_sniffing():
    sniff(prn=detect, store=0)

def start_ids(sockio):
    global socketio
    socketio = sockio
    thread = threading.Thread(target=start_sniffing)
    thread.daemon = True
    thread.start()
