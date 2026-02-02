import os
import time
import random
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

# --- AUTOMATIC TOOL INSTALLER ---
try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests

# --- 1. CONFIGURATION TOOL ---
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
# Ye tool Screenshot (290) wali screen ko zinda rakhta hai
class SimpleServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"51Game VIP Bot is Active 24/7")

def run_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), SimpleServer)
    print(f"🌍 Server started on port {port}")
    server.serve_forever()

# --- 4. TELEGRAM SENDER TOOL ---
def send_msg():
    text = get_vip_prediction()
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    
    try:
        r = requests.get(url, params=payload)
        if r.status_code == 200:
            print(f"✅ Prediction Sent Successfully! Status: {r.status_code}")
        else:
            print(f"❌ Telegram Error: {r.text}")
    except Exception as e:
        print(f"⚠️ Tool Connection Error: {e}")

# --- 5. MAIN RUNNER TOOL ---
if __name__ == "__main__":
    # Server Tool ko background mein chalao
    threading.Thread(target=run_server, daemon=True).start()
    
    print("🤖 VIP Bot with Full Tools is Starting...")
    
    while True:
        send_msg()
        # Har 60 seconds mein naya prediction jayega
        time.sleep(60)
