import os
import platform
import psutil

from pathlib import Path

WINDOW_SIZE = (900, 564)

AUTH_URL = "https://auth.cubedvij.pp.ua"

LAUNCHER_DIRECTORY = Path(__file__).parent
LAUNCHER_VERSION = "0.1.0"
LAUNCHER_NAME = "Кубічний Лаунчер"

if platform.system() == "Windows":
    APPDATA_FOLDER = Path.home() / "AppData" / "Roaming"
if platform.system() == "Linux":
    APPDATA_FOLDER = Path.home() / ".config"

APPDATA_FOLDER /= "cubedvij"
SKINS_CACHE_FOLDER = APPDATA_FOLDER / ".skins_cache"
if not os.path.exists(SKINS_CACHE_FOLDER):
    os.makedirs(SKINS_CACHE_FOLDER)
if not os.path.exists(APPDATA_FOLDER):
    os.makedirs(APPDATA_FOLDER)

MINECRAFT_FOLDER = APPDATA_FOLDER / ".minecraft"
if not os.path.exists(MINECRAFT_FOLDER):
    os.makedirs(MINECRAFT_FOLDER)


ACCOUNT_FILE = APPDATA_FOLDER / "account.json"
if not os.path.exists(ACCOUNT_FILE):
    with open(ACCOUNT_FILE, "w") as f:
        f.write("{}")

USER_FILE = APPDATA_FOLDER / "user.json"
if not os.path.exists(USER_FILE):
    with open(USER_FILE, "w") as f:
        f.write("{}")


JVM_ARGS = [
    "-XX:+UnlockExperimentalVMOptions",
    "-XX:+UseG1GC",
    "-XX:G1NewSizePercent=20",
    "-XX:G1ReservePercent=20",
    "-XX:MaxGCPauseMillis=50",
    "-XX:G1HeapRegionSize=32M",
]

# IN MB
RAM_SIZE = psutil.virtual_memory().total // 1024 // 1024
RAM_STEP = 256