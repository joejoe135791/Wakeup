import time
import datetime
from datetime import datetime
import requests
import feedparser
import json
from dotenv import load_dotenv
import os

load_dotenv()
currentDate = datetime.now()
print("Sanity check: If you can read this, The first 12 lines of code are working")
print()
print("The current Date is", currentDate.month, currentDate.day, currentDate.year, "-", currentDate.hour,":", currentDate.minute)