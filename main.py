from bs4 import BeautifulSoup
import requests
from datetime import datetime

# declare variables
rows = []
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
gsoc_timeline_url = requests.get("https://developers.google.com/open-source/gsoc/timeline")

soup = BeautifulSoup(gsoc_timeline_url.content, 'html5lib')

# get GSoC timeline table
table = soup.find('table')

#get all trs in the table body
trs = table.tbody.findAll('tr')

# format date and and time according to GSoC specifications
def format_date(timeline):
    return timeline.split() # make list to get date and time


def main():
    for tr in trs:
        rows.append([col.text for col in tr.findAll('td')])

    for row in rows[1:]:
        formatted_date = format_date(row[0])
        if formatted_date[0] in months and formatted_date[0] == datetime.now().strftime("%B"):
            return row[0] + " - " + row[1]

if __name__ == '__main__':
    print (main())
