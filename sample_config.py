import os

class Var(object):
    APP_ID = 123456 # REQUIRED 
    API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e" # REQUIRED
    STRING_SESSION = "" # REQUIRED
    DB_URI = "" # REQUIRED
    TEMP_DOWNLOAD_DIRECTORY = "./userbot/DOWNLOADS/"
    LOGGER = True
    GITHUB_ACCESS_TOKEN = ""
    GIT_REPO_NAME = ""
    ABUSE = "ON"
    BAN_PIC = None
    # Here for later purposes
    SUDO_USERS = [12345, 67890]
    WHITELIST_USERS = [12345, 67890]
    BLACKLIST_USERS = [12345, 67890]
    DEVLOPERS = [12345, 67890]
    OWNER_ID = [12345, 67890]
    SUPPORT_USERS = [12345, 67890]
   # PLUGIN_CHANNEL = int(os.environ.get("PLUGIN_CHANNEL", None)) 
    MAHAKAALBOT_LOGGER = -100×××××××× # REQUIRED
    LYDIA_API_KEY = ""
    HEROKU_API_KEY = ""
    HEROKU_APP_NAME = ""
    TG_BOT_TOKEN_BF_HER = "ENTER BOT TOKEN AND TURN ON INLINE MODE" # REQUIRED
    TG_BOT_USER_NAME_BF_HER = "ENTER BOT USERNAME WITH @" # REQUIRED
    DOWNLOAD_PFP_URL_CLOCK = ""
    PM_PERMIT_GROUP_ID = -100××××××× # REQUIRED
    G_DRIVE_CLIENT_ID = ""
    G_DRIVE_CLIENT_SECRET = ""
    GDRIVE_FOLDER_ID = "root"
    AUTH_TOKEN_DATA = ""
    if AUTH_TOKEN_DATA != None:
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
        t_file = open(TEMP_DOWNLOAD_DIRECTORY+"auth_token.txt","w")
        t_file.write(AUTH_TOKEN_DATA)
        t_file.close()
    PRIVATE_GROUP_ID = -100××××××× # REQUIRED
    if PRIVATE_GROUP_ID != None:
        try:
            PRIVATE_GROUP_ID = int(PRIVATE_GROUP_ID)
        except ValueError:
            raise ValueError("Invalid Private Group ID. Make sure your ID is starts with -100 and make sure that it is only numbers.")


class Development(Var):
    LOGGER = True
