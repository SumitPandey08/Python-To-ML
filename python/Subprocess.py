import subprocess
import time
import os

def open_application():
    file_address = r"F:\Kalki"
    if os.path.exists(file_address):
        try:
            subprocess.Popen([file_address])
        except PermissionError:
            print(f"Error: Permission denied for {file_address}. Please run as administrator.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"Error: The file at {file_address} was not found.")

if __name__ == "__main__":
    # Wait for 5 seconds
    time.sleep(5)
    # Open the application
    open_application()
