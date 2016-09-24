import facebook
import json

def find_events():
 
    graph = facebook.GraphAPI(access_token='EAAEiEv7tZBwUBAIwy3SPJZAMB0pPFzLPzDOowPKNZBcjciWaLfaDOuk1xCFtlJWUBjMcgFjOI5FgX5sjids2lT6r7sdyZBVgchlQL90JNM6Q2SxsGIXviXUtx0fp6gzPGy8m5B77IGjYoeD6pVSK5iKL9jO3gMkJgkfG9pbN8wZDZD', version='2.7')
    def pp(o):
        return json.dumps(o, indent=1)
    return pp(graph.request("search", {'q' : 'Berkeley, CA', 'type' : 'event'}))
    
