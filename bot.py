import time
import requests

# --- CONFIGURATION ---
TOKEN = "7731737827:AAH0pYcBy8B33V_HhD65_fI_C55543" 
CHAT_ID = "-1002302302251" # Is ID ko ek baar confirm kar lena

def send_prediction():
    message = "🚀 **VIP SHOR SHOT PREDICTION**\n"
    message += "========================\n"
    message += "WinGo 1Min - 51game 🟢/🔴\n"
    message += f"Time: {time.ctime()}\n"
    message += "Result: BIG / SMALL\n"
    message += "========================"
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    
    try:
        requests.get(url, params=params)
        print(f"Prediction sent at {time.ctime()}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("✅ Bot is starting on Render...")
    while True:
        send_prediction()
        time.sleep(60) # Har 1 minute mein message bhejega
