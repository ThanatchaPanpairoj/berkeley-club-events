from event_finder import find_events

from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)
app.config["DEBUG"] = True

events = find_events()

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template("index.html", events=events)
    
    events.append(request.form["contents"])
    return redirect(url_for('index'))

