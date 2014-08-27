from applets.applet import Applet


class GreetingApplet(Applet):

    def __init__(self, greeting=None, next_applet=None):
        self.greeting = greeting
        self.next_applet = next_applet

    def handle(self, req, res):
        if self.greeting:
            res.say(self.greeting)
        if self.next_applet:
            self.redirect(res, self.next_applet)
        return res
