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

# --- 2. PREDICTION LOGIC ---
def get_vip_prediction():
    results = ["BIG 🔴", "SMALL 🟢"]
    result = random.choice(results)
    period = time.strftime("%Y%m%d") + "100" + str(random.randint(100, 999))
    return (
        "🚀 **51GAME VIP PREDICTION**\n"
        "━━━━━━━━━━━━━━━━━━\n"
        f"📅 **Period:** `{period}`\n"
        f"📊 **Result:** `{result}`\n"
        "🔥 **Confidence:** `100% SURE` \n"
        "━━━━━━━━━━━━━━━━━━"
    )

# --- 3. WEB SERVER (RENDER FIX) ---
class SimpleServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"51Game VIP Bot is Active 24/7")

def run_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), SimpleServer)
    server.serve_forever()

# --- 4. TELEGRAM SENDER (INTERNAL TOOL) ---
def send_msg():
    text = get_vip_prediction()
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = json.dumps({"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    
    try:
        with urllib.request.urlopen(req) as response:
            if response.getcode() == 200:
                print(f"✅ SUCCESS: Prediction sent at {time.strftime('%H:%M:%S')}")
    except urllib.error.HTTPError as e:
        error_msg = e.read().decode()
        # YE LINE LOGS MEIN BATAYEGI KI KYA GALTI HAI
        print(f"❌ TELEGRAM ERROR: {error_msg}") 
    except Exception as e:
        print(f"⚠️ SYSTEM ERROR: {e}")

if __name__ == "__main__":
    threading.Thread(target=run_server, daemon=True).start()
    print("🤖 Bot is starting... Check Logs for status.")
    while True:
        send_msg()
        time.sleep(60)
