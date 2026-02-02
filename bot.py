import os
import time
import random
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.request
import json

# --- 1. CONFIGURATION ---
TOKEN = "7731737827:AAH0pYcBy8B33V_HhD65_fI_C55543"
CHAT_ID = "-1002302302251" 

# --- 2. HTML SERVER TOOL (RENDER FIX) ---
# Ye wahi tool hai jo Screenshot (290) mein "Active" dikhata hai
class SimpleServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # Wahi message jo Screenshot (290) mein tha
        self.wfile.write(b"<html><head><title>Bot Status</title></head>")
        self.wfile.write(b"<body><center><h1>51Game VIP Bot is Active 24/7</h1></center></body></html>")

def run_server():
    # Render ke liye port binding
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), SimpleServer)
    print(f"🌍 HTML Server Tool Live on Port {port}")
    server.serve_forever()

# --- 3. TELEGRAM SENDER TOOL ---
def send_msg():
    # Prediction Logic
    results = ["BIG 🔴", "SMALL 🟢"]
    res = random.choice(results)
    period = time.strftime("%Y%m%d") + "100" + str(random.randint(100, 999))
    
    text = f"🚀 **51GAME VIP**\n\n📊 Period: `{period}`\n✅ Result: {res}"
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = json.dumps({"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    
    try:
        with urllib.request.urlopen(req) as response:
            if response.getcode() == 200:
                print(f"✅ Telegram: Message Sent at {time.strftime('%H:%M:%S')}")
    except Exception as e:
        print(f"❌ Telegram Error: {e}")

# --- 4. MAIN RUNNER ---
if __name__ == "__main__":
    # Pehle HTML Server tool ko background mein chalao
    threading.Thread(target=run_server, daemon=True).start()
    
    print("🤖 VIP Bot Engine Started...")
    while True:
        send_msg()
        # Har 1 minute mein message
        time.sleep(60)
