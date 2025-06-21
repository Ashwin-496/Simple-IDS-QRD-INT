from scapy.all import sniff, IP, TCP
from datetime import datetime
import threading

LOG_FILE = "detector.log"
socketio = None  # Global variable to store SocketIO object
syn_counts = {}

def log_event(event):
    print(f"[ALERT] {event}")
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {event}\n")
    if socketio:
        socketio.emit('new_log', {'log': f"{datetime.now()} - {event}"})

def detect(packet):
    if TCP in packet and IP in packet:
        src_ip = packet[IP].src
        flags = packet[TCP].flags

        # Use bitwise operation instead of direct match
        if flags & 0x02:  # SYN flag
            syn_counts[src_ip] = syn_counts.get(src_ip, 0) + 1
            if syn_counts[src_ip] > 10:
                event = f"Possible Port Scan detected from {src_ip}"
                log_event(event)

def start_sniffing():
    sniff(prn=detect, store=0)

def start_ids(sio):
    global socketio
    socketio = sio
    thread = threading.Thread(target=start_sniffing)
    thread.daemon = True
    thread.start()
