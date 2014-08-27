from applets.applet import Applet


class HangupApplet(Applet):

    def __init__(self, session):
        self.session = session

    def handle(self, req, res):
        print self.session
        res.hangup()
        return res
