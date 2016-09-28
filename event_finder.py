import facebook
import dateutil.parser

def find_events():
    """
    Uses the Facebook Graph API to find UC Berkeley club events and return them in a list.
    Queries the API for relevant events and then the name, event, and start and end times are 
    added to the list if they exist.
    """
    graph = facebook.GraphAPI(access_token='EAAbfOTcPIK8BAPdwJK80Bi700scXZAnxN9jjx1ggywDoJviyXKqsjAPUkptoDNppcHUIGJqfjmJaPDwAw4qAPFEZCrKxJjQZAcvvm4gHBlcBFqDEFVtxBZB4JtEisbRfZAdVFbXxGMI68ZAv9GDUZBjFiwDwFQnZCh4ZD', version='2.7')
    #graph = facebook.GraphAPI(access_token='1934286690132143|wuzZwiZqs7IwFYEhs5qDS6GgTF4', version='2.7')
    output = []
    def get_events(search):
        nonlocal output
        events = graph.request('search', args={'q': search, 'type': 'event'}, method='GET')
        for event in events['data']:
            if 'name' in event:
                output += [event['name']]
            if 'place' in event and 'name' in event['place']:
                output += [event['place']['name']]
            if 'description' in event:
                output += [event['description']]
            if 'start_time' in event and 'end_time' in event:
                start = dateutil.parser.parse(event['start_time'])
                end = dateutil.parser.parse(event['end_time'])
                output += [start.strftime("%b %d %I:%M%p") + " - " + end.strftime("%I:%M%p")]
            output += ["-"]
    get_events("Apple Infosession")
    get_events("EY Infosession")
    get_events("Verizon Infosession")
    get_events("Adobe Infosession")
    get_events("Google Infosession")
    return output
