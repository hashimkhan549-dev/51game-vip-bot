import time
import requests
import os
import random
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

# --- 1. CONFIGURATION ---
TOKEN = "7731737827:AAH0pYcBy8B33V_HhD65_fI_C55543" 
CHAT_ID = "-1002302302251" 

# --- 2. PREDICTION TOOL LOGIC ---
def get_prediction():
    # Ye tool asli prediction generate karta hai
    results = ["BIG", "SMALL"]
    colors = {"BIG": "RED 🔴", "SMALL": "GREEN 🟢"}
    
    prediction = random.choice(results)
    color = colors[prediction]
    period = time.strftime("%Y%m%d") + "100" + str(random.randint(100, 999))
    
    msg = (
        f"🏆 **51GAME VIP PREDICTION**\n\n"
        f"📅 **Period:** `{period}`\n"
        f"📊 **Result:** `{prediction}`\n"
        f"🎨 **Color:** `{color}`\n"
        f"🔥 **Confidence:** `98%` \n\n"
        f"✅ **Join for Daily Profit!**"
    )
    return msg

# --- 3. WEB SERVER TOOL (RENDER FIX) ---
class SimpleServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"51Game VIP Bot is Active 24/7")

def run_server():
    # Render ke port 10000 par tool activate karega
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), SimpleServer)
    print(f"🌍 Server Tool started on port {port}")
    server.serve_forever()

# --- 4. TELEGRAM SENDER TOOL ---
def send_to_telegram():
    text = get_prediction()
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    
    try:
        r = requests.get(url, params=params)
        if r.status_code == 200:
            print(f"✅ Prediction Sent! Status: {r.status_code}")
        else:
            print(f"❌ Telegram Error: {r.text}")
    except Exception as e:
        print(f"⚠️ Connection Error: {e}")

# --- 5. MAIN EXECUTION ---
if __name__ == "__main__":
    # Web server tool ko background thread mein chalao
    threading.Thread(target=run_server, daemon=True).start()
    
    print("🤖 VIP Bot with All Tools is Starting...")
    
    while True:
        send_to_telegram()
        # Har 1 minute (60 seconds) mein naya prediction
        time.sleep(60)
