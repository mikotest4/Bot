# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "27704224"))
API_HASH = getenv("API_HASH", "c2e33826d757fe113bc154fcfabc987d")
BOT_TOKEN = getenv("BOT_TOKEN", "7540338860:AAFrzBmmdsrK26uTPqomiOliPT5Jd7_TLL8")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7970350353").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://koxiher824:uhWjdKAzmfAHcagy@cluster0.lg66r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002669902570")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002669902570"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "100"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "5000"))
