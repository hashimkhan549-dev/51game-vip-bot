import time
import requests
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

# --- CONFIGURATION ---
TOKEN = "7731737827:AAH0pYcBy8B33V_HhD65_fI_C55543" 
CHAT_ID = "-1002302302251" 

# Render port error fix karne ke liye
class SimpleServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is Running 24/7")

def run_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), SimpleServer)
    server.serve_forever()

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
        print(f"Status: {r.status_code}, Prediction Sent!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Server background mein chalega
    threading.Thread(target=run_server, daemon=True).start()
    
    print("🤖 Bot is starting on Render...")
    while True:
        send_prediction()
        time.sleep(60)
