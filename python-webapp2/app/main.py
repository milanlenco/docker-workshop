from flask import Flask
import redis
import datetime

app = Flask(__name__)
db = redis.StrictRedis(host='redis', port=6379, db=0)

@app.route('/')
def hello_world():
    last_visit = db.get("last-visit")
    if last_visit is None:
        html = '<html><h1 style="color:green">Hello Docker!</h1> This is your <b>first</b> visit.</html>'
    else:
        last_visit = last_visit.decode('utf-8')
        html = '<html><h1 style="color:green">Hello Docker!</h1> Your last visit: <b>%s</b>.</html>' % last_visit
    date = datetime.datetime.now().strftime("%H:%M:%S %d-%m-%Y")
    db.set("last-visit", date.encode('utf-8'))
    return html

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
