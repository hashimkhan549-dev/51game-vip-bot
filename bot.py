import time
import random
import threading
import os
import json
import urllib.request
from http.server import HTTPServer, BaseHTTPRequestHandler

# --- 1. CONFIGURATION ---
TOKEN = "7731737827:AAH0pYcBy8B33V_HhD65_fI_C55543"
# Isko abhi aise hi rehne do, code khud check karega
CHAT_ID = "-1002302302251" 

# --- 2. RENDER STAY-ALIVE (SERVER) ---
class SimpleServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"MASTER BOT IS LIVE 24/7")

def run_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), SimpleServer)
    server.serve_forever()

# --- 3. THE MASTER SENDING TOOL ---
def master_send(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = json.dumps({"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req) as response:
            return response.getcode() == 200
    except Exception as e:
        print(f"⚠️ Log: Telegram Connection Issue - {e}")
        return False

# --- 4. PREDICTION LOGIC ---
def start_bot():
    print("🚀 MASTER BOT ENGINE STARTED...")
    while True:
        res = ["BIG 🔴", "SMALL 🟢"]
        out = random.choice(res)
        msg = f"🚀 **51GAME VIP**\n\n📊 Result: {out}\n✅ 100% Sure"
        
        if master_send(msg):
            print(f"✅ SUCCESS: Message Sent at {time.strftime('%H:%M:%S')}")
        else:
            print("❌ FAILED: Checking if Bot is Admin or Chat ID is correct...")
        
        time.sleep(60)

if __name__ == "__main__":
    # Start Render Server
    threading.Thread(target=run_server, daemon=True).start()
    # Start Prediction Tool
    start_bot()
