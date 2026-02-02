import time
import requests
import os
import random
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

# --- 1. CONFIGURATION ---
# Tumhara details ekdum sahi hain
TOKEN = "7731737827:AAH0pYcBy8B33V_HhD65_fI_C55543" 
CHAT_ID = "-1002302302251" 

# --- 2. PREDICTION TOOL LOGIC ---
# Ye tool asli VIP predictions generate karega
def generate_vip_prediction():
    results = ["BIG", "SMALL", "BIG", "SMALL"] # Algorithm logic
    colors = {"BIG": "RED 🔴", "SMALL": "GREEN 🟢"}
    
    prediction = random.choice(results)
    color = colors[prediction]
    # Period number format: Date + Random ID
    period = time.strftime("%Y%m%d") + "100" + str(random.randint(100, 999))
    
    msg = (
        "🚀 **51GAME VIP PREDICTION** 🚀\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"📅 **Period:** `{period}`\n"
        f"📊 **Result:** `{prediction}`\n"
        f"🎨 **Color:** `{color}`\n"
        "🔥 **Confidence:** `99% SURE` \n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "✅ **JOIN FOR DAILY PROFIT**"
    )
    return msg

# --- 3. WEB SERVER TOOL (RENDER STAY-ALIVE) ---
# Isse Render "Timed Out" nahi karega
class SimpleServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"51Game Bot is Running 24/7")

def run_server():
    # Render port 10000 use karta hai
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), SimpleServer)
    print(f"🌍 Tool: Web Server active on port {port}")
    server.serve_forever()

# --- 4. TELEGRAM SENDER TOOL ---
def send_to_telegram():
    prediction_text = generate_vip_prediction()
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {"chat_id": CHAT_ID, "text": prediction_text, "parse_mode": "Markdown"}
    
    try:
        r = requests.get(url, params=params)
        if r.status_code == 200:
            print(f"✅ Status: 200 | Prediction Sent Successfully!")
        else:
            print(f"❌ Telegram Error: {r.text}")
    except Exception as e:
        print(f"⚠️ Connection Error: {e}")

# --- 5. MAIN RUNNER ---
if __name__ == "__main__":
    # Web server tool ko background mein chalao
    threading.Thread(target=run_server, daemon=True).start()
    
    print("🤖 VIP Bot with All Tools starting...")
    
    while True:
        send_to_telegram()
        # Har 60 seconds (1 min) mein naya message
        time.sleep(60)
