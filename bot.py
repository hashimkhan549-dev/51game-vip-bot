import time
import requests
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

# --- TOOL 1: CONFIGURATION ---
TOKEN = "7731737827:AAH0pYcBy8B33V_HhD65_fI_C55543" 
CHAT_ID = "-1002302302251" 

# --- TOOL 2: WEB SERVER (RENDER STAY-ALIVE TOOL) ---
# Ye tool Render ko signal deta hai ki bot active hai
class SimpleServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"51Game Bot is Running 24/7")

def run_server():
    # Render default port 10000 detect karne wala tool
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), SimpleServer)
    print(f"🌍 Tool: Web Server active on port {port}")
    server.serve_forever()

# --- TOOL 3: PREDICTION ENGINE ---
def send_prediction():
    message = "🚀 **51GAME VIP PREDICTION**\n"
    message += "========================\n"
    message += "🎰 Game: WinGo 1-Min\n"
    message += "📊 Result: BIG / SMALL\n"
    message += "🎨 Color: GREEN / RED\n"
    message += "========================\n"
    message += "✅ 100% SURE SHOT"
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    try:
        r = requests.get(url, params=params)
        print(f"✅ Prediction Tool: Status {r.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")

# --- TOOL 4: MAIN RUNNER (MULTI-THREADING) ---
if __name__ == "__main__":
    # Server ko background mein chalane ka tool
    threading.Thread(target=run_server, daemon=True).start()
    
    print("🤖 All Tools starting... Bot is LIVE!")
    while True:
        send_prediction()
        time.sleep(60) # Har 1 minute mein message jayega
