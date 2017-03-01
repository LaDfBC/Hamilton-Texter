import urllib2
from bs4 import BeautifulSoup
from twilio.rest import TwilioRestClient

TWILIO_ACCOUNT_SID='YOUR_ACCOUNT_SID'
TWILIO_AUTH_TOKEN='YOUR_AUTH_TOKEN'

def get_events():
    request = urllib2.Request('http://www.fabulousfox.com/events', headers={'User-Agent': 'Mozilla/5.0'})
    page = urllib2.urlopen(request).read()
    soup = BeautifulSoup(page)
    event_titles = []

    header_class = soup.findAll("h3", class_="evtitle")

    for event in header_class:
        event_titles.append(event.get_text())

    return event_titles

def check_hamilton():
    all_events = get_events()

    for event in all_events:
        event = event.encode('ascii', 'ignore')
        if "AIN" in event:
            send_text()

def send_text():

    client = TwilioRestClient(account='AC67d80ac6af081fab2ba6c5a8cf225219',
                              token='876010ab4ed02b7d09ba8e168214f7c3')

    client.messages.create(from_='13146268191',
                       to='3146605324',
                       body='Hamilton TIX ARE IN!')
check_hamilton()