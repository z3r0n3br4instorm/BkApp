import urllib.request
import os
print("Setting Up Installer Environment...")
os.system("pip install colorama")
from colorama import init, Fore, Style
init()

mongoDB = "https://fastdl.mongodb.org/windows/mongodb-windows-x86_64-7.0.11-signed.msi"
mongoDBF = "mongodb-windows-x86_64-7.0.11-signed.msi"
mongoDBCompass = "https://downloads.mongodb.com/compass/mongodb-compass-1.43.1-win32-x64.exe"
mongoDBCompassF = "mongodb-compass-1.43.1-win32-x64.exe"

def info(data):
    print(Fore.CYAN + "[INFO] " + Style.RESET_ALL + str(data))

def success(data):
    print(Fore.GREEN + "[SUCCESS] " + Style.RESET_ALL + str(data))

def warning(data):
    print(Fore.YELLOW + "[WARNING] " + Style.RESET_ALL + str(data))

def error(data):
    print(Fore.RED + "[ERROR] " + Style.RESET_ALL + str(data))

info("Princeton Plainsboro Teaching Hospital | Software Department")
print(Fore.MAGENTA + "--------------------------------------")
print("OPD Management System Installer Script")
print("--------------------------------------" + Style.RESET_ALL)
print(Fore.CYAN + "Installer version: 0.0.3 | CLI" + Style.RESET_ALL)

os.system("pause")

info("Initializing Installer...")

info("Downloading MongoDB - Community Edition, this may take a while...")

urllib.request.urlretrieve(mongoDB, mongoDBF)
success("MongoDB Downloaded!")
print(f"Downloaded file to {mongoDBF}")
info("Initializing MongoDB Installer...")
os.system(f"start {mongoDBF}")

info("Downloading MongoDB Compass...")
urllib.request.urlretrieve(mongoDBCompass, mongoDBCompassF)
success("MongoDB Compass Downloaded!")
print(f"Downloaded file to {mongoDBCompassF}")
info("Initializing MongoDB Compass Installer...")
os.system(f"start {mongoDBCompassF}")

info("Installing Required Libraries...")
os.system("pip install PyQt5 pymongo")

info("Installing Space Grotesk Font...")
warning("Click 'Install' in the next window...")
os.system("start data/SpaceGrotesk-VariableFont_wght.ttf")

info("Setting up MongoDB Environment...")
info("Running 'createDoctor.py'...")
os.system("python createDoctor.py")

success("Installer Script Completed!")

os.system("pause")