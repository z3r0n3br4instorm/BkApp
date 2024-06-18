import subprocess
def error(error):
        subprocess.Popen(["python", "notifications/error.py", error])
def success(success):
        subprocess.Popen(["python", "notifications/notific.py", success])