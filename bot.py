import time
import requests

# --- CONFIGURATION ---
TOKEN = "7731737827:AAH0pYcBy8B33V_HhD65_fI_C55543" 
CHAT_ID = "-1002302302251" 

def send_prediction():
    message = "🚀 **51GAME VIP PREDICTION**\n✅ BOT IS RUNNING 24/7!"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    try:
        r = requests.get(url, params=params)
        print(f"✅ Prediction Sent! Status: {r.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("🤖 Bot is starting without Web Server...")
    while True:
        send_prediction()
        time.sleep(60) # Har 60 seconds mein message
