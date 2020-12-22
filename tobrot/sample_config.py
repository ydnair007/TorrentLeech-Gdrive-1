import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1436489993:AAGXKRFV5o5dEJtZHVbSpiNgHvJ7AQ2FVIg")
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 1367358))
    API_HASH = os.environ.get("API_HASH", "7fcac8ce09043cd179a1c41d09b04614")
    # Get these values from my.telegram.org
    # to store the channel ID who are authorized to use the bot
    AUTH_CHANNEL = int(os.environ.get("AUTH_CHANNEL", -1001497657743))
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 1572864000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    #
    ARIA_TWO_STARTED_PORT = int(os.environ.get("ARIA_TWO_STARTED_PORT", 6800))
    EDIT_SLEEP_TIME_OUT = int(os.environ.get("EDIT_SLEEP_TIME_OUT", 15))
    MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START = int(os.environ.get("MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START", 600))
    MAX_TG_SPLIT_FILE_SIZE = int(os.environ.get("MAX_TG_SPLIT_FILE_SIZE", 1072864000))
    # add config vars for the display progress
    FINISHED_PROGRESS_STR = os.environ.get("FINISHED_PROGRESS_STR", "█")
    UN_FINISHED_PROGRESS_STR = os.environ.get("UN_FINISHED_PROGRESS_STR", "░")
    # add offensive API
    TG_OFFENSIVE_API = os.environ.get("TG_OFFENSIVE_API", None)
    CUSTOM_FILE_NAME = os.environ.get("CUSTOM_FILE_NAME", "Scotch ")
    RCLONE_CONFIG = os.environ.get("RCLONE_CONFIG", "type = drive 
                                   client_id = 1023363715542-659gq0fr64168rsa0up71vc77goj0g99.apps.googleusercontent.com 
                                   client_secret = KO4utgfVeSloOhGs8wvAVEIk 
                                   scope = drive 
                                   root_folder_id = 1BgNi460fFos1qT4vWSn4QKTLdRTSnABC 
                                   token = {"access_token":"ya29.a0AfH6SMBPs9cXM4J6jdrpEtXmVp7nSrmvuWuwHPIl9F-Nq7XtQeMIsibxLdJcNNNDxdY6fdRbOYskDoo05qw-PyqXrFAFqvp3skXaZNUL79zeSQyiCglRR2Nb_f3AG92nnTZNTvJAoZ0MVo9poq2bCCSfib3mv6sM2M5E5qnT0Ms","token_type":"Bearer","refresh_token":"1//0gvFG8gxY3_08CgYIARAAGBASNwF-L9IrHd-CTZjPKW5KprbgL5inkrnRh9lxlpwYASwV-WOFYCiEUlbVrAJ_RKzmhDTqgd7C_Ro","expiry":"2020-12-22T04:31:02.8079769+05:30"}")
    DESTINATION_FOLDER = os.environ.get("DESTINATION_FOLDER", "1BgNi460fFos1qT4vWSn4QKTLdRTSnABC")
    GLEECH_COMMAND = os.environ.get("GLEECH_COMMAND", "gleech")
    INDEX_LINK = os.environ.get("INDEX_LINK", "")
    TELEGRAM_LEECH_COMMAND_G = os.environ.get("TELEGRAM_LEECH_COMMAND_G", "tleech")
