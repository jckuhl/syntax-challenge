import math
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://syntax.fm/')

play_controls = driver.find_elements(By.CLASS_NAME, 'show__playcontrols')

durations = []
selector = '.player__section button p:last-child'
for control in play_controls:
    control.click()
    time = driver.find_element(By.CSS_SELECTOR, selector)
    duration = time.text.split(' / ')[1].strip()
    durations.append(duration)

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

driver.quit()