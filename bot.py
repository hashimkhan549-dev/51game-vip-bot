import time
import random
import threading
import os
import json
import urllib.request
from http.server import HTTPServer, BaseHTTPRequestHandler

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

# --- 3. TELEGRAM SENDER (INBUILT TOOL) ---
def send_telegram_msg():
    print(f"🔄 Attempting to send message at {time.strftime('%H:%M:%S')}...")
    text = get_vip_prediction()
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    
    data = json.dumps({
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }).encode('utf-8')
    
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req) as response:
            if response.getcode() == 200:
                print(f"✅ MESSAGE SENT SUCCESSFULLY at {time.strftime('%H:%M:%S')}")
    except Exception as e:
        print(f"❌ TELEGRAM ERROR: {str(e)}")

# --- 4. RENDER STAY-ALIVE TOOL ---
class SimpleServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"51Game VIP Bot is Active 24/7")

def run_server():
    port = int(os.environ.get("PORT", 10000))
    print(f"🌍 Web Server Tool starting on port {port}...")
    server = HTTPServer(('0.0.0.0', port), SimpleServer)
    server.serve_forever()

# --- 5. MAIN EXECUTION ---
if __name__ == "__main__":
    # Server thread shuru karo
    threading.Thread(target=run_server, daemon=True).start()
    
    print("🤖 VIP Bot Engine Started...")
    while True:
        send_telegram_msg()
        # Har 1 minute mein prediction
        time.sleep(60)
