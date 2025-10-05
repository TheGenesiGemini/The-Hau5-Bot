import os
from dotenv import load_dotenv

load_dotenv()

CHATS = [
    -1001515379979,  # Binance Crypto Box Code
    -1001813092752,  # Binance Red packet crypto box
    -1001610472708,  # 🐋 Chat Whale Box 🎁
]

CLIENT_NAME = os.getenv("CLIENT_NAME", "MajaderaBot")
API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
CSRFTOKEN = os.getenv("CSRFTOKEN", "")
FVIDEO_ID = os.getenv("FVIDEO_ID", "")
FVIDEO_TOKEN = os.getenv("FVIDEO_TOKEN", "")
USER_AGENT = os.getenv("USER_AGENT", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...")
X_TRACE_ID = os.getenv("X_TRACE_ID", "")
X_UI_REQUEST_TRACE = os.getenv("X_UI_REQUEST_TRACE", "")
LANG = os.getenv("LANG", "es-419")
REFERER = os.getenv("REFERER", "https://www.binance.com/es/my/wallet/account/payment/cryptobox")

HEADERS = {
    "User-Agent": USER_AGENT,
    "clienttype": "web",
    "csrftoken": CSRFTOKEN,
    "fvideo-id": FVIDEO_ID,
    "fvideo-token": FVIDEO_TOKEN,
    "x-trace-id": X_TRACE_ID,
    "x-ui-request-trace": X_UI_REQUEST_TRACE,
    "lang": LANG,
    "Referer": REFERER,
}

def __getelement__(element: str):
    return globals().get(element, None)
