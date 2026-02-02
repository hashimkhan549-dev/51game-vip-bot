import os
import time
import random
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.request
import json

# --- 1. CONFIGURATION ---
# Teri Chat ID aur Token ekdum sahi hai
TOKEN = "7731737827:AAH0pYcBy8B33V_HhD65_fI_C55543"
CHAT_ID = "-1002302302251" 

# --- 2. PREDICTION ENGINE TOOL ---
def get_vip_prediction():
    results = ["BIG 🔴", "SMALL 🟢", "BIG 🔴", "SMALL 🟢"]
    result = random.choice(results)
    period = time.strftime("%Y%m%d") + "100" + str(random.randint(100, 999))
    
    msg = (
        "🚀 **51GAME VIP PREDICTION** 🚀\n"
        "━━━━━━━━━━━━━━━━━━\n"
        f"📅 **Period:** `{period}`\n"
        f"📊 **Result:** `{result}`\n"
        "🔥 **Confidence:** `100% SURE` \n"
        "━━━━━━━━━━━━━━━━━━\n"
        "✅ **JOIN FOR DAILY PROFIT**"
    )
    return msg

# --- 3. WEB SERVER TOOL (RENDER STAY-ALIVE) ---
# Isse Screenshot (290) wali screen zinda rahegi
class SimpleServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"51Game VIP Bot is Active 24/7")

def run_server():
    # Render port 10000 detect kar raha hai
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), SimpleServer)
    server.serve_forever()

# --- 4. TELEGRAM SENDER (WITHOUT REQUESTS TOOL) ---
# Maine isse badal diya hai taaki 'requests' ki galti na aaye
def send_msg():
    text = get_vip_prediction()
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = json.dumps({"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}).encode('utf-8')
    
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req) as response:
            if response.getcode() == 200:
                print(f"✅ Prediction Sent Successfully!")
    except Exception as e:
        print(f"❌ Telegram Error: {e}")

# --- 5. MAIN RUNNER ---
if __name__ == "__main__":
    # Server Tool ko background mein chalao
    threading.Thread(target=run_server, daemon=True).start()
    
    print("🤖 VIP Bot is Starting...")
    while True:
        send_msg()
        # Har 60 seconds mein prediction
        time.sleep(60)
