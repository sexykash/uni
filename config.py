import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 1000))

# Chat id of a group for logging bot's activities
LOG_ID = int(getenv("LOGGER_ID"))
LOGGER_ID = int(getenv("LOGGER_ID"))

# Get this value from @fatherBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/sexykash/uni",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/saykkunomusic")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/saykkunomusic")

# Set it in True if you want to leave your assistant after a certain amount of time. [Set time via AUTO_LEAVE_ASSISTANT_TIME]
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", False)

# Time after which you're assistant account will leave chats automatically.
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "9000")
)  # Remember to give value in Seconds

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET")

# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", 900))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", 900))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes

# Get your pyrogram v2 session from @KavyaStringGeneratorBot on Telegram
STRING1 = getenv("STRING_SESSION")
STRING2 = getenv("STRING_SESSION2")
STRING3 = getenv("STRING_SESSION3")
STRING4 = getenv("STRING_SESSION4")
STRING5 = getenv("STRING_SESSION5")
STRING6 = getenv("STRING_SESSION6")
STRING7 = getenv("STRING_SESSION7")


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/e7ef690f27d84b0170924.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/e7ef690f27d84b0170924.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/9d75bfb77e17b80b3da5b.png"
STATS_IMG_URL = "https://i.pinimg.com/originals/2f/b8/d3/2fb8d33c12f3816e5bfed7fe614d447a.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/9d75bfb77e17b80b3da5b.png"
TELEGRAM_VIDEO_URL = "https://graph.org/file/9d75bfb77e17b80b3da5b.png"
STREAM_IMG_URL = "https://te.legra.ph/file/693694b0d94afa372ca5a.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/f72ea4bd955c418c724e1.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/693694b0d94afa372ca5a.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/c3682dc6fd740b2dac969.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/c3682dc6fd740b2dac969.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/c3682dc6fd740b2dac969.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
