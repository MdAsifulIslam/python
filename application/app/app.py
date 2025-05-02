import time
from datetime import datetime
import winsound

def alarm_every_one_minutes():
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"Current Time: {current_time}")
        winsound.Beep(1000, 1000)  # Beep sound for 1 second
        time.sleep(60)  # Wait for 2 minutes

if __name__ == "__main__":
    alarm_every_one_minutes()

# This script will beep every minute and print the current time to the console.
# To run this script, make sure you have Python installed on your system.