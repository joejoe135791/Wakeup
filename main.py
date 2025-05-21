import time
import datetime
from datetime import datetime
import requests
import threading
import logging
import json
from dotenv import load_dotenv
import os
import toml

load_dotenv()
with open('config.toml', 'r') as f:
    config = toml.load(f)
sysLogger = logging.basicConfig()

currentDate = datetime.now()
print("Sanity check: If you can read this, The first 12 lines of code are working")
print(f"The current Date is {currentDate.month}/{currentDate.day}/{currentDate.year}-{currentDate.hour}:{currentDate.minute}")
print("The script is ready!")