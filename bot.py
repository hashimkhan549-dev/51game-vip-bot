import time
import requests
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

# --- CONFIGURATION ---
TOKEN = "7731737827:AAH0pYcBy8B33V_HhD65_fI_C55543" 
CHAT_ID = "-1002302302251" 

# Render port error fix karne ke liye (Zaroori hai)
class SimpleServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is Active")

def run_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), SimpleServer)
    server.serve_forever()

def send_prediction():
    message = "🚀 **51GAME VIP PREDICTION**\n✅ BOT IS LIVE ON RENDER!"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    try:
        r = requests.get(url, params=params)
        print(f"✅ Status: {r.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    # Server start karo taaki Render timeout na de
    threading.Thread(target=run_server, daemon=True).start()
    
    print("🤖 Bot is starting...")
    while True:
        send_prediction()
        time.sleep(60) # Har 1 minute mein prediction
