from bs4 import BeautifulSoup
import requests
import json
from datetime import datetime

# declare variables
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
gsoc_timeline_url = requests.get("https://developers.google.com/open-source/gsoc/timeline")

try:
    soup = BeautifulSoup(gsoc_timeline_url.content, 'html5lib') 
except ConnectionError: 
    print('No internet connection. Please make sure you have a working internet connection!')


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
        results.append("GSoC isn't happening now. Please check later or visit https://summerofcode.withgoogle.com for more info")
        print("GSoC isn't happening now!")
    else:
        print("\n".join(results))
            
    # dumps results in a json file for bots to read
    with open('data.json', 'w', encoding='utf-8') as f:
        data = json.dumps({'length' : len(results), 'data' : results }, indent = 4, sort_keys=True)
        f.write(data)
        f.close()
        
if __name__ == '__main__':
    main()
