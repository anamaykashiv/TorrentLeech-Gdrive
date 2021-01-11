from tobrot.sample_config import Config

class Config(Config):
    TG_BOT_TOKEN= "1556682867:AAEXDAhwdU1Ur3ye4XrXkTJy6ZEPXzOYAbI"
    APP_ID = 2814333
    API_HASH = "a4a7d01c04c2edb86e034234ee7c950f"
    AUTH_CHANNEL = [-1001171321074,-1001198967649]
    INDEX_LINK = "https://jarvismirror.anamay.workers.dev/0:/jarvis%20mirror"
    OWNER_ID = 1479420774
    GLEECH_COMMAND = "gleech"
    YTDL_COMMAND = 'ytdl'
    TELEGRAM_LEECH_COMMAND_G = "tleech"
    CLONE_COMMAND_G = "gclone"
    PYTDL_COMMAND_G = "pytdl"
    STATUS_COMMAND = "status"
    DESTINATION_FOLDER = ""
    LEECH_COMMAND = "leech"
    #fill your rclone config like this(Your config may have some extra value or less. so Don't worry)
    # Do not delete [DRIVE] #do not delete [DRIVE] but replace remaining part with yours data..if more data use common sense
    RCLONE_CONFIG = """
[DRIVE]
type = drive
scope = drive
root_folder_id = 1-cduLmaiOe9zHMU7u8DpN9Uyuc7Z1PIi
token = {"access_token":"ya29.a0AfH6SMA3iOfRn3jkm93ge8w9M2r7IynCX4ZZFVUPKa9L-S8AzlPvOg9AnNxcx7RFLv6P1LK-OOrwYl42M_0k6V2S9tRKfEs27xf3KJ9tOS6QNxRRrpYgz4pHh-4wgtAlxthziohRTPkt1IsqnL8XZESzvP5nvlKvQ1okg81_QVA","token_type":"Bearer","refresh_token":"1//0gTE99S8O9s_VCgYIARAAGBASNwF-L9IrIAkEAhv-_2aN-ZjQ9zdNz_hPoLSKfWgywGIBSr3ur37d4W4-NxFiC4cvgzptJ_DXb7k","expiry":"2021-01-11T05:44:23.310735969Z"}
team_drive = 0ACIL4SHb6WoEUk9PVA"""
