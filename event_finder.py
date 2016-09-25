import facebook
from datetime import datetime
import dateutil.parser

def find_events():
    graph = facebook.GraphAPI(access_token='EAACEdEose0cBANKIjzrBn5fI2zZC3MMITLLWZCfLsl2LRiLsaW7rZCPJo6wqevY5vB3cwruIQx1ZAJT0rb6LBcQQt80BGJkVnwJc0nX6ssjuTtDijX8bv0tILVFclMR155TSx9ZBn7TM4bp9r0j6fcZCPV20NRlraS25Qs7glf9AZDZD', version='2.7')

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
        output += ["-"]
    return output
