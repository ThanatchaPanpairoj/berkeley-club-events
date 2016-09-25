import facebook
from datetime import datetime
import dateutil.parser

def find_events():
    graph = facebook.GraphAPI(access_token='EAACEdEose0cBAECWoZBeZAc0eVZBTVvAyX4xZAhy6ZCzVvJQqDs3WsTVzCuQ4mIdWwxfPhFArVU245YsJWsLxSwrFHUdpoh0NOpL47948X2e2p0ZCUr2aZBTurNQnAyR1q2tiwMvOu4zfJWyEfwZCw496H2KCHg30A0TTnYqAqr2eAZDZD', version='2.7')

    events = graph.request('search', args={'q': 'berkeley club', 'type': 'event'}, method='GET')
    output = []
    for event in events['data']:
        if 'name' in event:
            output += [event['name']]
        if 'location' in event:
            output += [event['location']]
        if 'start_time' in event and 'end_time' in event:
            start = dateutil.parser.parse(event['start_time'])
            end = dateutil.parser.parse(event['end_time'])
            output += [start.strftime("%I:%M%p") + " - " + end.strftime("%I:%M%p")]
        output+= ["\n"]
    return output
