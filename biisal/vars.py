# (c) adarsh-goel (c) @biisal
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()
bot_name = "@kissu_store_bot"
bisal_channel = "https://t.me/kissubots"
bisal_grp = "https://t.me/ur_movie_group"

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '9301087'))
    API_HASH = str(getenv('API_HASH', 'cbabdb3f23de6326352ef3ac26338d9c'))
    BOT_TOKEN = str(getenv('BOT_TOKEN' , ''))
    name = str(getenv('name', 'kissu_store_bot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002391526686'))
    NEW_USER_LOG = int(getenv('NEW_USER_LOG', '-1002391526686'))
    PORT = int(getenv('PORT', '8080'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = [int(x) for x in os.environ.get("OWNER_ID", "6670354006").split()]
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    PICS = (environ.get('PICS', 'https://telegra.ph/file/ded6640caffcd72b77f64.jpg https://telegra.ph/file/54b0ae662175ac6af6075.jpg https://telegra.ph/file/857a050c16577c3f140e0.jpg https://telegra.ph/file/a53e31d5f1617573cfaf6.jpg https://telegra.ph/file/252c23180fd4ec651d05c.jpg https://telegra.ph/file/43de56c43d2bfde9b436b.jpg https://telegra.ph/file/962f894d97316f97dfb97.jpg')).split() #SAMPLE PIC
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'xaekks'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME')) #dont need to fill anything here
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', 'BIND_ADRESS:PORT')) if not ON_HEROKU or getenv('FQDN', 'kissustream.koyeb.app') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',True))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://supriyaxrajput9:supriyaxrajput9@cluster0.dxf3w.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'kissubots')) 
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "")).split()))   
    BAN_CHNL = list(set(int(x) for x in str(getenv("BAN_CHNL", "")).split()))   
    BAN_ALERT = str(getenv('BAN_ALERT' , '<b>ʏᴏᴜʀ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ.Pʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ @kissuhelp ᴛᴏ ʀᴇsᴏʟᴠᴇ ᴛʜᴇ ɪssᴜᴇ!!</b>'))
