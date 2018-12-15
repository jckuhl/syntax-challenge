import xml.etree.ElementTree as ET
import math

tree = ET.parse('./feed.xml')
rss = tree.getroot()
channel = rss.getchildren()[0]

items = [item for item in channel.getchildren() if item.tag == 'item']

durations = []
for item in items:
    for child in item.getchildren():
        if('duration' in child.tag):
            durations.append(child.text)

totals = {
    'hours': 0,
    'minutes': 0,
    'seconds': 0
}

for duration in durations:
    timestamp = [int(t) for t in duration.split(':')]
    if len(timestamp) == 2:
        totals['hours'] += 0
        totals['minutes'] += timestamp[0]
        totals['seconds'] += timestamp[1]
    else:
        totals['hours'] += timestamp[0]
        totals['minutes'] += timestamp[1]
        totals['seconds'] += timestamp[2]

seconds = totals['seconds'] % 60
minutes = math.floor(totals['seconds'] / 60) + totals['minutes']
hours = math.floor(minutes / 60) + totals['hours']
minutes = minutes % 60

print(f'{hours}:{minutes}:{seconds}')

