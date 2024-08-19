# example_script.py

import datetime

def print_current_date():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")
    
if __name__ == "__main__":
    print_current_date()