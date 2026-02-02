import os
import time
import random
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.request
import json

# --- 1. CONFIGURATION ---
# Tera Token aur Chat ID
TOKEN = "7731737827:AAH0pYcBy8B33V_HhD65_fI_C55543"
CHAT_ID = "-1002302302251" 

# --- 2. HTML SERVER TOOL ---
# Ye tool Screenshot (290) wala page generate karta hai
class SimpleServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # Wahi exact message jo pehle dikhta tha
        html_content = """
        <html>
        <head><title>51Game VIP Bot</title></head>
        <body style="font-family: sans-serif; text-align: center; padding-top: 50px;">
            <h1>51Game VIP Bot is Active 24/7</h1>
            <p>Server is running smoothly on Render.</p>
        </body>
        </html>
        """
        self.wfile.write(html_content.encode())

def run_server():
    # Render ke liye port 10000 zaroori hai
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), SimpleServer)
    print(f"🌍 HTML Tool Live: http://0.0.0.0:{port}")
    server.serve_forever()

# --- 3. TELEGRAM MESSAGE TOOL ---
def send_telegram():
    # VIP Prediction Logic
    results = ["BIG 🔴", "SMALL 🟢"]
    out = random.choice(results)
    period = time.strftime("%Y%m%d") + "100" + str(random.randint(100, 999))
    
    msg_text = f"🚀 **51GAME VIP**\n\n📊 Period: `{period}`\n✅ Result: {out}"
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = json.dumps({"chat_id": CHAT_ID, "text": msg_text, "parse_mode": "Markdown"}).encode('utf-8')
    
    req = urllib.request.Request(url, data=payload, headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req) as response:
            if response.getcode() == 200:
                print(f"✅ Status: Message Sent to Telegram")
    except Exception as e:
        print(f"❌ Telegram Error: {e}")

# --- 4. MAIN START ---
if __name__ == "__main__":
    # HTML Server ko background mein chalao
    threading.Thread(target=run_server, daemon=True).start()
    
    print("🤖 Bot Engine started...")
    while True:
        send_telegram()
        # Har 1 minute mein prediction bhejna
        time.sleep(60)
