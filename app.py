from flask import Flask, request, session
from twilio.twiml import Response

from config import SECRET_KEY


app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config.from_object(__name__)


@app.route("/<flow>", methods=['GET', 'POST'])
def twiml(flow):
    try:
        flow = __import__("flows.%s" % flow, fromlist=["flows"]).APPLETS
        applet = flow[request.values.get('applet', 'start')]
        return str(applet.handle(request, Response()))
    except ImportError:
        return "Unknown flow requested", 404,

if __name__ == "__main__":
    app.run(debug=True)
