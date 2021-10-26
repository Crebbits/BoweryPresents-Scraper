import requests
import re
import time
import winsound
from bs4 import BeautifulSoup

# def main():
#     recursion(1)

with requests.Session() as s:
    root_url = "https://www.bowerypresents.com/info/events/get?scope=all&page=1&rows=99&venues=new-york-metro"

    lxml = s.get(root_url).text
    soup = BeautifulSoup(lxml, 'lxml')
    empty = ''
    event_notifier = []

    bowerybody = soup.find("body")
    boweryevent = bowerybody.find_all('div', class_='show-item')

    for event in boweryevent:
        eventdate = [a.text.strip() for a in event.select('p[class="list-date"]')]
        eventname = [a.text.strip() for a in event.select('span[itemprop="name"]') if a.text.strip() != empty]
        supporting = [a.text.strip() for a in event.select('span[itemprop="performer"]')]
        for date in eventdate:
            eventdate = date.replace('\n','')
            eventdate = re.sub(' +', ' ', eventdate)
        for opener in supporting:
            if opener == empty:
                print (eventname, eventdate)
            else:
                print(eventname, supporting, eventdate)

#
#
# def eventalert():
#     for vettix_date in vettix_dates:
#         vettix_edate = [a.text.strip() for a in vettix_date.select("p > strong")]
#         vettix_event = [a.text.strip() for a in vettix_date.select('div.date-1')]
#         for text in vettix_event:
#             if any(word in text for word in event_notifier):
#                 print(text, vettix_edate)
#                 winsound.Beep(440, 250)
#                 time.sleep(.5)
#
#
# def recursion(k):
#     if k > 0:
#         # printevent()
#         printnextpage()
#         eventalert()
#         time.sleep(600)
#         recursion(1)
#
#
# if __name__ == "__main__":
#     main()