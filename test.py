from bs4 import BeautifulSoup
import requests
from datetime import datetime, timezone, timedelta
import pytz

# declare variables
rows = []
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
page = requests.get("https://developers.google.com/open-source/gsoc/timeline")

soup = BeautifulSoup(page.content, 'html5lib')

# get GSOC timeline table
table = soup.find('table')

#get all trs in the table body
trs = table.tbody.findAll('tr')

# print(datetime.now().month)
# print(datetime.now().day)
# print(time.tzname)

for tr in trs:
    rows.append([col.text for col in tr.findAll('td')])

for me in rows[1:]:
        print(f"Time: {me[0]} - Activity performed {me[1]}")
