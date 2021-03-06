import requests, json
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def api():
    r = request.json
    username = r['receiver']
    for alerts in r['alerts']:
        if alerts['status'] == "resolved":
            color = 182388
        else:
            color = 16711680
        payload = {
            "username": username,
            "embeds": [{
                "title": (alerts['status']).upper() + ' ：' + '[ ' + alerts['labels']['alertname'] + ' ]',
                "description": alerts['annotations']['description'],
                "color": color,
                "fields": [{
                    "name": "severity",
                    "value": alerts['labels']['severity'],
                    "inline": "true"
                },{
                    "name": "hostname",
                    "value": alerts['labels']['instance'],
                    "inline": "true"
                },{
                    "name": "summary",
                    "value": alerts['annotations']['summary'],
                    "inline": "false"
                }]
            }]
        }
        requests.post('https://discordapp.com/api/webhooks/679XXXXXXXX778/iC4SXpabRqB5PrGNfx7HpFXXXXXXXXXXXXXXTW8GUOQ17LuQk3UQXBRryL1SotyRy', json=payload, headers = {"Content-Type": "application/json"})
        #you need preproduce a discord webhook for replacement request.post('url') to send alerts towards discord youself chennel
    return 'Hello'

app.run(host='0.0.0.0')
