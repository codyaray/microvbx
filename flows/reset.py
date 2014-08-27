from flask import session as flask_session
from twilio.twiml import Say
from applets.applet import Applet


class ResetSessionApplet(Applet):
    def __init__(self, session):
        self.session = session

    def handle(self, req, res):
        self.session.clear()
        res.say("Your session has been cleared. Goodbye", voice=Say.WOMAN)
        res.hangup()
        return res

APPLETS = {
    "start": ResetSessionApplet(flask_session)
}