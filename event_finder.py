import facebook
from datetime import datetime
import dateutil.parser

def find_events():
    graph = facebook.GraphAPI(access_token='EAACEdEose0cBAF5rigVzmxs8U481ean1iizEgAf0ocfiyZBjBWPk4zZAvImoJROHIvm9uyGayKx5I0tducx6ZAzDkDAy5kjRjPNLpIXifsQVWnsdzpfLmiqKxqfM2L6ZA4ERmIfaNfdA9KhZAClUr81l5luXkRXNo3KxIqeJfHQZDZD', version='2.7')

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
    return output
