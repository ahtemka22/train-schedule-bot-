import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
API = os.getenv("ORS_API_KEY")

SCHEDULE_DZR_TO_MINSK = [
    "04:53", "06:01", "06:44", "07:19", "08:11", "09:22",
    "10:20", "13:27", "15:38", "17:12", "17:48", "19:36",
    "21:06", "22:59"
]

SCHEDULE_MINSK_TO_DZR = [
    "00:48", "04:19", "05:33", "07:14", "08:47", "09:34",
    "13:55", "16:05", "16:59", "17:42", "18:50", "19:52",
    "20:38", "22:22"
]

STATION_K_IN_MINSK = (53.885023800, 27.538787100)
STATION_K_IN_DZR = (53.682583, 27.158917)
