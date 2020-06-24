import os
import os
import sys
import shutil
from typing import Set

import heroku3
from git import Repo
from git.exc import InvalidGitRepositoryError, GitCommandError
from pySmartDL import SmartDL
from dotenv import load_dotenv
from pyrogram import Filters

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH")
    # Get these values from my.telegram.org
    # to store the channel ID who are authorized to use the bot
    AUTH_CHANNEL = int(os.environ.get("AUTH_CHANNEL", -100))
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
    CUSTOM_FILE_NAME = os.environ.get("CUSTOM_FILE_NAME", "")
    LEECH_COMMAND = os.environ.get("LEECH_COMMAND", "leech")
    YTDL_COMMAND = os.environ.get("YTDL_COMMAND", "ytdl")
    RCLONE_CONFIG = os.environ.get("RCLONE_CONFIG", "")
    DESTINATION_FOLDER = os.environ.get("DESTINATION_FOLDER", "TorrentLeech-Gdrive")
    GLEECH_COMMAND = os.environ.get("GLEECH_COMMAND", "gleech")
    INDEX_LINK = os.environ.get("INDEX_LINK", "")
    TELEGRAM_LEECH_COMMAND_G = os.environ.get("TELEGRAM_LEECH_COMMAND_G", "tleech")
    UPSTREAM_REPO = os.environ.get("UPSTREAM_REPO", "https://github.com/gautamajay52/TorrentLeech-Gdrive")
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    UPSTREAM_REMOTE = 'upstream'
    HEROKU_APP = None
    HEROKU_GIT_URL = None
    
    if Config.HEROKU_API_KEY:
    #_LOG.info("Checking Heroku App...")
    for heroku_app in heroku3.from_key(Config.HEROKU_API_KEY).apps():
        if (heroku_app and Config.HEROKU_APP_NAME
                and heroku_app.name == Config.HEROKU_APP_NAME):
           # _LOG.info("Heroku App : %s Found...", heroku_app.name)
            Config.HEROKU_APP = heroku_app
            Config.HEROKU_GIT_URL = heroku_app.git_url.replace(
                "https://", "https://api:" + Config.HEROKU_API_KEY + "@")
            if not os.path.isdir(os.path.join(os.getcwd(), '.git')):
                tmp_heroku_git_path = os.path.join(os.getcwd(), 'tmp_heroku_git')
               # _LOG.info("Cloning Heroku GIT...")
                Repo.clone_from(Config.HEROKU_GIT_URL, tmp_heroku_git_path)
                shutil.move(os.path.join(tmp_heroku_git_path, '.git'), os.getcwd())
                shutil.rmtree(tmp_heroku_git_path)
            break

#_LOG.info("Checking REPO...")
try:
    _REPO = Repo()
except InvalidGitRepositoryError:
    _REPO = Repo.init()
if Config.UPSTREAM_REMOTE not in _REPO.remotes:
    _REPO.create_remote(Config.UPSTREAM_REMOTE, Config.UPSTREAM_REPO)
try:
    _REPO.remote(Config.UPSTREAM_REMOTE).fetch()
except GitCommandError as error:
    #_LOG.error(error)
    sys.exit()
