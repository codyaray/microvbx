import config
from flask import Flask, request
from twilio.twiml import Response

app = Flask(__name__)
app.secret_key = config.SECRET_KEY
app.config.from_object(__name__)


@app.route("/", methods=['GET', 'POST'])
def flow():
    applet = config.APPLETS[request.values.get('applet', 'start')]
    return str(applet.handle(request, Response()))

if __name__ == "__main__":
    app.run(debug=True)