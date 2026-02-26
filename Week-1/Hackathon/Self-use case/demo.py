import subprocess
import sys
from collections import Counter
import requests

APP_NAME = "python"          
APP_PORT = "8080"             
LOG_FILE = "app.log"          
ERROR_THRESHOLD = 50          

def run_command(command):
    return subprocess.run(command, capture_output=True, text=True)

def check_process():
    print("Checking application process...")
    result = run_command(["pgrep", "-f", APP_NAME])
    pids = [pid for pid in result.stdout.strip().split("\n") if pid]
    if not pids:
        print("Application not running")
        return False
    if len(pids) > 1:
        print("Warning: Multiple instances detected")
    return True

def check_port():
    print("Checking port binding...")
    result = run_command(["ss", "-tulnp"])
    if f":{APP_PORT}" not in result.stdout:
        print("Port not bound correctly")
        return False
    return True

def check_logs():
    print("Analyzing logs...")
    keywords = ["ERROR", "TIMEOUT", "CONNECTION_REFUSED"]
    counter = Counter()
    try:
        with open(LOG_FILE, "r") as f:
            for line in f:
                for k in keywords:
                    if k in line:
                        counter[k] += 1
    except FileNotFoundError:
        print("Log file not found")
        return False
    total_errors = sum(counter.values())
    print(f"Total critical log entries: {total_errors}")
    if total_errors > ERROR_THRESHOLD:
        print("Log anomaly detected")
        return False
    return True

def health_check():
    print("Performing health check...")
    try:
        response = requests.get(f"http://localhost:{APP_PORT}/health", timeout=5)
        if response.status_code == 200:
            return True
        else:
            print(f"Health check failed with status {response.status_code}")
            return False
    except Exception as e:
        print(f"Health check error: {e}")
        return False

def main():
    if not check_process():
        sys.exit(1)
    if not check_port():
        sys.exit(1)
    if not check_logs():
        sys.exit(1)
    if not health_check():
        sys.exit(1)
    print("Deployment Validation Successful")
    sys.exit(0)

if __name__ == "__main__":
    main()
