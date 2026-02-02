import time
import requests
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

# --- CONFIGURATION ---
# Tumhara Bot Token
TOKEN = "7731737827:AAH0pYcBy8B33V_HhD65_fI_C55543" 
# Tumhara Chat ID
CHAT_ID = "-1002302302251" 

# --- WEB SERVER TOOL (RENDER FIX) ---
# Ye tool Render ko signal deta hai ki service "Live" hai
class SimpleServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"51Game Bot is Running 24/7")

def run_server():
    # Render default port 10000 use karta hai
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), SimpleServer)
    print(f"🌍 Web Server started on port {port}")
    server.serve_forever()

# --- PREDICTION LOGIC ---
def send_prediction():
    # Prediction message format
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
        response = requests.get(url, params=params)
        if response.status_code == 200:
            print(f"✅ Status: 200 | Prediction sent at {time.ctime()}")
        else:
            print(f"❌ Failed to send: {response.text}")
    except Exception as e:
        print(f"⚠️ Error: {e}")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # 1. Web Server ko background thread mein chalao taaki bot aur server dono chalein
    threading.Thread(target=run_server, daemon=True).start()
    
    print("🤖 Bot is starting on Render...")
    
    # 2. Prediction loop shuru karo
    while True:
        send_prediction()
        # Har 60 seconds (1 minute) mein ek prediction jayegi
        time.sleep(60)
