from bs4 import BeautifulSoup
import requests
import json
from datetime import datetime

# declare variables
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
gsoc_timeline_url = requests.get("https://developers.google.com/open-source/gsoc/timeline")

soup = BeautifulSoup(gsoc_timeline_url.content, 'html5lib')

# get GSoC timeline table
table = soup.find('table')

# get all trs in the table body
trs = table.tbody.findAll('tr')

# format date and and time according to GSoC specifications
def format_date(timeline):
    return timeline.split() # make list to get date and time


def main():
    results = [];
    rows = []
    for tr in trs:
        rows.append([col.text for col in tr.findAll('td')])

    for row in rows[1:]:
        formatted_date = format_date(row[0])
        if formatted_date[0] in months and formatted_date[0] == datetime.now().strftime("%B"):
            results.append(row[0] + " - " + row[1])
     
    if len(results) < 0:
        print("No timeline available at this time")
    else:
        for result in results:
            print(result + "\n")
            
    # dumps results in a json file for bots to read
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump({ 'data' : results }, f, ensure_ascii = False, indent = 4)

if __name__ == '__main__':
    main()
